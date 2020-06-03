import math
import random

FirstNumber = 0
SecondNumber = 0
operation = "??"
Answer = 0
SqrtAns = 0
SqrtNumber = 0
RandomNumber = 0
maxnum = 0


def getRandomNumber():
    global RandomNumber
    global maxnum
    maxnum = int(input("What is the limit to the random number? "))
    RandomNumber = random.randint(1, maxnum)
    print("The random number is: " + str(RandomNumber))


def askSqrtNumber():
    global SqrtNumber
    global SqrtAns
    SqrtNumber = int(input("What is the number? "))
    SqrtAns = math.sqrt(SqrtNumber)
    print("This is the answer: " + str((SqrtAns)))


def askOperation():
    global operation
    operation = input("Operation: ")


def askSecondNumber():
    global SecondNumber
    SecondNumber = int(input("What is the second number? "))
    operate()


def askFirstNumber():
    global FirstNumber
    FirstNumber = int(input("What is the first number? "))
    askSecondNumber()


def operate():
    global Answer
    if operation == str("multiply") or operation == str("Multiply"):
        Answer = int(FirstNumber * SecondNumber)
        print("The answer is " + str(Answer))
    elif operation == str("add") or operation == str("Add"):
        Answer = int(FirstNumber + SecondNumber)
        print("The answer is " + str(Answer))
    elif operation == str("subtract") or operation == str("Subtract"):
        Answer = int(FirstNumber - SecondNumber)
        print("The answer is " + str(Answer))
    elif operation == str("divide") or operation == str("Divide"):
        Answer = int(FirstNumber / SecondNumber)
        print("The answer is " + str(Answer))
    elif operation == str("power") or operation == str("Power"):
        Answer = int(FirstNumber ^ SecondNumber)
        print("The answer is " + str(Answer))


print("Operations: *, /, -, +, ^, √, or random number")
askOperation()
if operation.isalpha() and operation == str("Multiply") or operation == str("multiply"):
    askFirstNumber()
elif operation.isalpha() and operation == str("Divide") or operation == str("divide"):
    askFirstNumber()
elif operation.isalpha() and operation == str("Add") or operation == str("add"):
    askFirstNumber()
elif operation.isalpha() and operation == str("Subtract") or operation == str("subtract"):
    askFirstNumber()
elif operation.isalpha() and operation == str("square root") or operation == str("Square root") or operation == str(
        "square Root") or operation == str("Square Root") or operation == str("sqrt") or operation == str(
        "Sqrt") or operation == str("SQrt") or operation == str("SQRT") or operation == str("sQRT") or operation == str(
        "sqRT") or operation == str("sqrT") or operation == str("SqRt") or operation == str("sQrT"):
    askSqrtNumber()
elif operation.isalpha() and operation == str("random"):
    getRandomNumber()
else:
    print("invalid operation (type it as a word)(power, sqrt, random)")
    askOperation()
