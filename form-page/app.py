from flask import Flask, request, url_for, redirect, render_template
import os
TEMPLATE_DIR = os.path.abspath('../templates')
STATIC_DIR = os.path.abspath('../static')


app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    return render_template('signup.html')

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    return render_template('signin.html')

@app.route('/welcome', methods=['GET', 'POST'])
def welcome():
    return render_template('welcome.html')
 
if __name__ =='__main__':
    app.run(debug = True) 
    app.run(host = '0.0.0.0', port= 5000)