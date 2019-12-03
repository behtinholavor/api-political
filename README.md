<h1 id="foobar">Political</h1>
<p>Political api is an application program interface that provides access to Brazilian politicians' expenses simply, easily and quickly.</p>

<h2 id="installation">Installation</h2>
<p>Use the command prompt 
	<a href="https://pip.pypa.io/en/stable/">pip</a> to install the required libraries.
</p>

<pre>
<code class="bash language-bash">pip install flask flask-jsonpify flask-sqlalchemy flask-restful</code>
</pre>

<h2 id="usage">Usage</h2>
<pre>
<code class="python language-python">
from flask 		import Flask, request, jsonify
from flask_restful 	import Resource, Api
from sqlalchemy 	import create_engine
from json 		import dumps
</code>
</pre>

<h2 id="contributing">Contributing</h2>
<p>Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.</p>
<p>Please make sure to update tests as appropriate.</p>

<h2 id="license">License</h2>
<p><a href="https://choosealicense.com/licenses/unlicense/">Unlicense</a></p>