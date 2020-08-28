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
        numList = []
        for i in range(2, self.number + 1):
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                numList.append(i)
        return numList