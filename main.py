# simple calculator
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def modulo(x, y):
    return x % y

# take input from the user
x = int(input("Enter first number: "))
operator = input("Enter operator: ")
y = int(input("Enter second number: "))

result = 0
if operator == "+":
    result = add(x, y)
elif operator == "-":
    result = subtract(x, y)
elif operator == "*":
    result = multiply(x, y)
elif operator == "/":
  if y == 0:
    print("Cannot divide by zero")
    exit()
  else:
    result = divide(x, y)
elif operator == "%":
  if y == 0:
    print("Cannot divide by zero")
    exit()
  else:
    result = modulo(x, y)
else:
    print("Invalid operator")

print(x, operator, y, "=", result)
