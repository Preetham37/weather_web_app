import requests
import os
from dotenv import load_dotenv

load_dotenv()

def display_weather(weather_data):
    for key,value in weather_data.items():
        print(f"{key}:{value}")

def process_weather_data(data_from_api):
    # if data_from_api.status_code==200:

    dict_dat=data_from_api
    needed_weather_data={"Location":dict_dat['location']['name'],
                        "Temperature":f"{dict_dat['current']['temp_c']}°C",
                        "Humidity":f"{dict_dat['current']['humidity']}%",
                        "Wind Speed":f"{dict_dat['current']['wind_kph']}km/h",
                        "Cloud Coverage":f"{dict_dat['current']['cloud']}%"
                        }
    return needed_weather_data

def api_error_check(location_id,search_location):
    try:
        if location_id:
            data_from_api=requests.get(os.getenv("WEB_URL"),params={"key":os.getenv("API"),"q":f"id:{location_id}"},timeout=10)
            data_from_api.raise_for_status()
            print()
            return data_from_api.json()
        else:
            # checks the api status and gets the search location information
            request=requests.get(os.getenv("WEB_URL_SEARCH"),params={"key":os.getenv("API"),"q":search_location})
            request.raise_for_status()

            # returns the complete location list 

            return request.json()
    except requests.exceptions.ConnectionError:
        print("Connection error")
    except requests.exceptions.Timeout:
        print("Connection time out")
    except requests.exceptions.RequestException as e:
        print(f"Request failed : {e}")
    return

def get_location_list(request_json):
    # prints out the list of the city 
    for inedex,data in enumerate(request_json,start=1):
        print(f"{inedex} . {data['name']}\n    {data['region']}\n    {data['country']}\n")
    return request_json

def print_and_ask_location(request_json):
    # asks the user to select a location from the returened list 
    search_name_index=int(input("enter the no of location : "))
    
    # gets the location index from the list 
    selected_location=request_json[search_name_index-1]
    
    # prints out the locatin name region and country 
    print(f"\n{selected_location['name']}\n{selected_location['region']}\n{selected_location['country']}\n")
    
    # returns the id of the selected location form the list
    return selected_location['id']




def main():
    user_search_name=input("enter the city you want : ")
    city_list=api_error_check(0,user_search_name)
    get_location_list(city_list)
    index_of_selected_location=int(input("enter the city index to get the weather : "))
    city_weather_info=api_error_check(city_list[index_of_selected_location-1]["id"],0)
    refined_weather_data=process_weather_data(data_from_api=city_weather_info)
    display_weather(refined_weather_data)
if __name__=="__main__":
    main()