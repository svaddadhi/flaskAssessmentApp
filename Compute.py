class ComputeNums:

    def __init__(self, number):
        self.number = number

    def showNums(self):
        numList = []
        for i in range(1, self.number + 1):
            numList.append(i)
        return numList

    def showOddNums(self):
        numList = []
        for i in range(1, self.number + 1, 2):
            numList.append(i)
        return numList

    def showEvenNums(self):
        numList = []
        for i in range(1, self.number + 1):
            if i % 2 == 0:
                numList.append(i)
        return numList

    def showPrimeNums(self):
        # list of trues to the length of inputted number
        sieve = [True] * self.number

        # this for loop only is entered for ints 9 and above
        # if int is below 9, last return statement handles output
        for i in range(3, int(self.number**0.5)+1, 2):
            # iterate from 3 to sqrt of n because if you cannot find
            # any factors less than the sqrt of n n must be prime
            if sieve[i]:
                # here we are setting all the multiples to false
                sieve[i*i::2*i] = [False]*((self.number-i*i-1)//(2*i)+1)

        # this return statement will return all primes
        return [2] + [i for i in range(3, self.number, 2) if sieve[i]]
