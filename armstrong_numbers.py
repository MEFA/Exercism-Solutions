def is_armstrong_number(number):
    numberAsString = str(number)
    numberLength = len(numberAsString)
    numberLength = int(numberLength)
    numberAsList = [] 
    totalSum = 0
    for i in numberAsString:
        numberAsList.append(int(i))
    for i in numberAsList:
        powerOfEachNumber = i ** numberLength
        totalSum = totalSum + powerOfEachNumber
    return totalSum == number
is_armstrong_number(153)