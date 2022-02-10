
import tkinter as tk
import requests 
import time



def whatsTheWeatherLike(ui):
    city = tField.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=4691b8ca185f1776615f2a1f11961f1a"
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp= int(json_data['main']['temp'] )
    conversion = int((temp - 273.15 ) * 9/5 + 32)
    min_temp = int(json_data['main']['temp_min'])
    min_temp_conv = int((min_temp - 273.15 ) * 9/5 + 32)
    max_temp = int(json_data['main']['temp_max'])
    max_temp_conv = int((max_temp - 273.15 ) * 9/5 + 32)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    sunrise = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunrise'] - 21600))
    sunset = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunset'] - 21600))

    final_info = condition + "\n" + str(conversion) + "F"
    final_data = "\n" + "Max Temp: " + str(max_temp_conv) + "\n" + "Min Temp: " + str(min_temp_conv) + "\n" + "Pressure: " + str(pressure) + "\n" + "Humidity: " + str(humidity) + "\n" +"Wind Speed: " + str(wind) + "\n" + "Sunrise: " + str(sunrise) + "\n" + "Sunset: " + str(sunset)
    label1.config(text = final_info)
    label2.config(text = final_data) 
    
    
    






# Ui set up  
ui = tk.Tk()
ui.geometry("600x500")
ui.title("Weather App")
ui.configure(bg="black")
ft = ("Modern", 14)
text = ("Modern", 30)

tField = tk.Entry(ui, justify='center', width = '30', font = text)
tField.pack(pady = 20)
tField.focus()
tField.bind('<Return>', whatsTheWeatherLike)

label1 = tk.Label(ui, font = text)
label1.pack()
label2 = tk.Label(ui, font = ft)
label2.pack()
ui.mainloop()