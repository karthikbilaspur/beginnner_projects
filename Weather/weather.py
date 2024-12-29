import requests
import json
import matplotlib.pyplot as plt

def get_weather(location, api_key, units):
    """
    Fetch weather data from OpenWeatherMap API.

    Args:
        location (str): City name, zip code or coordinates (lat,lon).
        api_key (str): OpenWeatherMap API key.
        units (str): Temperature units (metric, imperial or standard).

    Returns:
        dict: Weather data.
    """
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units={units}"
    response = requests.get(base_url)
    return response.json()


def get_forecast(location, api_key, units):
    """
    Fetch 30-day weather forecast from OpenWeatherMap API.

    Args:
        location (str): City name, zip code or coordinates (lat,lon).
        api_key (str): OpenWeatherMap API key.
        units (str): Temperature units (metric, imperial or standard).

    Returns:
        dict: 30-day weather forecast.
    """
    base_url = f"http://api.openweathermap.org/data/2.5/forecast?q={location}&appid={api_key}&units={units}"
    response = requests.get(base_url)
    return response.json()


def get_air_quality(location, api_key):
    """
    Fetch air quality data from OpenWeatherMap API.

    Args:
        location (str): City name, zip code or coordinates (lat,lon).
        api_key (str): OpenWeatherMap API key.

    Returns:
        dict: Air quality data.
    """
    base_url = f"http://api.openweathermap.org/data/2.5/air_pollution?q={location}&appid={api_key}"
    response = requests.get(base_url)
    return response.json()


def display_weather(weather_data):
    """
    Display weather information.

    Args:
        weather_data (dict): Weather data.
    """
    city = weather_data["name"]
    temperature = weather_data["main"]["temp"]
    feels_like = weather_data["main"]["feels_like"]
    humidity = weather_data["main"]["humidity"]
    pressure = weather_data["main"]["pressure"]
    wind_speed = weather_data["wind"]["speed"]
    weather = weather_data["weather"][0]["description"]

    print(f"Weather in {city}:")
    print(f"Temperature: {temperature}°C (Feels like: {feels_like}°C)")
    print(f"Humidity: {humidity}%")
    print(f"Pressure: {pressure} hPa")
    print(f"Wind Speed: {wind_speed} m/s")
    print(f"Weather: {weather}")


def display_forecast(forecast_data):
    """
    Display 30-day weather forecast.

    Args:
        forecast_data (dict): 30-day weather forecast.
    """
    city = forecast_data["city"]["name"]
    print(f"\n30-Day Forecast for {city}:")
    for i, forecast in enumerate(forecast_data["list"]):
        date = forecast["dt_txt"]
        temperature = forecast["main"]["temp"]
        weather = forecast["weather"][0]["description"]
        print(f"\nDay {i+1} ({date}):")
        print(f"Temperature: {temperature}°C")
        print(f"Weather: {weather}")


def display_air_quality(air_quality_data):
    """
    Display air quality information.

    Args:
        air_quality_data (dict): Air quality data.
    """
    aqi = air_quality_data["list"][0]["main"]["aqi"]
    print(f"\nAir Quality Index: {aqi}")


def display_graphs(forecast_data):
    """
    Display temperature, humidity and wind speed graphs.

    Args:
        forecast_data (dict): 30-day weather forecast.
    """
    temperatures = [forecast["main"]["temp"] for forecast in forecast_data["list"]]
    humidities = [forecast["main"]["humidity"] for forecast in forecast_data["list"]]
    wind_speeds = [forecast["wind"]["speed"] for forecast in forecast_data["list"]]

    plt.figure(figsize=(15, 5))

    plt.subplot(1, 3, 1)
    plt.plot(temperatures)
    plt.title("Temperature")
    plt.xlabel("Time")
    plt.ylabel("°C")

    plt.subplot(1, 3, 2)
    plt.plot(humidities)
    plt.title("Humidity")
    plt.xlabel("Time")
    plt.ylabel("%")

    plt.subplot(1, 3, 3)
    plt.plot(wind_speeds)
    plt.title("Wind Speed")
    plt.xlabel("Time")
    plt.ylabel("m/s")

    plt.tight_layout()
    plt.show()


def main():
    api_key = "YOUR_API_KEY"  # Replace with your API key.

    while True:
        print("\nLocation Search:")
        print("1. City Name")
        print("2. Zip Code")
        print("3. Geographic Coordinates")
        choice = input("Choose location type (1/2/3): ")

        if choice == "1":
            location = input("Enter city name: ")
        elif choice == "2":
            location = input("Enter zip code: ")
        elif choice == "3":
            lat = input("Enter latitude: ")
            lon = input("Enter longitude: ")
            location = f"{lat},{lon}"
        else:
            print("Invalid choice. Please choose again.")
            continue

        while True:
            print("\nTemperature Units:")
            print("1. Celsius")
            print("2. Fahrenheit")
            print("3. Kelvin")
            unit_choice = input("Choose unit (1/2/3): ")

            if unit_choice in ["1", "2", "3"]:
                units = "metric" if unit_choice == "1" else "imperial" if unit_choice == "2" else "standard"
                break
            else:
                print("Invalid choice. Please choose again.")

        try:
            weather_data = get_weather(location, api_key, units)
            display_weather(weather_data)

            forecast_choice = input("\nShow 30-day forecast? (y/n): ")
            if forecast_choice.lower() == "y":
                forecast_data = get_forecast(location, api_key, units)
                display_forecast(forecast_data)

                air_quality_choice = input("\nShow air quality? (y/n): ")
                if air_quality_choice.lower() == "y":
                    air_quality_data = get_air_quality(location, api_key)
                    display_air_quality(air_quality_data)

                graph_choice = input("\nShow temperature, humidity and wind speed graphs? (y/n): ")
                if graph_choice.lower() == "y":
                    display_graphs(forecast_data)

        except requests.exceptions.RequestException as e:
            print(f"Error fetching weather data: {e}")
        except KeyError:
            print("Invalid location. Please try again.")

        repeat_choice = input("\nSearch again? (y/n): ")
        if repeat_choice.lower() != "y":
            break


if __name__ == "__main__":
    main()