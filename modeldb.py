import datetime

from sqlalchemy import create_engine, Column, Integer, Sequence, String, Unicode, DateTime, LargeBinary, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class WikiPages(Base):
    __tablename__ = 'WikiPages'
    id = Column(Integer, primary_key=True)
    path = Column(Unicode(128))
    created = Column(DateTime, default=datetime.datetime.now)
    version_id = Column(Integer) #pointer to table WikiVersions
    files = relationship("Files", backref="owner")  #field 'owner' defined here is dynamically created in tabela Files, for relation one-to-many
    def __init__(self, path, version_id):
        self.path = path
        self.version_id = version_id

class WikiVersions(Base):
    __tablename__ = 'WikiVersions'
    id = Column(Integer, primary_key=True)
    title = Column(Unicode(128))
    user_id = Column(Integer) #pointer to table Users
    body = Column(Unicode)
    created = Column(DateTime, default=datetime.datetime.now)
    page_id = Column(Integer) #pointer to table WikiPages
    def __init__(self, title, body, user_id, page_id):
        self.title = title
        self.body = body
        self.user_id = user_id
        self.page_id = page_id

class Files(Base):
    __tablename__ = 'Files'
    Id = Column(Integer,  primary_key=True)
    Filename = Column(Unicode(128))
    ContentType = Column(String(128))
    Size = Column(Integer)
    CreationTime = Column(DateTime)
    owner_id = Column(Integer, ForeignKey('WikiPages.id'))
    #owner -> a field dynamically created by backref, which keep the parent object(is not a list because of relation one-to-many)
    def __init__(self, fielname, size, contenttype, owner_id):
        self.Filename = fielname
        self.Size = size
        self.ContentType = contenttype
        self.owner_id = owner_id

class Users(Base):
    __tablename__ = 'Users'
    id = Column(Integer, primary_key=True)
    username = Column(Unicode(64))
    fullname = Column(Unicode(64))
    password = Column(Unicode(64))
    created = Column(DateTime, default=datetime.datetime.now)
    changed = Column(DateTime, default=datetime.datetime.now)
    def __init__(self, username, password):
        self.username = username
        self.fullname = username
        self.password = password



def addUsers(db):
    db.add(Users(u'root',u'123'))
    db.add(Users(u'admin',u'123'))
    db.add(Users(u'john',u'123'))

def addPages(db):
    wikipage = WikiPages(u'/FrontPage',0)
    db.add(wikipage)
    db.commit()
    version = WikiVersions(u'Front Page',u'''# This is the start page
[Home](/) - [Page 1](/page1) - [Page 2](/page2) - [Page 1/Subpage 1](/page1/subpage1)
Wiki server
''',1,wikipage.id)
    db.add(version)
    db.commit()
    wikipage.version_id = version.id
    db.add(wikipage)
    db.commit()


