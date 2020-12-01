from flask import Flask, render_template, request, redirect
import csv
# *** https://www.sneppets.com/python/python-importerror-no-module-named-flask/ use this link for explanation in case of any flask errors

app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

# This tells your server that any visits to a path that looks like /index.html or /anypage.html will get handled by this route handler, and that page_name will be set equal to the string after the /
# Look at Flask documentation regarding Variable rules https://flask.palletsprojects.com/en/1.1.x/quickstart/

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'Did not save to database.'
    else:
        return 'Something went wrong, please try again.'

def write_to_file(data):
    with open('database.txt', mode='a') as database:     # write in append mode
        email =  data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database2:     # write in append mode
        email =  data["email"]
        subject = data["subject"]
        message = data["message"]

        # for more info on the csv library https://docs.python.org/3/library/csv.html
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

# @app.route('/about.html')
# def about():
#     return render_template('about.html')
#
# @app.route('/works.html')
# def work():
#     return render_template('works.html')
#
# @app.route('/components.html')
# def components():
#     return render_template('components.html')
#
# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')