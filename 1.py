import requests

response = requests.get("https://openlibrary.org/search.json?q=war+and+peace")
data = response.json()
print(f"Первая книга: {data['docs'][0]['title']}")

response = requests.get("https://openlibrary.org/search.json?q=lord+of+the+rings")
data = response.json()
print(f"Название: {data['docs'][0]['title']}")
print(f"Автор: {data['docs'][0]['author_name']}")
print(f"Год издания: {data['docs'][0]['first_publish_year']}")