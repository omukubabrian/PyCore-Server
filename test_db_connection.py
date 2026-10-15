from database import get_db_connection

try:
    connection=get_db_connection()

    if connection.is_connected():

        print("Successfully connected to MySQL!")

        print("Database:",connection.database)

    connection.close()

except Exception as error:

    print("Database connection failed.")
    
    print("Error:",error)