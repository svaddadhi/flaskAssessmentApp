from flask import Flask
app = Flask(__name__)

#this route is to test connection, will be deleted
@app.route('/')
def hello():
    return "Hello World!"


#route for printing numbers from 1-N
#error handling needs to be done
@app.route('/<int:number>')
def displayNums(number):
    numList = []
    for i in range(1, number + 1):
        numList.append(i)
    return str(numList)


@app.route('/<int:number>/odd')
def displayOddNums(number):
    numList =[]
    for i in range(1, number + 1, 2):
        numList.append(i)
    return str(numList)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)