# -*- coding: utf-8 -*-

#importing required modules for program
import requests
import customtkinter #variation of tkinter, a native gui interface in python, allowed for theme changes
from customtkinter import CTkLabel, CTkFrame, CTkEntry #These load the GUI interface variation and windows


API_KEY = "8ef2a370d4894f998e6220006231204"   #This is the Weather API key. This api key allows data requested to be the pre selected paramaters i gave in the API response fields. 


def get_weather_data( zip_code=None):
    if zip_code:
        # Make API request using zip code
        url = f"http://api.weatherapi.com/v1/forecast.json?key=8ef2a370d4894f998e6220006231204&q={zip_code}&days=1"
 #  elif state:
        # Make API request using state name
     #  url = f"http://api.weatherapi.com/v1/forecast.json?key=8ef2a370d4894f998e6220006231204&q={state}&days=1"
    else:
        
        # Neither state nor zip code provided
        return None
    
    response = requests.get(url)
    if response.ok:
        data = response.json()
        current = data['current']
        forecast = data['forecast']['forecastday'][0]['day']

        # Extract desired information from JSON response. This defines all the different parameters I requiested and assigns them for the text in line 45 
        city = data['location']['name']
        region = data['location']['region']
        country = data['location']['country']
        temperature = current['temp_f']
        wind_speed = current['wind_mph']
        uv_index = current['uv']
        prob_rain = forecast['daily_chance_of_rain']
        total_precip = forecast['totalprecip_in']

        # Display weather data in a label
        weather_label = CTkLabel(frame, text=f"City: {city}\nRegion: {region}\nCountry: {country}\nTemperature (F): {temperature}\nWind Speed (mph): {wind_speed}\nUV Index: {uv_index}\nProbability of Rain Today: {prob_rain}%\nTotal Precipitation (in)(24 hours): {total_precip}")
        weather_label.pack(pady=12, padx=10)
    else:
        # Display error message if no weather data is returned or zip code is not valid
        error_label = CTkLabel(frame, text="Error: Please Ensure the input is a valid United States 5 digit Zip code")
        error_label.pack(pady=12, padx=10)


def login():#this is executed once the user has hit the button to get weather for their inputted location. This takes the raw json response and parses it to make it cleaner for output and allows the variables assigned above to use those values when called. 
    zip_code = entry2.get()
    weather_data = get_weather_data(zip_code=zip_code)
    if weather_data:
        # Extract desired information from JSON response
        city = weather_data['location']['name']
        region = weather_data['location']['region']
        country = weather_data['location']['country']
        temperature = weather_data['current']['temp_f']
        wind_speed = weather_data['current']['wind_mph']
        precip_prob = weather_data['current']['precip_prob']
        total_precip = weather_data['current']['precip_in']
        uv_index = weather_data['current']['uv']

        # Display weather data in a label
        weather_label = CTkLabel(frame, text=f"City: {city}\nRegion: {region}\nCountry: {country}\nTemperature (F): {temperature}\nWind Speed (mph): {wind_speed}\nProbability of Precipitation: {precip_prob}%\nTotal Precipitation (in): {total_precip}\nUV Index: {uv_index}")
        weather_label.pack(pady=12, padx=10)
    else:
        # Display error message if no weather data is returned
        error_label = CTkLabel(frame, text=weather_data)
        error_label.pack(pady=12, padx=10)
#state_label = CTkLabel(frame, text="Select a state:")# this code is commented out based on changes to proposed outline and to improve functionality of the program. 
#state_label.pack()

#state_var = customtkinter.StringVar()
#state_dropdown = CTkComboBox(frame, variable=s ate_var, values=["london", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia"])
#state_dropdown.pack()


customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()#this block creates a window using the loaded customttkinter module native in python and sets the title of the window when the program is ran. 
root.geometry("800x600")
root.title("Quick Weather Now")

frame = CTkFrame(master=root)#this creates a frame and is set to the root from above
frame.pack(pady=20, padx=60, fill='both' , expand=True)

zip_label = CTkLabel(frame, text="Enter ZIP Code:")#this prompts the suser to input a zip code
zip_label.pack()

zip_var = customtkinter.StringVar()#allows inserted zip code string to be assigned to zip_var an dbe usde tro call the request to api
entry2 = CTkEntry(frame, textvariable=zip_var)
entry2.pack()

button = customtkinter.CTkButton(frame, text='Get Weather Now', command=login)# this button allows users to prompt an API request to call the data based on their input location zip code. 
button.pack(pady=12, padx=10)

root.mainloop()
