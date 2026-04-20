import sqlite3

conn = sqlite3.connect("company.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS departments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    budget INTEGER
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    department_id INTEGER,
    salary INTEGER,
    hire_date TEXT,
    FOREIGN KEY(department_id) REFERENCES departments(id)
)
""")
conn.commit()

def add_department(name, budget):
    cursor.execute("INSERT INTO departments (name, budget) VALUES (?, ?)", (name, budget))
    conn.commit()

def add_employee(name, department_id, salary, hire_date):
    cursor.execute("INSERT INTO employees (name, department_id, salary, hire_date) VALUES (?, ?, ?, ?)",
                   (name, department_id, salary, hire_date))
    conn.commit()

add_department("dep1", 500000)
add_department("dep2", 300000)
add_department("dep3", 200000)

add_employee("Александр", 1, 95000, "2019-05-12")
add_employee("Мария", 1, 105000, "2020-03-15")
add_employee("Дмитрий", 1, 80000, "2024-11-01")
add_employee("Елена", 2, 60000, "2018-02-20")
add_employee("Алексей", 2, 70000, "2021-06-10")
add_employee("Ольга", 2, 55000, "2025-01-15")
add_employee("Иван", 3, 50000, "2017-09-30")
add_employee("Татьяна", 3, 45000, "2023-08-22")
add_employee("Сергей", 1, 110000, "2022-04-10")
add_employee("Наталья", 2, 58000, "2024-05-12")

print("Отдел с максимальной суммарной зарплатой:")
cursor.execute("""
    SELECT departments.name, SUM(employees.salary)
    FROM departments, employees
    WHERE departments.id = employees.department_id
    GROUP BY departments.id
    ORDER BY SUM(employees.salary) DESC
    LIMIT 1
""")
result_task_3 = cursor.fetchone()
if result_task_3:
    print(f"Название отдела: {result_task_3[0]}, Сумма зарплат: {result_task_3[1]}")

cursor.execute("""
    SELECT employees.name, employees.salary, departments.name
    FROM employees, departments
    WHERE employees.department_id = departments.id
    AND employees.salary > (
        SELECT AVG(salary) 
        FROM employees 
        WHERE department_id = employees.department_id
    )
""")
for name, salary, dept_name in cursor.fetchall():
    print(f"Сотрудник: {name}, Зарплата: {salary}, Отдел: {dept_name}")

cursor.execute("""
    SELECT name, hire_date 
    FROM employees 
    WHERE hire_date <= '2023-04-20'
""")
for name, date in cursor.fetchall():
    print(f"Имя: {name}, Дата приема: {date}")

conn.close()