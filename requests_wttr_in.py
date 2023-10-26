import requests

# :help
url = 'https://wttr.in'

weather_parameters = {
    '0': '',
    'T': '',
    # 'lang': 'ru',
    'M': ''
}

request_headers = {
    'Accept-Language': 'ru'

}

response = requests.get(url, params=weather_parameters, headers=request_headers)
print(response.text)
