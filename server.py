from flask import Flask, render_template,url_for, request , redirect

import csv

app = Flask(__name__)
@app.route("/")     
def my_home():   
    return render_template('index.html')

@app.route("/<string:page_name>")     
def html_page(page_name=None):   
    return render_template(page_name)

def write_to_file(data):
    with open('./database.txt', mode='a') as my_Db:     
          email =   data["email"]
          subject = data["subject"]
          message = data["message"]
          file = my_Db.write(f'\n{email};{subject},{message}')
          print(file)

def write_to_csv(data):
    with open('./database.csv', mode='a',newline='') as my_Db2:     
          email =   data["email"]
          subject = data["subject"]
          message = data["message"]
          csv_writer = csv.writer(my_Db2,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)   ##quotechar='' just means empty string
          csv_writer.writerow([email,subject,message])
          print(csv_writer)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            print(data)
            write_to_file(data)
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'something went wrong, Try again! '  


# the   below code is very basic , nothing dynamique


# @app.route("/index.html")     
# def my_index():   
#     return render_template('index.html')

# @app.route("/works.html")     
# def works():   
#     return render_template('works.html')

# @app.route("/about.html")
# def about():
#     return render_template('about.html')

# @app.route("/contact.html")
# def contact():
#     return render_template('contact.html')



# @app.route("/<username>/<int:post_id>")     #username represents a parameter
# def hello_world(username=None,post_id=None):    #None represent a default value
#    # print (url_for('static', filename='favicon.ico')) ; just testing what "url_for" function do
#     return render_template('index.html',name=username, post_id=post_id)