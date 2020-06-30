from flask import Flask, render_template, request, redirect, url_for
import csv
app = Flask(__name__)



@app.route('/')
def index():
    return render_template("index.html")

@app.route('/<string:page_name>')
def components(page_name):
    return render_template(page_name)

@app.route('/submit_form', methods=["POST", "GET"])
def submit_form():
    if request.method == "POST":
    	data = request.form.to_dict()
    	write_to_csv(data)
    	return redirect("thankyou.html")
    else:
    	return "failed"
 
def write_to_file_json(data): #JSON Format
	with open("database.txt", "a") as database:
		database.write(json.dumps(data))

def write_to_file(data): #Desfazendo o dict e append os valores em separado
	with open("database.txt", "a") as database:
		email = data["email"]
		subject = data["subject"]
		message = data["message"]
		database.write(f"\n{email}, {subject}, {message}")

def write_to_csv(data): #Desfazendo o dict e append os valores em separado
	with open("database.csv", "a", newline='') as database_csv:
		email = data["email"]
		subject = data["subject"]
		message = data["message"]
		csv_writer = csv.writer(database_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([email, subject, message])










