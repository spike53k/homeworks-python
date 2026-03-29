import json

with open("products.json", "r",encoding="utf-8") as file:
    data = json.load(file)
    for item in data:
        item["discount"] = "10%"
        item["price"] = item["price"] * 0.9

    for item in data:
        if item["price"] > 1000 and item["in_stock"] == True:
            print(item["name"], item["price"], item["category"], item["discount"])