item_counts = {}
with open("data.txt", "r", encoding="utf-8") as file:
    for line in file:
        line = line.strip()
        if line and "," in line:
            parts = line.split(",")
            item_name = parts[0].strip()
            quantity = int(parts[1].strip())
            if item_name in item_counts:
                item_counts[item_name] += quantity
            else:
                item_counts[item_name] = quantity

with open("corrected_data.txt", "w", encoding="utf-8") as file:
    for item, count in item_counts.items():
        file.write(f"{item}, {count}\n")

total_items = sum(item_counts.values())
most_popular = ""
max_count = 0

for item, count in item_counts.items():
    if count > max_count:
        max_count = count
        most_popular = item

print(f"Количество товаров: {total_items}")
print(f"Самый популярный товар: {most_popular} {max_count} штук")