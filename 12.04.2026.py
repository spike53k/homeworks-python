import sqlite3

conn = sqlite3.connect("shop.db")
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS customers (
ID INTEGER PRIMARY KEY,
name TEXT,
email TEXT UNIQUE,
phone TEXT
)""")
cursor.execute("""CREATE TABLE IF NOT EXISTS products (
ID INTEGER PRIMARY KEY,
name TEXT,
price REAL,
stock INTEGER
)""")
cursor.execute("""CREATE TABLE IF NOT EXISTS orders (
ID INTEGER PRIMARY KEY,
customer_id INTEGER,
product_id INTEGER,
quantity INTEGER,
order_date TEXT,
FOREIGN KEY(customer_id) REFERENCES customers(id),
FOREIGN KEY(product_id) REFERENCES products(id)
)""")

def add_customer(name, email, phone):
    cursor.execute("INSERT INTO customers (name, email, phone) VALUES(?,?,?)", (name, email, phone))
    conn.commit()

def add_product(name, price, stock):
    cursor.execute("INSERT INTO products (name, price, stock) VALUES(?,?,?)", (name, price, stock))
    conn.commit()

def place_order(customer_id, product_id, quantity, order_date):
    cursor.execute("INSERT INTO orders (customer_id, product_id, quantity, order_date) VALUES(?,?,?,?)", (customer_id, product_id, quantity, order_date))
    conn.commit()

add_customer("N1", "N1@email.ru", "8912 345 67 89")
add_customer("N2", "N2@email.ru", "8902 365 67 49")
add_customer("N3", "N3@email.ru", "8982 745 67 83")

add_product("Телефон", 20000, 11)
add_product("Холодильник", 15000, 3)
add_product("Диван", 45000, 2)
add_product("Наушники", 3000, 7)
add_product("Вода", 50, 15)

place_order(2, 1, 1, "2026-04-11")
place_order(2, 5, 2, "2026-04-10")
place_order(3, 3, 1, "2026-04-09")
place_order(1, 4, 1, "2026-04-11")

cursor.execute("""SELECT orders.id, customers.name, products.name, orders.quantity, orders.order_date
FROM orders
JOIN customers ON orders.customer_id = customers.id
JOIN products ON orders.product_id = products.id
""")
for i in cursor.fetchall():
    print(i)

cursor.execute("SELECT name, stock FROM products WHERE stock < 10")
for i in cursor.fetchall():
    print(i)

cursor.execute("""SELECT customers.name, SUM(products.price * orders.quantity)
FROM orders
JOIN customers ON orders.customer_id = customers.id
JOIN products ON orders.product_id = products.id
GROUP BY customers.id
""")
for i in cursor.fetchall():
    print(i)

def get_orders_by_customer(customer_id):
    cursor.execute("SELECT * FROM orders WHERE customer_id = ?", (customer_id,))
    return cursor.fetchall()

def update_product_stock(product_id, new_stock):
    cursor.execute("""UPDATE products SET stock = ? WHERE id = ?""", (new_stock, product_id))
    conn.commit()