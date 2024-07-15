import requests
import webbrowser

ISBN = '978-85-3591-182-4'

url = 'https://bookcover.longitood.com/bookcover/'+ISBN

response = requests.get(url).json()['url']

abrir_url = webbrowser.open(response,new = 2)










