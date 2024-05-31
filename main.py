import mysql.connector

     
host = input("Enter the host name you want to connect to: ")
user_name = input("Enter the user name: ")
passwrd = input("Enter the password: ")
db_name = input("Enter the database name: ")


db = mysql.connector.connect(
            host=host,
            user=user_name,
            password=passwrd,
            database=db_name
        )
mycursor = db.cursor()

def display_menu():
    while True:
        print("\nMain Menu:")
        print("1. Add")
        print("2. Remove")
        print("3. Update")
        print("4. View")
        print("5. Search")
        print("6. Quit")

        user_option = int(input("Enter your choice (1-6): "))
        
        if user_option == 1:
            Add()
        elif user_option == 2:
            Remove()
        elif user_option == 3:
            Update()
        elif user_option == 4:
           View()
        elif user_option == 5:
            Search()
        elif user_option == 6:
            print("Exiting the program")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")


def Add():
    while True:
        print("What table would you like to add to:")
        print("\n1.Add A Customer")
        print("2.Add An Employee")
        print("3.Add something to Inventory")
        print("4.Add an item to orders")

        user_option = int(input("Enter your choice (1-4): "))
        if user_option == 1:
            while True:
                customer_no = int(input("Enter the customer number: "))
                first_name = input("Enter the first name: ")
                last_name = input("Enter the last name: ")
                phone_num = int(input("Enter the phone number: ")) 
                email = input("Enter the email: ")

                mycursor.execute("INSERT INTO customer_info (customer_No, first_name, last_name, phone_num, email) VALUES (%s, %s, %s, %s, %s)",
                (customer_no, first_name, last_name, phone_num, email))
                db.commit()

                print("\nHere's the new dataset: ")

                mycursor.execute("SELECT * FROM customer_info")

                for x in mycursor:
                    print(x)

                 
                continue_input = input("Do you want to add another customer? (yes/no): ").strip().lower()
                if continue_input != 'yes':
                    break

            # Make sure to close the cursor and the database connection if no longer needed
            mycursor.close()
            db.close()

        elif user_option == 2:
            while True:
                employee_id = int(input("Enter an employee id: "))
                E_first_name = input("Enter the employee's first name: ")
                E_last_name = input("Enter the last name: ")
                hourly_pay = float(input("Enter the hourly pay: "))
                title = input("What is their title: ")

                mycursor.execute("INSERT INTO employee_info (employee_id, first_name, last_name, hourly_pay, title) VALUES (%s, %s, %s, %s, %s)",
                (employee_id, E_first_name, E_last_name, hourly_pay, title))
                
                db.commit()

                print("\nHere's the new dataset: ")

                mycursor.execute("SELECT * FROM employee_info")

                for x in mycursor:
                  print(x)

                 
                continue_input = input("Do you want to add another employee? (yes/no): ").strip().lower()
                if continue_input != 'yes':
                        break

            
            mycursor.close()
            db.close()
        elif user_option == 3:
            product_number = int(input("Enter the product number: "))
            brand = input("Enter the product's brand: ")
            quanity = int(input("Enter the current quanity: "))
            price = float(input("Enter the bulk cost: "))
            supplier= input("Enter supplier's name: ")
            
            mycursor.execute("INSERT INTO inventory (product_number, brand, quantity, price, supplier) VALUES (%s,%s, %s, %s, %s)", (product_number, brand, quanity, price, supplier))
            db.commit

            print("\nHere's the new dataset: ")

            mycursor.execute("Select *  FROM inventory")

            for x in mycursor:
                print(x)
            break

        elif user_option == 4:
            order_number= int(input("Enter an employee id: "))
            customer_no = input("Enter the employee's first name: ")
            employee_id = input("Enter the last name: ")
            hourly_pay = int(input("Enter the hourly pay: "))
            title = input("What their title: ")
            
            mycursor.execute("INSERT INTO employee_info (employee_id, first_name, last_name, hourly_pay, title) VALUES (%s,%s, %s, %s, %s)", (employee_id, E_first_name, E_last_name, hourly_pay, title))
            db.commit

            print("\nHere's the new dataset: ")

            mycursor.execute("Select *  FROM customer_info")

            for x in mycursor:
                print(x)
            break
        





display_menu()
