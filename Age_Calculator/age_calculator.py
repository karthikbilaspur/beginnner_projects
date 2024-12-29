from datetime import date, timedelta

def calculate_age(birth_date, calculation_date=None):
    """
    Calculate age from birth date.

    Args:
        birth_date (date): Birth date.
        calculation_date (date, optional): Date for age calculation. Defaults to today.

    Returns:
        dict: Age in years, months and days.
    """
    if calculation_date is None:
        calculation_date = date.today()

    years = calculation_date.year - birth_date.year
    months = calculation_date.month - birth_date.month
    days = calculation_date.day - birth_date.day

    if months < 0:
        years -= 1
        months += 12
    if days < 0:
        months -= 1
        days_in_month = (date(calculation_date.year, calculation_date.month, 1) -
                         date(calculation_date.year, calculation_date.month - 1, 1)).days
        days += days_in_month

    return {
        "years": years,
        "months": months,
        "days": days
    }

def validate_date(date_string):
    """
    Validate date string.

    Args:
        date_string (str): Date string in DD/MM/YYYY format.

    Returns:
        date: Validated date object or None.
    """
    try:
        day, month, year = map(int, date_string.split('/'))
        return date(year, month, day)
    except ValueError:
        return None

def get_upcoming_birthday(birth_date):
    """
    Get upcoming birthday.

    Args:
        birth_date (date): Birth date.

    Returns:
        date: Upcoming birthday.
    """
    today = date.today()
    upcoming_birthday = date(today.year, birth_date.month, birth_date.day)
    if upcoming_birthday < today:
        upcoming_birthday = date(today.year + 1, birth_date.month, birth_date.day)
    return upcoming_birthday

def time_to_upcoming_birthday(birth_date):
    """
    Calculate time to upcoming birthday.

    Args:
        birth_date (date): Birth date.

    Returns:
        dict: Time to upcoming birthday in days, hours, minutes and seconds.
    """
    upcoming_birthday = get_upcoming_birthday(birth_date)
    time_to_birthday = upcoming_birthday - date.today()
    days = time_to_birthday.days
    hours, remainder = divmod(time_to_birthday.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return {
        "days": days,
        "hours": hours,
        "minutes": minutes,
        "seconds": seconds
    }

def zodiac_sign(birth_date):
    """
    Determine zodiac sign.

    Args:
        birth_date (date): Birth date.

    Returns:
        str: Zodiac sign.
    """
    zodiac_dict = {
        (1, 20): "Aquarius", (2, 19): "Pisces", (3, 21): "Aries", (4, 20): "Taurus",
        (5, 21): "Gemini", (6, 21): "Cancer", (7, 23): "Leo", (8, 23): "Virgo",
        (9, 23): "Libra", (10, 23): "Scorpio", (11, 22): "Sagittarius", (12, 22): "Capricorn"
    }
    for date_tuple, sign in zodiac_dict.items():
        if (birth_date.month == date_tuple[0] and birth_date.day >= date_tuple[1]) or \
           (birth_date.month == date_tuple[0] - 1 and birth_date.day <= date_tuple[1]):
            return sign

def main():
    while True:
        print("\nAge Calculator Menu:")
        print("1. Calculate Age")
        print("2. Time to Next Birthday")
        print("3. Zodiac Sign")
        print("4. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            birth_date_input = input("Enter birthdate (DD/MM/YYYY): ")
            birth_date = validate_date(birth_date_input)
            if birth_date is None:
                print("Invalid date format. Please use DD/MM/YYYY.")
                continue

            calculation_date_input = input("Calculate age at (DD/MM/YYYY) or press Enter for today: ")
            calculation_date = validate_date(calculation_date_input) if calculation_date_input else None

            age = calculate_age(birth_date, calculation_date)
            print(f"Age: {age['years']} years, {age['months']} months, {age['days']} days")

        elif choice == "2":
            birth_date_input = input("Enter birthdate (DD/MM/YYYY): ")
            birth_date = validate_date(birth_date_input)
            if birth_date is None:
                print("Invalid date format. Please use DD/MM/YYYY.")
                continue

            time_to_birthday = time_to_upcoming_birthday(birth_date)
            print(f"Time to next birthday: {time_to_birthday['days']} days, {time_to_birthday['hours']} hours, "
                  f"{time_to_birthday['minutes']} minutes, {time_to_birthday['seconds']} seconds")

        elif choice == "3":
            birth_date_input = input("Enter birthdate (DD/MM/YYYY): ")
            birth_date = validate_date(birth_date_input)
            if birth_date is None:
                print("Invalid date format. Please use DD/MM/YYYY.")
                continue

            zodiac = zodiac_sign(birth_date)
            print(f"Zodiac sign: {zodiac}")

        elif choice == "4":
            break

        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()