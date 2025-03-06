operator = input("Enter your operator (+ ,- ,* ,/) ")

Number1 = int(input("Enter the first number :"))
Number2 = int(input("Enter the Second number: "))

if operator == "+":
    Result = Number1 + Number2
    print (f"The Answer is {Result}")
elif operator == "-":
    Result = Number1 - Number2
    print (f"The Answer is {Result}")
elif operator == "*":
    Result = Number1 * Number2
    print (f"The Answer is {Result}")
elif operator == "/":
    Result = Number1 / Number2
    print (f"The Answer is {Result}")
else:
    print("You entered wrong operator")