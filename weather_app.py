from tkinter import *
import requests
import json

root = Tk()


def fetch_air_quality_data(city_name):
    try:
        api_request = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=3dfcc909c2c2b17e8b89cd74f4468b64')
        api = json.loads(api_request.content)  # Convert JSON data into Python object
        
        city = api['name']
        wind = api['wind']['speed'] * 3.6  # Convert m/s to km/h
        weather = api['weather'][0]['main']
        des = api['weather'][0]['description']
        feel = round(api['main']['feels_like'] - 273.15, 2)  # Convert K to °C
        temp = round(api['main']['temp'] - 273.15, 2)  # Convert K to °C
        
        api_data = (f'City: {city}\n'
                    f'Wind Speed: {wind:.2f} km/h\n'
                    f'Weather: {weather}\n'
                    f'Description: {des}\n'
                    f'Temperature: {temp} °C\n'
                    f'Feels Like: {feel} °C')
    except Exception as e:
        api_data = "Give a valid city name!"
    
    t_lab.config(text=api_data)

def get_city_name():
    city = txt.get("1.0", END).strip()
    fetch_air_quality_data(city)

# Create the main frame
frame = LabelFrame(root, text='Enter the city name 🌆', font=("Segoe UI Emoji", 12))
frame.grid(row=0, column=0, padx=10, pady=10)

# Create a Text widget inside the LabelFrame
txt = Text(frame, width=20, height=1, font=("Segoe UI Emoji", 12))
txt.grid(row=0, column=1, padx=10, pady=10)

# Create buttons
btn = Button(frame, text='Submit', padx=5, pady=4, font=("Segoe UI Emoji", 8), command=get_city_name)
btn.grid(row=1, column=1)

back = Button(frame, text='Back', padx=5, pady=6, font=("Segoe UI Emoji", 8), command=root.quit)
back.grid(row=2, column=1)

# Create an update frame and label
t_frame = LabelFrame(root, text='This is the Update.')
t_frame.grid(row=1, column=0, padx=10, pady=10)

t_lab = Label(t_frame, text='', font=("Segoe UI Emoji", 10))
t_lab.grid(row=0, column=0, padx=10, pady=10)

root.mainloop()
