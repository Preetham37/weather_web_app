import requests
import os
from dotenv import load_dotenv

load_dotenv()

def display_weather(weather_data):
    for key,value in weather_data.items():
        print(f"{key}:{value}")

def process_weather_data(data_from_api):
    if data_from_api.status_code==200:

        dict_dat=data_from_api.json()
        needed_weather_data={"Location":dict_dat['location']['name'],
                            "Temperature":f"{dict_dat['current']['temp_c']}°C",
                            "Humidity":f"{dict_dat['current']['humidity']}%",
                            "Wind Speed":f"{dict_dat['current']['wind_kph']}km/h",
                            "Cloud Coverage":f"{dict_dat['current']['cloud']}%"
                            }
        return needed_weather_data

def gets_weather_data():
    try:
        data_from_api=requests.get(os.getenv("WEB_URL_API"),timeout=10)
        data_from_api.raise_for_status()
        return data_from_api
    except requests.exceptions.ConnectionError:
        print("Connection error")
    except requests.exceptions.Timeout:
        print("Connection time out")
    except requests.exceptions.RequestException as e:
        print(f"Request failed : {e}")
    return

def main():
    weather_api_data=gets_weather_data()
    if weather_api_data is None:
        return
    refined_data=process_weather_data(weather_api_data)
    display_weather(refined_data)

main()