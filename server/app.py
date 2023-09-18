#!/usr/bin/env python3

from flask import Flask 

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'


@app.route('/print/<string:parameter>', methods=['GET'])
def print_string(parameter):
    # Print the string to the console
    print(parameter)
    
    # Display the string in the web browser
    return parameter

@app.route('/count/<int:integer>', methods=['GET'])
def count(integer):
    # Create a list of numbers in the specified range, starting from 1
    numbers = range(integer)
    
    # Convert the list of numbers to a string with each number on a separate line
    numbers_str = '\n'.join(map(str, numbers)) + '\n'
    
    # Display the numbers in the web browser
    return numbers_str

@app.route('/math/<num1>/<operation>/<num2>')
def math(num1, operation, num2):
    try:
        num1 = int(num1)  # Try to convert to int
    except ValueError:
        try:
            num1 = float(num1)  # If it's not an int, try to convert to float
        except ValueError:
            return "Invalid input for num1"

    try:
        num2 = int(num2)  # Try to convert to int
    except ValueError:
        try:
            num2 = float(num2)  # If it's not an int, try to convert to float
        except ValueError:
            return "Invalid input for num2"
    result = None

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 != 0:
            result = num1 / num2
        else:
            return "Division by zero is not allowed"
    elif operation == '%':
        result = num1 % num2
    else:
        return "Invalid operation. Supported operations are +, -, *, div, %"

    return str(result)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
