import requests
# module that allows user to send HTTP requests (HTTP request returns Response Object)

def get_weather(api_key, base_url, city):
    request_url = f"{base_url}?appid={api_key}&q={city}"
    response = requests.get(request_url) # send GET request to the url/ request data from server
    if response.status_code == 200:
        data = response.json()
        display_weather(data)
    else:
        print("Error occurred.")

def get_datetime(api_key, base_url, city):
    request_url = f"{base_url}?city={city}"
    response = requests.get(request_url, headers={"X-Api-Key": api_key}) # send GET request to the url/ request data from server
    if response.status_code == 200:
        data = response.json()
        display_datetime(data, city)
    else:
        print("Error occurred.")

def display_weather(data):
    weather = data["weather"][0]["description"]
    temperature = round(data["main"]["temp"] - 273.15, 2)
    print("Weather:", weather)
    print("Temperature:", temperature, "celcius")
    print(" ")

def display_datetime(data, city):
    datetime = data["datetime"]
    day = data["day_of_week"]
    print(" ")
    print("City:", city)
    print("Date & Time/ Day:", datetime, "/", day)

def main():
    API_KEY1 = "0e0859e9f54f8f01cb1bd1144658e628" # # APi key from OpenWeather
    API_KEY2 = "n4FilKP0NZDqYZguKKP1+Q==TePugoKqGLVK4rQJ" # APi key from API Ninjas (World Time API)
    BASE_URL1 = "https://api.openweathermap.org/data/2.5/weather" # API call url (weather)
    BASE_URL2 = "https://api.api-ninjas.com/v1/worldtime" # API call url (datetime)

    city = input("Enter a city name: ")
    get_datetime(API_KEY2, BASE_URL2, city)
    get_weather(API_KEY1, BASE_URL1, city)
    

if __name__ == "__main__":
    main()