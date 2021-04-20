import requests


def get_weather(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather?units=metric"
    complete_url = base_url + "&appid=" + api_key + "&q=" + city_name

    response = requests.get(complete_url)
    x = response.json()

    if x["cod"] != "404":
        y = x["main"]
        current_temperature = y["temp"]
        current_pressure = y["pressure"]
        current_humidiy = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]
        print("\nTemperature (in celsius unit) = " +
                        str(current_temperature) + 
              "\nAtmospheric pressure (in hPa unit) = " +
                        str(current_pressure) +
              "\nHumidity (in percentage) = " +
                        str(current_humidiy) +
              "\nDescription = " +
                        str(weather_description))
      
    else:
        print(" City Not Found ")
  
