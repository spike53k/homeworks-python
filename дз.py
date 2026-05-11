import requests

api_key = "71b9e9fe-03fd-4178-8f7b-8496c974ea38"
url = "https://api.le-systeme-solaire.net/rest/bodies/"

headers = {
    "Authorization": f"Bearer {api_key}",
}
params = {
    "filter[]": "isPlanet,eq,true",
}

response = requests.get(url,  headers=headers, params=params)
response.raise_for_status()
data = response.json()

for planet in data["bodies"]:
    print(planet["englishName"])