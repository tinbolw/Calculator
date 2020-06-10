import random
# DISCLAIMER: I AM NOT A CERTIFIED PROGRAMMER
# I HAVE LITTLE EXPERIENCE, TAKE ALL MY CLAIMS
# WITH A GRAIN OF SALT, AS THAT WILL BRING THE FLAVOR OUT
# JOKE BTW BUT PLEASE DO TAKE MY CLAIMS WITH A GRAIN OF SALT

# i import a module called "random" which can pick random numbers and stuff
# if you want to use a module in python, you type the
# module name, then the action (random.randint)
# you can also import modules as something else
# like: "import random as ran"
# or you can import a module from the module
# "from random import randint"
FirstNumber = 0
SecondNumber = 0
operation = "??"
Answer = 0
SqrtAns = 0
SqrtNumber = 0
RandomNumber = 0
maxnum = 0
useAgainput = None
# i set all variables that i use in the program to nothing
# i dont think this is necessary
# None = nothing. 0 does not = nothing
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
        
# i define a function called useAgain which triggers
# when the program is finished to restart it if you want to
# i set the variables that i want to use in the function as 
# global so they can be used anywhere
# notice the (): at the end of the function name (useAgain():)
# that is so the function doesnt include the whole program
# the (): says, whatever under the function and is indented
# is part of the function

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
    
# notice the "useAgain():" at the end of each function
# this runs useAgain
# if you want to run a function, remember the ()
# parameters would normally go there but since my function
# doesnt take any parameters, so i leave it blank.

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


# ^^ is the code that determines what operation you entered
# i use the operation = float("3.14159")
# because if someone enters an invalid operation, it will
# set operation at 3.14159 and that makes the if
# statement realize that the person entered
# the operation incorrectly so
# it would check the operation again


def askSecondNumber():
    global SecondNumber
    SecondNumber = int(input("What is the second number? "))
    operate()

# these functions get the number(s) that you want to use
# the input() function is used here
# setting a variable to contain the value recieved
# from the input() is a good idea

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

# the code that calculates the answers is ^^

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

# this code ^^ asks what operation.