from flask import Flask, jsonify
app = Flask(__name__)


@app.route('/<int:number>/<string:option>')
def chooseRoute(option):
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
@app.route('/<int:number>')
def displayNums(number):
    try:
        if number < 1:
            return jsonify({'ERROR': 'NUMBER MUST BE GREATER THAN OR EQUAL TO 1'}), 400
        numList = []
        for i in range(1, number + 1):
            numList.append(i)
        return jsonify({'SUCCESS': numList}), 200
    except Exception as e:
        return jsonify({'ERROR': str(e).upper()}), 500

# route for displaying odd numbers from 1-N
# different approach will also be provided
@app.route('/<int:number>/odd')
def displayOddNums(number):
    try:
        if number < 1:
            return jsonify({'ERROR': 'NUMBER MUST BE GREATER THAN OR EQUAL TO 1'}), 400
        numList =[]
        for i in range(1, number + 1, 2):
            numList.append(i)
        return jsonify({'SUCCESS': numList}), 200
    except Exception as e:
        return jsonify({'ERROR': str(e).upper()}), 500

# route for displaying even numbers from 1-N
@app.route('/<int:number>/even')
def displayEvenNums(number):
    try:
        if number < 1:
            return jsonify({'ERROR': 'NUMBER MUST BE GREATER THAN OR EQUAL TO 1'}), 400
        numList =[]
        for i in range(1, number + 1):
            if i % 2 == 0:
                numList.append(i)
        return jsonify({'SUCCESS': numList}), 200
    except Exception as e:
        return jsonify({'ERROR': str(e).upper()}), 500

# route for displaying all prime numbers from 2 - N
# starting from two because prime numbers are greater than 1
@app.route('/<int:number>/prime')
def displayPrimeNums(number):
    try:
        if number < 2:
            return jsonify({'ERROR': 'NUMBER MUST BE GREATER THAN OR EQUAL TO 2'}), 400
        numList =[]
        for i in range(2, number + 1):
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                numList.append(i)              
        return jsonify({'SUCCESS': numList}), 200
    except Exception as e:
        return jsonify({'ERROR': str(e).upper()}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)