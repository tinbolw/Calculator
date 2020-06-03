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
    if operation == str("multiply"):
        Answer = int(FirstNumber * SecondNumber)
        print("The answer is " + str(Answer))


print("Operations: *, /, -, +, ^, √, or random number")
askOperation()
if operation.isalpha():
    askFirstNumber()
else:
    print("invalid operation (type it as a word)")
    askOperation()
