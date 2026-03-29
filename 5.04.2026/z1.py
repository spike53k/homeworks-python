import json

with open("students.json", "r", encoding="utf-8") as file:
    data = json.load(file)
    for item in data:
        print(item["name"], item["gpa"])