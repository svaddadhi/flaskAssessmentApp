from flask import Flask, jsonify, request
from Compute import ComputeNums
app = Flask(__name__)

@app.route('/<int:number>/<string:option>')
def chooseRoute(number, option):
    try:
        if option == None:
            displayNums(number)
        elif option == 'odd':
            displayOddNums(number)
        elif option == 'even':
            displayEvenNums(number)
        elif option == 'prime':
            displayPrimeNums(number)
        else:
            return jsonify({'ERROR': 'PLEASE CHOOSE EVEN, ODD, OR PRIME AS AN OPTION OR INPUT A NUMBER AND OMIT THE OPTION PORTION'}), 400
    except Exception as e:
        return jsonify({'ERROR': str(e).upper()}), 500

# route for displaying numbers from 1-N
@app.route('/<int:number>', methods=['GET'])
def displayNums(number):
    try:
        if number < 1:
            return jsonify({'ERROR': 'NUMBER MUST BE GREATER THAN OR EQUAL TO 1'}), 400
        result = ComputeNums(number).showNums()
        return jsonify({'SUCCESS': result}), 200
    except Exception as e:
        return jsonify({'ERROR': str(e).upper()}), 500

# route for displaying odd numbers from 1-N
@app.route('/<int:number>/odd', methods=['GET'])
def displayOddNums(number):
    try:
        if number < 1:
            return jsonify({'ERROR': 'NUMBER MUST BE GREATER THAN OR EQUAL TO 1'}), 400
        result = ComputeNums(number).showOddNums()
        return jsonify({'SUCCESS': result}), 200
    except Exception as e:
        return jsonify({'ERROR': str(e).upper()}), 500

# route for displaying even numbers from 1-N
@app.route('/<int:number>/even', methods=['GET'])
def displayEvenNums(number):
    try:
        if number < 1:
            return jsonify({'ERROR': 'NUMBER MUST BE GREATER THAN OR EQUAL TO 1'}), 400
        result = ComputeNums(number).showEvenNums()
        return jsonify({'SUCCESS': result}), 200
    except Exception as e:
        return jsonify({'ERROR': str(e).upper()}), 500

# route for displaying all prime numbers from 2 - N
@app.route('/<int:number>/prime', methods=['GET'])
def displayPrimeNums(number):
    try:
        if number < 2:
            return jsonify({'ERROR': 'NUMBER MUST BE GREATER THAN OR EQUAL TO 2'}), 400
        result = ComputeNums(number).showPrimeNums()             
        return jsonify({'SUCCESS': result}), 200
    except Exception as e:
        return jsonify({'ERROR': str(e).upper()}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)


