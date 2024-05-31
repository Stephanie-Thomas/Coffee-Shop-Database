import mysql.connector

class connect_to_database(host, user_name, passwrd, db_name):
    return mysql.conntector.connect(
    host = host,
    user = user_name,
    password = passwrd,
    database = db_name)



