% include('header.tpl')



<p align="right">
Page:<b>/{{path}}</b>, Author:<b>{{pageuser}}</b>, Created:<b>{{created.strftime('%Y/%m/%d %H:%M:%S')}}</b>
</p>

<h1 class="wikititle">{{title}}</h1>





<div class="wikivers">

<a href="/">Home</a> -
%if user:
Logged user:</b>{{user}}</b> - <a href="/logout">Logout</a> 
%else:
<a href="/login">Login</a>
%end
- <a href="/edit/{{path}}">Edit</a>

<hr>
<form method="POST" action="/upload/{{path}}" enctype="multipart/form-data">
<input type="file" name="upload">
<input type="submit" value="Upload">
</form>
<hr>


%if len(allversions) > 1:
<b>Found {{len(allversions)}} versions:</b>
<table>
<tr><th>#</th><th>Data</th><th>User</th><th>Title</th></tr>
%for i,vv in enumerate(allversions):
<tr>
<td>{{i}}</td>
<td>{{vv.created.strftime('%Y/%m/%d %H:%M:%S')}}</td>
<td>{{d_users.get(vv.user_id,'??')}}</td>
<td><a href="/{{path}}?v={{i}}">{{vv.title}}</a></td>
</tr>
%end
</table>
%else:
<b>Just one version.</b>
%end

<br/>


%if len(files) > 0:
<b>Found {{len(files)}} uploaded files:</b><br/>
<ul>
%for i,vv in enumerate(files):
<li>{{i}}: <a href="/get/{{vv.Id}}">{{vv.Filename}}</a> - {{"%.2f" % (vv.Size/1024./1024.)}} MB</li>
%end
</ul>
%else:
<b>No uploaded files.</b>
%end
</div>


{{!body}}



% include('footer.tpl')
