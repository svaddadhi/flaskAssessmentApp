# flaskAssessmentApp
This small web app has few operations that it does. When inputted a number, it will display all the number from 1 to the inputted number, 
all the evens from 1 to the inputted number, all the odds from 1 to the inputted number, or all the primes from 2 to the inputted numbers.

Testing of these routes was done on Postman, hitting the endpoints as follows:

Numbers from 1-N:
http://localhost:8080/10

Odd number from 1-N:
http://localhost:8080/10/odd

Even numbers from 1-N:
http://localhost:8080/10/even

Prime numbers from 1-N:
http://localhost:8080/10/prime

There is a docker file provided in this repository, after  cloning you can run these commands in the directory:

To build:
docker build -t <giveNameToContainer> .

To run:
docker run -p <portNumber>:8080 --name="giveOtherName" <giveNameToContainer>

To stop:
docker stop "giveOtherName"
docker rm "giveOtherName"


