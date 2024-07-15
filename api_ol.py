import pandas as pd
import requests

format = "json"
jscmd = "details"
ISBN = "978-85-3591-169-5"

url_data = "http://openlibrary.org/api/books?bibkeys=ISBN:"+ISBN+"&jscmd=data&format=json"
url_details = "http://openlibrary.org/api/books?bibkeys=ISBN:"+ISBN+"&jscmd=details&format=json"

def chamar_api_ol(url):
    response = requests.get(url)
    return response

response_data = chamar_api_ol(url_data).json()
response_details = chamar_api_ol(url_details).json()

normalizado = pd.json_normalize(response_data)

df_data = pd.DataFrame(normalizado)

df_data.to_excel('texte.xlsx')








