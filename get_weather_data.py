import requests
import os
from dotenv import load_dotenv

load_dotenv()

data_from_api=requests.get(os.getenv("WEB_URL_API"),timeout=10)

if data_from_api.status_code==200:

    dict_dat=data_from_api.json()
    
    # this 6 lines of code will print the keys and this valus one by one form both location and current 
    # print(dict_dat["current"].keys())

    # for key,value in dict_dat["location"].items():
    #     print(key,":",value) 

    # print()

    # for key,value in dict_dat["current"].items():
    #     print(key,":",value)    

    print(f"Location : {dict_dat['location']['name']}")
    print(f"Temperature : {dict_dat['current']['temp_c']}°C")
    print(f"Humidity : {dict_dat['current']['humidity']}%")
    print(f"Wind Speed : {dict_dat['current']['wind_kph']} km/h")
    print(f"Cloud coverage : {dict_dat['current']['cloud']} %")


else:
    if data_from_api.status_code==400:
        print("bad request")
    elif data_from_api.status_code==401:
        print("Unatharised")
    elif data_from_api.status_code==403:
        print("Forbidden")
    elif data_from_api.status_code==404:
        print("Resorce not found")
    elif data_from_api.status_code==429:
        print("too many request try againe after some time")
    elif data_from_api.status_code==500:
        print("Server error")
    else:
        print(f"unexpected error {data_from_api.status_code}")