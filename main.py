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
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")



def Add():
    tables = {
        1: ("customer_info", ["customer_No", "first_name", "last_name", "phone_num", "email"]),
        2: ("employee_info", ["employee_id", "first_name", "last_name", "hourly_pay", "title"]),
        3: ("inventory", ["product_number", "brand", "quantity", "price", "supplier"]),
        4: ("orders", ["order_number", "customer_No", "employee_id", "order_date", "total_amount"])
    }

    print("What table would you like to add to:")
    for key, value in tables.items():
        print(f"{key}. Add to {value[0]}")

    while True:
        try:
            user_option = int(input("\nEnter your choice (1-4): "))
            if user_option not in tables:
                print("Invalid choice. Please enter a number from 1 to 4.")
                continue

            table_name, columns = tables[user_option]
            
            while True:
                new_entry = {}
                for column in columns:
                    if column in ['customer_No', 'employee_id', 'product_number', 'order_number', 'quantity']:
                        new_entry[column] = int(input(f"Enter the {column}: "))
                    elif column in ['hourly_pay', 'price', 'total_amount']:
                        new_entry[column] = float(input(f"Enter the {column}: "))
                    else:
                        new_entry[column] = input(f"Enter the {column}: ")

                placeholders = ', '.join(['%s'] * len(columns))
                query = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({placeholders})"
                mycursor.execute(query, tuple(new_entry.values()))
                db.commit()

                print(f"\nHere's the new dataset for {table_name}:")
                mycursor.execute(f"SELECT * FROM {table_name}")
                for x in mycursor:
                    print(x)

                continue_input = input(f"Do you want to add another entry to {table_name}? (yes/no): ").strip().lower()
                if continue_input != 'yes':
                    break

            break  # Exit the outer while loop

        except ValueError:
            print("\nInvalid input. Please ensure you're entering the correct data types.")
        except Exception as e:
            print(f"An error occurred: {e}")
            print("Please try again.")

    # Close the cursor and the database connection
    mycursor.close()
    db.close()
def Remove():
    tables = {
        1: "customer_info",
        2: "employee_info",
        3: "inventory",
        4: "orders"
    }

    print("Which table would you like to remove from:")
    for key, value in tables.items():
        print(f"{key}. Remove from {value}")

    while True:
        try:
            user_option = int(input("\nEnter your choice (1-4): "))
            if user_option not in tables:
                print("Invalid choice. Please enter a number from 1 to 4.")
                continue

            table_name = tables[user_option]
            id_column = input(f"Enter the ID column name for {table_name}: ")
            id_value = input(f"Enter the {id_column} of the record to remove: ")

            query = f"DELETE FROM {table_name} WHERE {id_column} = %s"
            mycursor.execute(query, (id_value,))
            db.commit()

            if mycursor.rowcount > 0:
                print(f"Record successfully removed from {table_name}")
            else:
                print(f"No record found with {id_column} = {id_value}")

            break

        except ValueError:
            print("\nInvalid input. Please ensure you're entering the correct data types.")
        except Exception as e:
            print(f"An error occurred: {e}")
            print("Please try again.")

def Update():
    tables = {
        1: "customer_info",
        2: "employee_info",
        3: "inventory",
        4: "orders"
    }

    print("Which table would you like to update:")
    for key, value in tables.items():
        print(f"{key}. Update {value}")

    while True:
        try:
            user_option = int(input("\nEnter your choice (1-4): "))
            if user_option not in tables:
                print("Invalid choice. Please enter a number from 1 to 4.")
                continue

            table_name = tables[user_option]
            id_column = input(f"Enter the ID column name for {table_name}: ")
            id_value = input(f"Enter the {id_column} of the record to update: ")

            mycursor.execute(f"SHOW COLUMNS FROM {table_name}")
            columns = [column[0] for column in mycursor.fetchall() if column[0] != id_column]

            print(f"Available columns to update: {', '.join(columns)}")
            column_to_update = input("Enter the column name you want to update: ")
            if column_to_update not in columns:
                print("Invalid column name.")
                continue

            new_value = input(f"Enter the new value for {column_to_update}: ")

            query = f"UPDATE {table_name} SET {column_to_update} = %s WHERE {id_column} = %s"
            mycursor.execute(query, (new_value, id_value))
            db.commit()

            if mycursor.rowcount > 0:
                print(f"Record successfully updated in {table_name}")
            else:
                print(f"No record found with {id_column} = {id_value}")

            break

        except ValueError:
            print("\nInvalid input. Please ensure you're entering the correct data types.")
        except Exception as e:
            print(f"An error occurred: {e}")
            print("Please try again.")

def View():
    tables = {
        1: "customer_info",
        2: "employee_info",
        3: "inventory",
        4: "orders"
    }

    print("Which table would you like to view:")
    for key, value in tables.items():
        print(f"{key}. View {value}")

    while True:
        try:
            user_option = int(input("\nEnter your choice (1-4): "))
            if user_option not in tables:
                print("Invalid choice. Please enter a number from 1 to 4.")
                continue

            table_name = tables[user_option]
            
            mycursor.execute(f"SELECT * FROM {table_name}")
            results = mycursor.fetchall()

            if results:
                print(f"\nData in {table_name}:")
                for row in results:
                    print(row)
            else:
                print(f"No data found in {table_name}")

            break

        except ValueError:
            print("\nInvalid input. Please enter a number.")
        except Exception as e:
            print(f"An error occurred: {e}")
            print("Please try again.")

def Search():
    tables = {
        1: "customer_info",
        2: "employee_info",
        3: "inventory",
        4: "orders"
    }

    print("Which table would you like to search in:")
    for key, value in tables.items():
        print(f"{key}. Search in {value}")

    while True:
        try:
            user_option = int(input("\nEnter your choice (1-4): "))
            if user_option not in tables:
                print("Invalid choice. Please enter a number from 1 to 4.")
                continue

            table_name = tables[user_option]
            
            mycursor.execute(f"SHOW COLUMNS FROM {table_name}")
            columns = [column[0] for column in mycursor.fetchall()]

            print(f"Available columns to search: {', '.join(columns)}")
            search_column = input("Enter the column name you want to search in: ")
            if search_column not in columns:
                print("Invalid column name.")
                continue

            search_value = input(f"Enter the value to search for in {search_column}: ")

            query = f"SELECT * FROM {table_name} WHERE {search_column} LIKE %s"
            mycursor.execute(query, (f"%{search_value}%",))
            results = mycursor.fetchall()

            if results:
                print(f"\nSearch results in {table_name}:")
                for row in results:
                    print(row)
            else:
                print(f"No results found in {table_name} for {search_column} like '{search_value}'")

            break

        except ValueError:
            print("\nInvalid input. Please ensure you're entering the correct data types.")
        except Exception as e:
            print(f"An error occurred: {e}")
            print("Please try again.")

display_menu()
