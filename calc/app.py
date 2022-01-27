# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def add_page():
    a = int(request.args['a'])
    b = int(request.args['b'])
    result = add(a,b)
    return f"{result}"

@app.route('/sub')
def sub_page():
    a = int(request.args['a'])
    b = int(request.args['b'])
    result = sub(a,b)
    return f"{result}"

@app.route('/mult')
def mult_page():
    a = int(request.args['a'])
    b = int(request.args['b'])
    result = mult(a,b)
    return f"{result}"

@app.route('/div')
def div_page():
    a = int(request.args['a'])
    b = int(request.args['b'])
    result = div(a,b)
    return f"{result}"

operations = {
    'add': add,
    'sub': sub,
    'mult': mult,
    'div': div
}

@app.route('/math/<opp>')
def math_page(opp):
    a = int(request.args['a'])
    b = int(request.args['b'])
    result = operations[opp](a,b)
    return f"{result}"