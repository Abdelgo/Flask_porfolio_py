from flask import Flask, render_template
from flask import request, redirect
import pandas as pd
import csv

app = Flask(__name__)
print(__name__)

@app.route('/')
def index():
    return render_template('./index.html')

#@app.route('/<username>')
#def user(username = None):
#    return render_template('./index1.html', name=username[:6], job=username[6:]) #name is the variable put in the html file
@app.route('/<page_name>')
def html_pages(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database_csv:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database_csv, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            #write_to_file(data)
            write_to_csv(data)
            #dataframe = pd.DataFrame.from_dict([data])
            #print(dataframe)
            return redirect('./thanks.html')
        except:
            return 'did not save the database'
    else:
        return 'something is wrong'







'''
@app.route('/about.html')
def about():
    return render_template('./about.html')

@app.route('/components.html')
def components():
    return render_template('./components.html')

@app.route('/contact.html')
def contact():
    return render_template('./contact.html')

@app.route('/work.html')
def work():
    return render_template('./work.html')

@app.route('/works.html')
def works():
    return render_template('./works.html')
'''

