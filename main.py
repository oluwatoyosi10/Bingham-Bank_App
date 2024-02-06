# Import required modules
import tkinter as tk
import requests
from tkinter import messagebox
from PIL import Image, ImageTk
import ttkbootstrap


# Function to get weather information from OpenWeatherMap API
def get_weather(city):
    API_key = "30d1cf22246548cc78b54c5d020f6ba4"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}"
    res = requests.get(url)

    if res.status_code == 404:
        messagebox.showerror("Error", "city not found")
        return None

    # Parse the response JSON to get weather information
    weather = res.json()
    icon_id = ['weather'][0]['icon']
    temperature = weather['main']['temp'] - 273.15
    description = weather['weather'][0]['description']
    city = weather['name']
    country = weather['sys']['country']

    # Get the icon URL and return all the weather information
    icon_url = f"https://openweathermap.org/img/wn/{icon_id}@2x.png"
    return (icon_url, temperature, description, city, country)


# Function to search weather for a city
def search():
    city = city_entry.get()
    result = get_weather(city)
    if result is None:
        return
    # If the country is found, unpack the weather information
    icon_url, temperature, description, city, country = result
    locate_label.configure(text=f"{city}, {country}")

    # Get the weather icon image from the URL and update the icon label
    image = Image.open(requests.get(icon_url, steam=True).raw)
    icon = ImageTk.PhotoImage(image)
    icon_label.configure(image=icon)
    icon_label.image = icon

    # Update the temperature and description labels
    temperature_label.configure(text=f"Temperature: {temperature:.2f}°C")
    description_label.configure(text=f"Description: {description}")

root = ttkbootstrap.Window(themename="morph")
root.title = "Weather App"
root.geometry("400x400")

# Entry widget -> to enter the city name
city_entry = ttkbootstrap.Entry(root, font="Helvetica, 18")
city_entry.pack(pady=10)

# Button widget -> to search for the weather information
search_button = ttkbootstrap.Button(root, text="search", command=search, bootstyle="warning")
search_button.pack(pady=10)

# Label widget -> to show the city/country name
locate_label = tk.Label(root, font="Helvetica, 25")
locate_label.pack(pady=20)

# Label widget -> to show the weather icon
icon_label = tk.Label(root)
icon_label.pack()

# Label widget -> to show the temperature
temperature_label = tk.Label(root, font="Helvetica, 20")
temperature_label.pack()

# Label widget -> to show the weather description
description_label = tk.Label(root, font="Helvetica, 20")
description_label.pack()

root.mainloop()