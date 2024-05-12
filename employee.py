import mysql.connector

class employee:
    def __init__(self, db_connection):
        self.db_connection = db_connection
        cursor = self.db_connection.cursor()
    
    def add_new_employee(self):
        cursor = self.db_connection.cursor()
        print("Adding new employee")
        employeeid = int(input("Enter an employee id: "))
        first_name = input("Enter the first name: ")
        last_name = input("Enter the last name: ")
        pay = float(input("Enter hourly pay: "))
        position = input("Enter thier position: ")

        cursor.execute("INSERT INTO customer_info VALUES(%s, %s, %s,%s,%s)" (employeeid, first_name, last_name, pay, position))


        

    def remove_employee(self):
        print("Remove employee")
    
    def update_employee_details(self):
        print("Updating employee details")

    def view_employees(self):
        print("Viewing employees")
    
    def search_employees(self):
        print("Searching employees")