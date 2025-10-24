from flask import Flask, render_template
app = Flask(__name__)
#print (__name__)

@app.route('/')
def hello_world():
	#return 'Hello, World only if you hit route!'
     return render_template('index.html')

@app.route('/<username>')
def nextpage(username=None):
	 return render_template('index.html', name=username)

	