# Math Interpreter



# Asks for expression and splits it into three variables
expression = input("Expression: ")
x, y, z = expression.split()

# Ensures x and z are integers
x = int(x)
z = int(z)

# Conditionals
if y == "+":
    math = (x + z)
elif y == "-":
    math = (x - z)
elif y == "*":
    math = (x * z)
elif y == "/":
    math = (x / z)

# Converts math to a float rounded to one decimal and prints result
math = float(math)
result = round(math, 1)
print(result)