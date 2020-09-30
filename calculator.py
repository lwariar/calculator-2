"""CLI application for a prefix-notation calculator."""

# some code is from calculator-1 exercise

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

while True:
    user_input = input('Enter your equation > ')
    tokens = user_input.split(' ')

    if 'q' in tokens:
        print('You will exit.')
        break

    operator = tokens[0]
    num1 = tokens[1]

    if len(tokens) == 3:
        num2 = tokens[2]

    if len(tokens) > 3:
        print("Too many parameters.")
        break

    # Initial result is set to 0
    result = 0

    # Assigning action for each operator

    if operator == '+':
        result = add(float(num1), float(num2))

    elif operator == '-':
        result = subtract(float(num1), float(num2))

    elif operator == '*':
        result = multiply(float(num1), float(num2))

    elif operator == '/':
        result = divide(float(num1), float(num2))

    elif operator == 'square':
        result = square(float(num1))

    elif operator == 'cube':
        result = cube(float(num1))

    elif operator == 'pow':
        result = power(float(num1), float(num2))

    elif operator == 'mod':
        result = mod(float(num1), float(num2))

    else:
        print("Invalid requests.")
    print(result)
