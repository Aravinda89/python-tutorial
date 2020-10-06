#set FLASK_APP=flask_decorators.py
#export FLASK_APP=flask_decorators.py
#flask run

from flask import Flask

app = Flask(__name__)

@app.route('/')
def print_fib():
    return '<h1>Fibonacci</h1>'

@app.route('/fib')
def list_fib():
    return '<b>1,1,2,3,5,8...</b>'
