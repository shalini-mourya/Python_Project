from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)
#print (__name__)

@app.route('/')
def main_page():
	return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
	return render_template(page_name)

#Write the data to a file in current project folder

def write_to_file(data):
	with open('database.txt',mode='a') as database:
		email=data["email"]
		subject=data["subject"]
		message=data["message"]
		database.write(f'\n{email},{subject},{message}')
		
#Write the data to a csv in current project folder

def write_to_csv(data):
	with open('database.csv',mode='a', newline='') as csvdatabase:
		email=data["email"]
		subject=data["subject"]
		message=data["message"]
		csv_writer=csv.writer(csvdatabase,delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([email,subject,message])
		
		

#Send Button
@app.route('/submit_form', methods=['POST','GET'])
def submit_form():
	if request.method=='POST':
		data=request.form.to_dict()
		write_to_csv(data)
		return redirect('/thankyou.html')
	else:
		return 'something wnet wrong. Try again!'





#@app.route('/<username>')
#def nextpage(username=None):
#	 return render_template('index.html', name=username)

	