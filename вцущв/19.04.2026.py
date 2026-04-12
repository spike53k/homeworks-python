import sqlite3

conn = sqlite3.connect("shop.db")
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS product (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
price REAL,
stock INTEGER
)""")
cursor.execute("""CREATE TABLE IF NOT EXISTS customers (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
city TEXT
)""")
cursor.execute("""CREATE TABLE IF NOT EXISTS orders (
id INTEGER PRIMARY KEY AUTOINCREMENT,
customer_id INTEGER,
order_date TEXT
)""")
cursor.execute("""CREATE TABLE IF NOT EXISTS order_items (
id INTEGER PRIMARY KEY AUTOINCREMENT,
order_id INTEGER,
product_id INTEGER,
quantity INTEGER
)""")

def add_product(name, price, stock):
    cursor.execute("INSERT INTO product (name, price, stock) VALUES (?, ?, ?)", (name, price, stock))
    conn.commit()

def add_customer(name, city):
    cursor.execute("INSERT INTO customers (name, city) VALUES (?, ?)", (name, city))
    conn.commit()

def add_order(customer_id, order_date):
    cursor.execute("INSERT INTO orders (customer_id, order_date) VALUES (?, ?)", (customer_id, order_date))
    conn.commit()

def add_order_item(order_id, product_id, quantity):
    cursor.execute("INSERT INTO order_items (order_id, product_id, quantity) VALUES (?, ?, ?)", (order_id, product_id, quantity))
    conn.commit()

add_product("ноутбук", 40000, 10)
add_product("телефон", 25000, 15)
add_product("колонки", 3500, 8)
add_product("клавиатура", 4000, 12)

add_customer("name1", "city1")
add_customer("name2", "city2")
add_customer("name3", "city3")

add_order(1, "2026-12-04")
add_order(2, "2026-12-04")
add_order(3, "2026-12-04")

add_order_item(1, 2, 1)
add_order_item(2, 4, 2)
add_order_item(3, 1, 1)

print("общая сумма каждого заказа")
cursor.execute("""
    SELECT orders.id, SUM(product.price * order_items.quantity)
    FROM orders, order_items, product
    WHERE orders.id = order_items.order_id 
    AND order_items.product_id = product.id
    GROUP BY orders.id
""")
for order_id, total in cursor.fetchall():
    print(f"заказ {order_id}: {total}")

print("покупатели которые потратили более 5000")
cursor.execute("""
    SELECT customers.name, SUM(product.price * order_items.quantity)
    FROM customers, orders, order_items, product
    WHERE customers.id = orders.customer_id 
    AND orders.id = order_items.order_id
    AND order_items.product_id = product.id
    GROUP BY customers.id
    HAVING SUM(product.price * order_items.quantity) > 5000
""")
results = cursor.fetchall()
if results:
    for name, total in results:
        print(f"{name}: {total}")
else:
    print("нет покупателей которые потратили более 5000")

print("самый популярный товар")
cursor.execute("""
    SELECT product.name
    FROM product, order_items
    WHERE product.id = order_items.product_id
    GROUP BY product.id
    ORDER BY SUM(order_items.quantity) DESC
    LIMIT 1
""")
name = cursor.fetchall()
print(*name)