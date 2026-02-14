# Stage 2: Calculator with Positive/Negative/Zero check
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

if op == '+':
    result = num1 + num2
elif op == '-':
    result = num1 - num2
elif op == '*':
    result = num1 * num2
elif op == '/':
    result = num1 / num2 if num2 != 0 else None
else:
    result = None

if result is not None:
    print(f"Result = {result}")
    if result > 0:
        print("Positive")
    elif result < 0:
        print("Negative")
    else:
        print("Zero")
else:
    print("Error: Invalid operation or division by zero")
