import pandas as pd
import requests

format = "json"
jscmd = "details"
ISBN = "978-85-3591-169-5"

url = "http://openlibrary.org/api/books?bibkeys=ISBN:"+ISBN+"&jscmd=details&format=json"

response = requests.get(url)
print(response.json())

