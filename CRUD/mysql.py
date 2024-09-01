import mysql.connector

# Establishing the connection
connection = mysql.connector.connect(
    host="127.0.0.1",       # Your host, usually localhost
    user="root",   # Your MySQL username
    password="",  # Your MySQL password
    database="test"   # The database you want to use
)

# Creating a cursor object using the cursor() method
cursor = connection.cursor()

# Checking if the connection was successful
if connection.is_connected():
    print("Successfully connected to the database")


# Create
insert_query = "INSERT INTO crud (name, email) VALUES (%s, %s)"
values = ("value2", "value3")
cursor.execute(insert_query, values)
connection.commit()

# Read
select_query = "SELECT * FROM crud"
cursor.execute(select_query)
records = cursor.fetchall()
if not records:
    print("No records found.")
else:
    for row in records:
        print(row)

# Update
update_query = "UPDATE crud SET name = %s WHERE email = %s"
values = ("lakhwider", "value3")
cursor.execute(update_query, values)
connection.commit()

# Delete
delete_query = "DELETE FROM crud WHERE id = %s"
value = (10,)
cursor.execute(delete_query, value)
connection.commit()

# Close the connection
cursor.close()
connection.close()