import mysql.connector

class customer:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    
    def add_new_customer(self):
        print("Adding new customer")

    def remove_customer(self):
        print("Removing customer")
    
    def update_customer_details(self):
        print("Updating customer details")

    def view_customers(self):
        print("Viewing customers")
    
    def search_customers(self):
        print("Searching customers")
