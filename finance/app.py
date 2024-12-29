import json
import os

class PersonalFinanceManager:
    def __init__(self, file_name):
        self.file_name = file_name
        self.load_data()
        self.categories = {
            "housing": 0,
            "food": 0,
            "transportation": 0,
            "entertainment": 0
        }
        self.budget = {
            "housing": 0,
            "food": 0,
            "transportation": 0,
            "entertainment": 0
        }

    def load_data(self):
        if os.path.exists(self.file_name):
            with open(self.file_name, 'r') as file:
                data = json.load(file)
                self.income = data["income"]
                self.expenses = data["expenses"]
                self.balance = data["balance"]
                self.transaction_history = data["transaction_history"]
                self.categories = data["categories"]
                self.budget = data["budget"]
        else:
            self.income = 0
            self.expenses = 0
            self.balance = 0
            self.transaction_history = []

    def save_data(self):
        data = {
            "income": self.income,
            "expenses": self.expenses,
            "balance": self.balance,
            "transaction_history": self.transaction_history,
            "categories": self.categories,
            "budget": self.budget
        }
        with open(self.file_name, 'w') as file:
            json.dump(data, file)

    def add_income(self, amount):
        """Add income."""
        self.income += amount
        self.balance += amount
        self.transaction_history.append(f"Income: +{amount}")
        self.save_data()

    def add_expense(self, amount, category, description):
        """Add expense."""
        if amount > self.balance:
            print("Insufficient balance.")
            return
        self.expenses += amount
        self.balance -= amount
        self.categories[category] += amount
        self.transaction_history.append(f"Expense: -{amount} ({category} - {description})")
        self.save_data()

    def view_balance(self):
        """View balance."""
        print(f"Balance: {self.balance}")

    def view_transaction_history(self):
        """View transaction history."""
        for transaction in self.transaction_history:
            print(transaction)

    def delete_transaction(self, index):
        """Delete transaction."""
        if index < 1 or index > len(self.transaction_history):
            print("Invalid transaction index.")
            return
        transaction = self.transaction_history[index - 1]
        amount = float(transaction.split(":")[1].split(" ")[1])
        category = transaction.split(" ")[-1].split("-")[0]
        if transaction.startswith("Income"):
            self.income -= amount
            self.balance -= amount
        else:
            self.expenses -= amount
            self.balance += amount
            self.categories[category] -= amount
        self.transaction_history.pop(index - 1)
        self.save_data()

    def set_budget(self, category, amount):
        """Set budget for category."""
        self.budget[category] = amount
        self.save_data()

    def view_budget(self):
        """View budget."""
        for category, amount in self.budget.items():
            usage = self.categories[category]
            print(f"{category.capitalize()}: {amount} (Usage: {usage})")


def main():
    finance_manager = PersonalFinanceManager("finance_data.json")

    while True:
        print("\nPersonal Finance Manager")
        print("1. Add income")
        print("2. Add expense")
        print("3. View balance")
        print("4. View transaction history")
        print("5. Delete transaction")
        print("6. Set budget")
        print("7. View budget")
        print("8. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            amount = float(input("Enter income amount: "))
            finance_manager.add_income(amount)
        elif choice == "2":
            amount = float(input("Enter expense amount: "))
            category = input("Enter expense category (housing/food/transportation/entertainment): ")
            description = input("Enter expense description: ")
            finance_manager.add_expense(amount, category, description)
        elif choice == "3":
            finance_manager.view_balance()
        elif choice == "4":
            finance_manager.view_transaction_history()
        elif choice == "5":
            index = int(input("Enter transaction index to delete: "))
            finance_manager.delete_transaction(index)
        elif choice == "6":
            category = input("Enter category (housing/food/transportation/entertainment): ")
            amount = float(input("Enter budget amount: "))
            finance_manager.set_budget(category, amount)
        elif choice == "7":
            finance_manager.view_budget()
        elif choice == "8":
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()