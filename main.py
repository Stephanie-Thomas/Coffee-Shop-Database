import mysql.connector
import customer
import employee



def display_menu():
    while True:
        print("\nMain Menu:")
        print("1. Employee Management")
        print("2. Customer Management")
        print("3. Inventory Management")
        print("4. Order Management")
        print("5. Exit")

        user_option = int(input("Enter your choice (1-5): "))
        
        if user_option == 1:
            employee_management_menu()
        elif user_option == 2:
            customer_management_menu()
        elif user_option == 3:
            inventory_management_menu()
        elif user_option == 4:
            order_management_menu()
        elif user_option == 5:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


def employee_management_menu():
     while True:
        print("\nEmployee Management:")
        print("1. Add new employee")
        print("2. Remove employee")
        print("3. Update employee details")
        print("4. View employees")
        print("5. Search employees")
        print("6. Back to Main Menu")

        user_option = int(input("Enter your choice (1-6): "))
       

        if user_option == 1:
            add_new_employee()
        elif user_option == 2:
            remove_employee()
        elif user_option == 3:
            update_employee_details()
        elif user_option == 4:
            view_employees()
        elif user_option == 5:
            search_employees()
        elif user_option == 6:
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6")

def customer_management_menu():
    while True:
        print("\nCustomer Management:")
        print("1. Add new customer")
        print("2. Remove customer")
        print("3. Update customer details")
        print("4. View customers")
        print("5. Search customers")
        print("6. Back to Main Menu")

        user_option = int(input("Enter your choice (1-6): "))
        
        
        if user_option == 1:
            add_new_customer()
        elif user_option == 2:
            remove_customer()
        elif user_option == 3:
            update_customer_details()
        elif user_option == 4:
            view_customers()
        elif user_option == 5:
            search_customers()
        elif user_option == 6:
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6")


def inventory_management_menu():
    while True:
        print("\nInventory Management:")
        print("1. Add new item")
        print("2. Remove item")
        print("3. Update item details")
        print("4. View inventory")
        print("5. Search inventory")
        print("6. Back to Main Menu")

        user_option = int(input("Enter your choice (1-6): "))
        
        if user_option == 6:
            break
def order_management_menu():
    while True:
        print("\nOrder Management:")
        print("1. Place new order")
        print("2. Cancel order")
        print("3. Update order")
        print("4. View orders")
        print("5. Search orders")
        print("6. Back to Main Menu")

        user_option = int(input("Enter your choice (1-6): "))
        # Implement actions for order management based on user choice
        if user_option == 6:
            break


print("Welcome! This program is an interactive database management application\n")


host = input("Enter the host name you want to connect to: ")
user_name = input("Enter the user name: ")
passwrd = input("Enter the passowrd: ")
db_name = input("Enter the database: ")

db = mysql.connector.connect(
    host = host,
    user = user_name,
    password = passwrd,
    database = db_name
)


display_menu()
