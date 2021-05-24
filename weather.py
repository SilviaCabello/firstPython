import requests

api_key = "08bc139c456596450dfe0769403f6c5e"
city = "Valencia"
url = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api_key+"&units=metric"

request = requests.get(url)
json = request.json()
print(json)
