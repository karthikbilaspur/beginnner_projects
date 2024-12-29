import math

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        raise ValueError("Cannot divide by zero.")
    return num1 / num2

def modulus(num1, num2):
    if num2 == 0:
        raise ValueError("Cannot divide by zero.")
    return num1 % num2

def exponent(num1, num2):
    return num1 ** num2

def sqrt(num):
    if num < 0:
        raise ValueError("Cannot compute square root of negative number.")
    return math.sqrt(num)

def cbrt(num):
    return round(num ** (1. / 3), 3)

def factorial(num):
    if num < 0:
        raise ValueError("Factorial not defined for negative numbers.")
    return math.factorial(num)

def main():
    while True:
        print("\nCommand-Line Calculator Menu:")
        print("1. Basic Operations")
        print("2. Exit")

        choice = input("Choose option (1-2): ")

        if choice == "1":
            print("\nBasic Operations:")
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
            print("5. Modulus")
            print("6. Exponentiation")
            print("7. Square Root")
            print("8. Cube Root")
            print("9. Factorial")

            operation = input("Choose operation (1-9): ")

            if operation in ("1", "2", "3", "4", "5", "6"):
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if operation == "1":
                    result = add(num1, num2)
                elif operation == "2":
                    result = subtract(num1, num2)
                elif operation == "3":
                    result = multiply(num1, num2)
                elif operation == "4":
                    try:
                        result = divide(num1, num2)
                    except ValueError as e:
                        print(str(e))
                        continue
                elif operation == "5":
                    try:
                        result = modulus(num1, num2)
                    except ValueError as e:
                        print(str(e))
                        continue
                elif operation == "6":
                    result = exponent(num1, num2)

                print(f"Result: {result}")

            elif operation == "7":
                num = float(input("Enter number: "))
                try:
                    result = sqrt(num)
                    print(f"Square Root: {result}")
                except ValueError as e:
                    print(str(e))

            elif operation == "8":
                num = float(input("Enter number: "))
                result = cbrt(num)
                print(f"Cube Root: {result}")

            elif operation == "9":
                num = int(input("Enter positive integer: "))
                try:
                    result = factorial(num)
                    print(f"Factorial: {result}")
                except ValueError as e:
                    print(str(e))

        elif choice == "2":
            print("Exiting calculator.")
            break

        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()