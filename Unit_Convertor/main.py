import json
import os

class UnitConverter:
    def __init__(self, history_file):
        self.conversion_history = []
        self.history_file = history_file
        self.load_history()

    def length_conversion(self):
        """Converts length units."""
        print("Length Conversion")
        print("1. Kilometers to Miles")
        print("2. Miles to Kilometers")
        print("3. Meters to Feet")
        print("4. Feet to Meters")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            kilometers = float(input("Enter distance in kilometers: "))
            miles = kilometers * 0.621371
            print(f"{kilometers} kilometers = {miles} miles")

        elif choice == '2':
            miles = float(input("Enter distance in miles: "))
            kilometers = miles * 1.60934
            print(f"{miles} miles = {kilometers} kilometers")

        elif choice == '3':
            meters = float(input("Enter distance in meters: "))
            feet = meters * 3.28084
            print(f"{meters} meters = {feet} feet")

        elif choice == '4':
            feet = float(input("Enter distance in feet: "))
            meters = feet * 0.3048
            print(f"{feet} feet = {meters} meters")

        else:
            print("Invalid choice")

    def weight_conversion(self):
        """Converts weight units."""
        print("Weight Conversion")
        print("1. Kilograms to Pounds")
        print("2. Pounds to Kilograms")
        print("3. Grams to Ounces")
        print("4. Ounces to Grams")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            kilograms = float(input("Enter weight in kilograms: "))
            pounds = kilograms * 2.20462
            print(f"{kilograms} kilograms = {pounds} pounds")

        elif choice == '2':
            pounds = float(input("Enter weight in pounds: "))
            kilograms = pounds * 0.453592
            print(f"{pounds} pounds = {kilograms} kilograms")

        elif choice == '3':
            grams = float(input("Enter weight in grams: "))
            ounces = grams * 0.035274
            print(f"{grams} grams = {ounces} ounces")

        elif choice == '4':
            ounces = float(input("Enter weight in ounces: "))
            grams = ounces * 28.3495
            print(f"{ounces} ounces = {grams} grams")

        else:
            print("Invalid choice")

    def store_conversion(self, from_unit, value, to_unit, result):
        """Stores conversion history."""
        history_entry = f"{value} {from_unit} = {result} {to_unit}"
        self.conversion_history.append(history_entry)

    def display_history(self):
        """Displays conversion history."""
        if not self.conversion_history:
            print("No conversion history.")
        else:
            print("Conversion History:")
            for i, entry in enumerate(self.conversion_history, start=1):
                print(f"{i}. {entry}")

    def save_history(self):
        """Saves conversion history to file."""
        with open(self.history_file, 'w') as file:
            json.dump(self.conversion_history, file)

    def load_history(self):
        """Loads conversion history from file."""
        if os.path.exists(self.history_file):
            with open(self.history_file, 'r') as file:
                self.conversion_history = json.load(file)

    def temperature_conversion(self):
        """Converts temperature units."""
        print("Temperature Conversion")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")

        choice = input("Enter your choice (1/2): ")

        if choice == '1':
            celsius = float(input("Enter temperature in celsius: "))
            fahrenheit = (celsius * 9/5) + 32
            print(f"{celsius}°C = {fahrenheit}°F")

        elif choice == '2':
            fahrenheit = float(input("Enter temperature in fahrenheit: "))
            celsius = (fahrenheit - 32) * 5/9
            print(f"{fahrenheit}°F = {celsius}°C")

        else:
            print("Invalid choice")


def main():
    converter = UnitConverter()

    while True:
        print("\nUnit Converter")
        print("1. Length Conversion")
        print("2. Weight Conversion")
        print("3. Temperature Conversion")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            converter.length_conversion()
        elif choice == '2':
            converter.weight_conversion()
        elif choice == '3':
            converter.temperature_conversion()
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()