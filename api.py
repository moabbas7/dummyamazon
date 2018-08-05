from flask import Flask,request	,render_template

app = Flask(__name__)

@app.route("/home")
def hello_world():
	name_str = request.args.get('name')
	age_str = request.args.get('age')
	return render_template('welcome.html',name=name_str,age=age_str)

@app.route("/what/why")
def something():
	return "We've hit something"

if(__name__ =="__main__"):
	app.run() 

