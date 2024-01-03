from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def run_add():
    """Add a and b. Returns a string"""
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = add(a, b)
    return str(result)

@app.route('/sub')
def run_sub():
    """Subtract b from a. Returns a string"""
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = sub(a, b)
    return str(result)

@app.route('/mult')
def run_mult():
    """Multiply a and b. Returns a string"""
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = mult(a, b)
    return str(result) 

@app.route('/div')
def run_div():
    """Divide a by b. Returns a string"""
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = div(a, b)
    return str(result)

OPERATORS = {
    'add': add,
    'sub': sub,
    'mult': mult,
    'div':div
}

@app.route('/math/<operation>')
def do_math(operation):
    """Does a math function on a and b. Returns a string"""
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = OPERATORS[operation](a, b)
    return str(result)