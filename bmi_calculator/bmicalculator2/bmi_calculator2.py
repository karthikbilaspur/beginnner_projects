import json
import os
import matplotlib.pyplot as plt

class BMICalculator:
    def __init__(self, data_file="bmi_data.json"):
        self.bmi_categories = {
            "Underweight": (0, 18.5),
            "Normal": (18.5, 25),
            "Overweight": (25, 30),
            "Obese": (30, float("inf")),
        }
        self.health_risks = {
            "Underweight": "Malnutrition risk",
            "Normal": "Low risk",
            "Overweight": "Moderate risk",
            "Obese": "High risk",
        }
        self.data_file = data_file
        self.load_data()

    def calculate_bmi(self, weight, height):
        """
        Calculate Body Mass Index.

        Args:
        weight (float): Weight in kilograms.
        height (float): Height in meters.

        Returns:
        float: Calculated BMI.
        """
        if weight <= 0 or height <= 0:
            raise ValueError("Weight and height must be positive.")
        bmi = weight / (height ** 2)
        return bmi

    def get_bmi_category(self, bmi):
        """
        Determine BMI category.

        Args:
        bmi (float): Calculated BMI.

        Returns:
        str: BMI category.
        """
        for category, (lower, upper) in self.bmi_categories.items():
            if lower <= bmi < upper:
                return category
        return "Unknown"

    def get_health_risk(self, category):
        """
        Determine health risk based on BMI category.

        Args:
        category (str): BMI category.

        Returns:
        str: Health risk.
        """
        return self.health_risks.get(category, "Unknown")

    def load_data(self):
        """
        Load stored user data.
        """
        if os.path.exists(self.data_file):
            with open(self.data_file, "r") as file:
                self.data = json.load(file)
        else:
            self.data = {}

    def save_data(self):
        """
        Save user data.
        """
        with open(self.data_file, "w") as file:
            json.dump(self.data, file, indent=4)

    def add_user_data(self, name, weight, height):
        """
        Add user data.

        Args:
        name (str): User name.
        weight (float): Weight in kilograms.
        height (float): Height in meters.
        """
        bmi = self.calculate_bmi(weight, height)
        category = self.get_bmi_category(bmi)
        health_risk = self.get_health_risk(category)
        self.data[name] = {
            "weight": weight,
            "height": height,
            "bmi": bmi,
            "category": category,
            "health_risk": health_risk,
        }
        self.save_data()

    def view_user_data(self, name):
        """
        View user data.

        Args:
        name (str): User name.
        """
        if name in self.data:
            user_data = self.data[name]
            print(f"\nUser: {name}")
            print(f"Weight: {user_data['weight']} kg")
            print(f"Height: {user_data['height']} m")
            print(f"BMI: {user_data['bmi']:.2f}")
            print(f"Category: {user_data['category']}")
            print(f"Health Risk: {user_data['health_risk']}")
        else:
            print(f"\nNo data found for user '{name}'.")

    def visualize_data(self):
        """
        Visualize user data.
        """
        categories = list(self.bmi_categories.keys())
        counts = [0] * len(categories)

        for user_data in self.data.values():
            category = user_data["category"]
            index = categories.index(category)
            counts[index] += 1

        plt.bar(categories, counts)
        plt.xlabel("BMI Category")
        plt.ylabel("Number of Users")
        plt.title("BMI Category Distribution")
        plt.show()

    def calculate_statistics(self):
        """
        Calculate statistics.
        """
        weights = [user_data["weight"] for user_data in self.data.values()]
        heights = [user_data["height"] for user_data in self.data.values()]
        bmis = [user_data["bmi"] for user_data in self.data.values()]

        print(f"\nAverage Weight: {sum(weights) / len(weights):.2f} kg")
        print(f"Average Height: {sum(heights) / len(heights):.2f} m")
        print(f"Average BMI: {sum(bmis) / len(bmis):.2f}")

    def run(self):
        print("BMI Calculator")
        print("----------------")

        while True:
            print("\nOptions:")
            print("1. Calculate BMI")
            print("2. Add user data")
            print("3. View user data")
            print("4. Visualize data")
            print("5. Calculate statistics")
            print("6. Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                weight_unit = input("Enter weight unit (kg/lb): ")
                weight = float(input(f"Enter weight in {weight_unit}: "))

                if weight_unit.lower() == "lb":
                    weight = weight * 0.453592  # Convert pounds to kilograms

                height_unit = input("Enter height unit (m/cm/in): ")
                height = float(input(f"Enter height in {height_unit}: "))

                if height_unit.lower() == "cm":
                    height = height / 100  # Convert centimeters to meters
                elif height_unit.lower() == "in":
                    height = height * 0.0254  # Convert inches to meters

                try:
                    bmi = self.calculate_bmi(weight, height)
                    category = self.get_bmi_category(bmi)
                    health_risk = self.get_health_risk(category)

                    print(f"\nYour BMI is: {bmi:.2f}")
                    print(f"Your BMI category is: {category}")
                    print(f"Your health risk is: {health_risk}")
                except ValueError as e:
                    print(f"\nError: {e}")

            elif choice == "2":
                name = input("Enter user name: ")
                weight = float(input("Enter weight in kilograms: "))
                height = float(input("Enter height in meters: "))
                self.add_user_data(name, weight, height)
                print(f"\nUser '{name}' added successfully.")

            elif choice == "3":
                name = input("Enter user name: ")
                self.view_user_data(name)

            elif choice == "4":
                self.visualize_data()

            elif choice == "5":
                self.calculate_statistics()

            elif choice == "6":
                break

            else:
                print("\nInvalid choice. Please choose again.")


if __name__ == "__main__":
    calculator = BMICalculator()
    calculator.run()