import sqlite3

conn = sqlite3.connect("company.db")
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS departments (
ID INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL UNIQUE,
budget REAL
)""")

cursor.execute("""CREATE TABLE IF NOT EXISTS employees (
ID INTEGER PRIMARY KEY AUTOINCREMENT,
first_name TEXT NOT NULL,
last_name TEXT NOT NULL,
department_id INTEGER,
salary REAL,
hire_date TEXT
)""")

cursor.execute("""CREATE TABLE IF NOT EXISTS salary_history (
ID INTEGER PRIMARY KEY AUTOINCREMENT,
employee_id INTEGER,
old_salary REAL,
new_salary REAL,
change_date TEXT
)""")

def add_department(name, budget):
    cursor.execute("INSERT INTO departments (name, budget) VALUES (?, ?)", (name, budget))

def add_employee(first_name, last_name, department_id, salary):
    cursor.execute("INSERT INTO employees (first_name, last_name, department_id, salary) VALUES (?, ?, ?, ?)",
                   (first_name, last_name, department_id, salary))
def update_salary(employee_id, new_salary):
    cursor.execute("SELECT salary FROM employees WHERE id = ?", (employee_id,))
    old_salary = cursor.fetchone()[0]
    cursor.execute("UPDATE employees SET salary = ? WHERE id = ?", (new_salary, employee_id))
    cursor.execute("INSERT INTO salary_history (employee_id, old_salary, new_salary) VALUES (?, ?, ?)",
                   (employee_id, old_salary, new_salary))

add_department("IT", 2000000)
add_department("Бухгалтерия", 1000000)
add_department("Маркетинг", 1500000)

add_employee("first_name1", "last_name1", 1, 60000)
add_employee("first_name2", "last_name2", 1, 90000)
add_employee("first_name3", "last_name3", 2, 40000)
add_employee("first_name4", "last_name4", 3, 65000)
add_employee("first_name5", "last_name5", 3, 100000)

update_salary(3, 55000)
update_salary(1, 70000)
update_salary(4, 80000)

conn.commit()

cursor.execute("SELECT id, first_name, last_name, salary FROM employees")
for row in cursor.fetchall():
    print(row)

cursor.execute("SELECT name FROM departments WHERE budget > 500000")
for row in cursor.fetchall():
    print(row)

cursor.execute("SELECT COUNT(*) FROM employees e JOIN departments d ON e.department_id = d.id WHERE d.name = 'IT'",)
count = cursor.fetchall()
print(*count)

cursor.execute("SELECT e.first_name, e.last_name, d.name FROM employees e JOIN departments d ON e.department_id = d.id")
for row in cursor.fetchall():
    print(row)

cursor.execute("SELECT MAX(salary) FROM employees")
print(cursor.fetchone()[0])

conn.close()