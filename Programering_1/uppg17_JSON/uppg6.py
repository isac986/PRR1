import requests

objekt = requests.get("https://jsonplaceholder.typicode.com/todos/1")

info = objekt.json()
print("Titel:", info["title"])