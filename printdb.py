from persistence import *

def main():
    printActivities()
    printBranches()
    printEmployees()
    printProducts()
    printSuppliers()
    printReport()
    printActivityReport()


def printActivities():
    print("Activities")
    cursor = repo._conn.cursor()
    cursor.execute("SELECT * FROM activities")
    for action in cursor.fetchall():
        print(action)

def printBranches():
    print("Branches")
    cursor = repo._conn.cursor()
    cursor.execute("SELECT * FROM branches")
    for branch in cursor.fetchall():
        print(branch)

def printEmployees():
    print("Employees")
    cursor = repo._conn.cursor()
    cursor.execute("SELECT * FROM employees")
    for employee in cursor.fetchall():
        print(employee)

def printProducts():
    print("Products")
    cursor = repo._conn.cursor()
    cursor.execute("SELECT * FROM products")
    for product in cursor.fetchall():
        print(product)

def printSuppliers():
    print("Suppliers") 
    cursor = repo._conn.cursor()
    cursor.execute("SELECT * FROM suppliers")
    for supplier in cursor.fetchall():
        print(supplier)

def printReport():
    print("")
    print("Employees report")
    cursor = repo._conn.cursor()

    cursor.execute("SELECT employees.id, employees.name, employees.salary, branches.location FROM employees JOIN branches ON employees.branche = branches.id ORDER BY name")
    for report in cursor.fetchall():
        cursor2 = repo._conn.cursor()
        total_sales_income = cursor2.execute(f"SELECT SUM(-1 * activities.quantity * products.price) AS total_sales_income FROM activities JOIN products ON activities.product_id = products.id WHERE activities.activator_id={report[0]} AND activities.quantity < 0").fetchall()

        if(total_sales_income[0] != (None, )):
            report+= (total_sales_income[0])
            report = report[1:]
            print(*report)
        else:
            report+= (0,)
            report = report[1:]
            print(*report)

def printActivityReport():
    print("")
    print("Activities report")
    cursor = repo._conn.cursor()
    command = "SELECT activities.date, products.description, activities.quantity, employees.name, suppliers.name FROM activities INNER JOIN products ON activities.product_id = products.id LEFT JOIN employees ON activities.activator_id = employees.id LEFT JOIN suppliers ON activities.activator_id = suppliers.id ORDER BY activities.date"

    cursor.execute(command)
    for report in cursor.fetchall():
        print(report)

if __name__ == '__main__':
    main()