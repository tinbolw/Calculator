import random
import re
FirstNumber = 0
SecondNumber = 0
operation = "??"
Answer = 0
SqrtAns = 0
SqrtNumber = 0
RandomNumber = 0
maxnum = 0
useAgainput = None
def useAgain():
    global useAgainput
    global operation
    useAgainput = input("Do you want to try again? (Y/N)\n")
    if useAgainput == "Y":
        operation = 3.14159
        askOperation()
    elif useAgainput == "N":
        print("Okay. Goodbye!")
        quit()
    else:
        print("Invalid Selection")
        useAgain()

def getRandomNumber():
    global RandomNumber
    global maxnum
    maxnum = int(input("What is the limit to the random number? "))
    RandomNumber = random.randint(1, maxnum)
    print("The random number is: " + str(RandomNumber))
    useAgain()


def askSqrtNumber():
    global SqrtNumber
    global SqrtAns
    SqrtNumber = int(input("What is the number? "))
    SqrtAns = SqrtNumber ** 0.5
    print("This is the answer: " + str((SqrtAns)))
    useAgain()


def askOperation():
    global operation
    if operation == 3.14159:
        operation = input("Operation: ")
        if operation.isalpha() and operation == str("Multiply") or operation == str("multiply"):
            askFirstNumber()
        elif operation.isalpha() and operation == str("Divide") or operation == str("divide"):
            askFirstNumber()
        elif operation.isalpha() and operation == str("Add") or operation == str("add"):
            askFirstNumber()
        elif operation.isalpha() and operation == str("Subtract") or operation == str("subtract"):
            askFirstNumber()
        elif operation.isalpha() and operation == str("square root") or operation == str(
                "Square root") or operation == str(
                "square Root") or operation == str("Square Root") or operation == str("sqrt") or operation == str(
            "Sqrt") or operation == str("SQrt") or operation == str("SQRT") or operation == str(
            "sQRT") or operation == str(
            "sqRT") or operation == str("sqrT") or operation == str("SqRt") or operation == str("sQrT"):
            askSqrtNumber()
        elif operation.isalpha() and operation == str("random"):
            getRandomNumber()
        else:
            operation = float("3.14159")
            print("invalid operation)")
            print("Operations:\nAdd\nSubtract\nDivide\nMultiply\nPower\nRandom\n")
            askOperation()
    else:
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
        useAgain()
    elif operation == str("add") or operation == str("Add"):
        Answer = int(FirstNumber + SecondNumber)
        print("The answer is " + str(Answer))
        useAgain()
    elif operation == str("subtract") or operation == str("Subtract"):
        Answer = int(FirstNumber - SecondNumber)
        print("The answer is " + str(Answer))
        useAgain()
    elif operation == str("divide") or operation == str("Divide"):
        Answer = int(FirstNumber / SecondNumber)
        print("The answer is " + str(Answer))
        useAgain()
    elif operation == str("power") or operation == str("Power"):
        Answer = int(FirstNumber ** SecondNumber)
        print("The answer is " + str(Answer))
        useAgain()


print("Operations:\nAdd / Subtract\nMultiply / Divide\nSqrt /Power \nRandom\n")
askOperation()
if operation.isalpha() and operation == str("Multiply") or operation == str("multiply"):
    askFirstNumber()
elif operation.isalpha() and operation == str("Divide") or operation == str("divide"):
    askFirstNumber()
elif operation.isalpha() and operation == str("Add") or operation == str("add"):
    askFirstNumber()
elif operation.isalpha() and operation == str("Subtract") or operation == str("subtract"):
    askFirstNumber()
elif operation.isalpha() and operation == str("SQRT"):
    askSqrtNumber()
elif operation.isalpha() and operation == str("random"):
    getRandomNumber()
else:
    operation = float("3.14159")
    print("invalid operation (its case sensitive)")
    print("Operations:\nAdd\nSubtract\nDivide\nMultiply\nSQRT\nPower\nRandom\n")
    askOperation()
