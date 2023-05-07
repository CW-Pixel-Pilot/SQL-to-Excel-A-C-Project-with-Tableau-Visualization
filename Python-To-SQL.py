import mysql.connector

# Connect to the database
cnx = mysql.connector.Connect(user='mysql',password='password',host='localhost',database='Adventure_Works')

# Create a cursor object
cursor = cnx.cursor()

# Execute a SELECT Query
query = ("SELECT Name, SalesPersonID FROM Adventure_Works.Sales_Store;")
cursor.execute(query)

# Print the results
for (Name, SalesPersonID) in cursor:
    print("{} {}".format(Name, SalesPersonID))

# Close the cursor and connection
cursor.close()
cnx.close()
