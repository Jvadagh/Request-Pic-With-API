import webbrowser
import requests

response = requests.get('https://dog.ceo/api/breeds/image/random')
webbrowser.open(response.json()['message'])
