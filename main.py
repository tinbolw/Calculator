FirstNumber = 0
SecondNumber = 0
operation = "??"
Answer = 0


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
    elif operation == str("power") or operation == str("Power")
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
else:
    print("invalid operation (type it as a word)(power, sqrt)")
    askOperation()
