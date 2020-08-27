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

# route for printing displaying odd numbers from 1-N
# error handling needs to be done
# different approach will also be provided
@app.route('/<int:number>/odd')
def displayOddNums(number):
    numList =[]
    for i in range(1, number + 1, 2):
        numList.append(i)
    return str(numList)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)