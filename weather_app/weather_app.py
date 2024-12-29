import tkinter as tk
from tkinter import ttk
import requests
import json
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from google.oauth2 import service_account
from googleapiclient.discovery import build
import pyttsx3

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.api_key = ""
        self.location = ""
        self.units = "metric"
        self.ml_model = None
        self.voice_assistant = None

        self.create_widgets()

    def create_widgets(self):
        # API key entry
        tk.Label(self.root, text="API Key:").grid(row=0, column=0)
        self.api_key_entry = tk.Entry(self.root, width=30)
        self.api_key_entry.grid(row=0, column=1)

        # Location entry
        tk.Label(self.root, text="Location:").grid(row=1, column=0)
        self.location_entry = tk.Entry(self.root, width=30)
        self.location_entry.grid(row=1, column=1)

        # Unit selection
        tk.Label(self.root, text="Units:").grid(row=2, column=0)
        self.unit_var = tk.StringVar()
        self.unit_var.set("metric")
        unit_options = ["metric", "imperial"]
        unit_menu = ttk.OptionMenu(self.root, self.unit_var, *unit_options)
        unit_menu.grid(row=2, column=1)

        # Weather buttons
        tk.Button(self.root, text="Current Weather", command=self.get_current_weather).grid(row=3, column=0)
        tk.Button(self.root, text="30-Day Forecast", command=self.get_forecast).grid(row=3, column=1)
        tk.Button(self.root, text="Voice Assistant", command=self.activate_voice_assistant).grid(row=4, column=0)

        # Weather display text area
        self.weather_text = tk.Text(self.root, width=40, height=10)
        self.weather_text.grid(row=5, column=0, columnspan=2)

        # Machine learning model training
        self.train_ml_model()

        # Voice assistant initialization
        self.initialize_voice_assistant()

    def train_ml_model(self):
        # Load historical weather data
        data = pd.read_csv("weather_data.csv")

        # Prepare data for training
        X = data.drop(["temperature"], axis=1)
        y = data["temperature"]

        # Split data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Train random forest regressor model
        self.ml_model = RandomForestRegressor()
        self.ml_model.fit(X_train, y_train)

        # Evaluate model performance
        y_pred = self.ml_model.predict(X_test)
        print(f"Model MSE: {mean_squared_error(y_test, y_pred)}")

    def initialize_voice_assistant(self):
        # Initialize Google Assistant SDK
        credentials = service_account.Credentials.from_service_account_file(
            "path_to_service_account_key.json"
        )
        self.voice_assistant = build("assistant", "v1", credentials=credentials)

        # Initialize text-to-speech engine
        self.tts_engine = pyttsx3.init()

    def activate_voice_assistant(self):
        # Activate voice assistant and listen for commands
        self.voice_assistant.start_conversation()
        command = self.voice_assistant.get_response()

        # Process voice command
        if command == "what's the weather":
            self.get_current_weather()
        elif command == "forecast":
            self.get_forecast()

    def get_current_weather(self):
        # Fetch current weather data
        self.api_key = self.api_key_entry.get()
        self.location = self.location_entry.get()
        self.units = self.unit_var.get()

        weather_data = self.fetch_weather_data()
        self.display_weather(weather_data)

        # Provide personalized weather recommendations using ML model
        recommendations = self.ml_model.predict(pd.DataFrame([weather_data]))
        self.weather_text.insert(tk.END, f"\nRecommendations: {recommendations}")

    def get_forecast(self):
        # Fetch forecast data
        self.api_key = self.api_key_entry.get()
        self.location = self.location_entry.get()
        self.units = self.unit_var.get()

        forecast_data = self.fetch_forecast_data()
        self.display_forecast(forecast_data)

        # Provide personalized forecast recommendations using ML model
        recommendations = self.ml_model.predict(pd.DataFrame([forecast_data]))
        self.weather_text.insert(tk.END, f"\nRecommendations: {recommendations}")

    def fetch_weather_data(self):
        base_url = f"http://api.openweathermap.org/data/2.5/weather?q={self.location}&appid={self.api_key}&units={self.units}"
        response = requests.get(base_url)
        return response.json()

    def fetch_forecast_data(self):
        base_url = f"http://api.openweathermap.org/data/2.5/forecast?q={self.location}&appid={self.api_key}&units={self.units}"
        response = requests.get(base_url)
        return response.json()

    def display_weather(self, weather_data):
        city = weather_data['name']
        weather = weather_data['weather'][0]['description']
        temperature = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        wind_speed = weather_data['wind']['speed']

        self.weather_text.delete(1.0, tk.END)
        self.weather_text.insert(tk.END, f"Weather in {city}:\n")
        self.weather_text.insert(tk.END, f"Description: {weather}\n")
        self.weather_text.insert(tk.END, f"Temperature: {temperature}°{self.units}\n")
        self.weather_text.insert(tk.END, f"Humidity: {humidity}%\n")
        self.weather_text.insert(tk.END, f"Wind Speed: {wind_speed} m/s\n")

    def display_forecast(self, forecast_data):
        city = forecast_data['city']['name']
        self.weather_text.delete(1.0, tk.END)
        self.weather_text.insert(tk.END, f"Weather Forecast for {city}:\n")
        for i, forecast in enumerate(forecast_data['list']):
            date = forecast['dt_txt']
            weather = forecast['weather'][0]['description']
            temperature = forecast['main']['temp']
            humidity = forecast['main']['humidity']
            wind_speed = forecast['wind']['speed']

            self.weather_text.insert(tk.END, f"\nDay {i+1} ({date}):")
            self.weather_text.insert(tk.END, f"\nDescription: {weather}")
            self.weather_text.insert(tk.END, f"\nTemperature: {temperature}°{self.units}")
            self.weather_text.insert(tk.END, f"\nHumidity: {humidity}%")
            self.weather_text.insert(tk.END, f"\nWind Speed: {wind_speed} m/s\n")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Weather App")
    app = WeatherApp(root)
    root.mainloop()