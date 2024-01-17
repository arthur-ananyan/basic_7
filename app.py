import requests
import deepdiff

url = "https://www.google.com/"

r = requests.get(url)
print(r.status_code)