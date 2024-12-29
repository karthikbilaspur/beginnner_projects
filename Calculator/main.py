class Calculator:
    def __init__(self):
        self.history = []
        self.memory = 0

    def add(self, num1, num2):
        """Returns the sum of two numbers."""
        result = num1 + num2
        self.history.append(f"{num1} + {num2} = {result}")
        return result

    def subtract(self, num1, num2):
        """Returns the difference of two numbers."""
        result = num1 - num2
        self.history.append(f"{num1} - {num2} = {result}")
        return result

    def multiply(self, num1, num2):
        """Returns the product of two numbers."""
        result = num1 * num2
        self.history.append(f"{num1} * {num2} = {result}")
        return result

    def divide(self, num1, num2):
        """Returns the quotient of two numbers."""
        if num2 == 0:
            raise ValueError("Cannot divide by zero.")
        result = num1 / num2
        self.history.append(f"{num1} / {num2} = {result}")
        return result

    def print_history(self):
        """Displays calculation history."""
        if not self.history:
            print("No calculation history.")
        else:
            print("\nCalculation History:")
            for i, entry in enumerate(self.history, start=1):
                print(f"{i}. {entry}")

    def memory_store(self, value):
        """Stores a value in memory."""
        self.memory = value
        print(f"Memory stored: {value}")

    def memory_recall(self):
        """Recalls the stored memory value."""
        if self.memory == 0:
            print("No value stored in memory.")
        else:
            print(f"Memory recalled: {self.memory}")


def main():
    calculator = Calculator()

    while True:
        print("\nSimple Calculator Menu:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. History")
        print("6. Memory Store")
        print("7. Memory Recall")
        print("8. Quit")

        choice = input("Enter your choice (1-8): ")

        if choice in ['1', '2', '3', '4']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(f"{num1} + {num2} = {calculator.add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {calculator.subtract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {calculator.multiply(num1, num2)}")
            elif choice == '4':
                try:
                    print(f"{num1} / {num2} = {calculator.divide(num1, num2)}")
                except ValueError as e:
                    print(str(e))
        elif choice == '5':
            calculator.print_history()
        elif choice == '6':
            value = float(input("Enter value to store in memory: "))
            calculator.memory_store(value)
        elif choice == '7':
            calculator.memory_recall()
        elif choice == '8':
            print("Exiting the calculator. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")


if __name__ == "__main__":
    main()