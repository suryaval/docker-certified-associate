import requests
import json

GetReposURL = "https://api.github.com/users/suryaval/repos"

listReposResponse = requests.request("GET", url = GetReposURL)

print(listReposResponse.json())
