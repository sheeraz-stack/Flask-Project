from flask import Flask,redirect,url_for,render_template,request
app = Flask(__name__,template_folder='C:\Users\DELL\flask\templates')

#Building Url dynamically
#variables rules and url building

@app.route('/',methods=['GET'])
def welcome():
	return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):
	res=""
	if score>=50:
		res='PASS'
	else:
		res='FAIl'	
	return render_template('result.html',result=res)

@app.route('/fail/<int:score>')
def fail(score):
	return "<html><body><h1>The Result is pass</h1></body></html>" 

#Result checker
@app.route('/results/<int:marks>')

def results(marks):
	result=""
	if marks < 50:
		result ='fail'
	else:
		result ='success'
	return redirect(url_for(result,score=marks))	

##Result checker Html Page
@app.route('/submit',methods=['POST'])
def submit():
	total_score=0
	
	if request.method=='POST':
		science=float(request.form['science'])
		Maths=float(request.form['Maths'])
		c=float(request.form['c'])
		Datascience=float(request.form['Datascience'])
		total_score=(science+Maths+c+Datascience)/4
	res=""
	if total_score >=50:
		res='success'
	else:
		res='fail'	
	return redirect(url_for(res,score=total_score))	



if __name__=='__main__':
	app.run(debug=True)