expression=input("Expression: ")

if expression.find("+")>=0:
    print(int(expression[0])+int(expression[2]))
elif expression.find("-")>=0:
    print(int(expression[0])-int(expression[2]))
elif expression.find("*")>=0:
    print(int(expression[0])*int(expression[2]))
elif expression.find("/")>=0:
    print(int(expression[0])/int(expression[2]))