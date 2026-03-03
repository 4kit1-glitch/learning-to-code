expression = input("Enter the expression: ")
print(expression)

for char in expression:

    operator_test = (char == '+' or char == '-' or char == '*' or char == '/')

    if(operator_test == True):
        pass
    elif(operator_test == False):
        operand1 = int(char)
        continue



