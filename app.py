from flask import Flask
app = Flask(__name__)


# route for displaying numbers from 1-N
# error handling needs to be done
@app.route('/<int:number>')
def displayNums(number):
    numList = []
    for i in range(1, number + 1):
        numList.append(i)
    return str(numList)

# route for displaying odd numbers from 1-N
# error handling needs to be done
# different approach will also be provided
@app.route('/<int:number>/odd')
def displayOddNums(number):
    numList =[]
    for i in range(1, number + 1, 2):
        numList.append(i)
    return str(numList)

# route for displaying even numbers from 1-N
# error handling will be added
@app.route('/<int:number>/even')
def displayEvenNums(number):
    numList =[]
    for i in range(1, number + 1):
        if i % 2 == 0:
            numList.append(i)
    return str(numList)

# route for displaying all prime numbers from 2 - N
# starting from two because prime numbers are greater than 1
@app.route('/<int:number>/prime')
def displayPrimeNums(number):
    numList =[]
    for i in range(2, number + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            numList.append(i)
                
    return str(numList)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)