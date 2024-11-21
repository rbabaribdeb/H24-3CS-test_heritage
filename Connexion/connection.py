import oracledb as db
# Set your database connection information here
username = "sys"              # Replace with your database username
password = "oracle"           # Replace with your database password
host = "localhost"            # Replace with your Oracle server's hostname or IP address
port = "1521"                 # Replace with the Oracle service port (usually 1521)
service_name = "freepdb1"     # Replace with your Oracle service name or SID
# Create a DSN (Data Source Name) The DSN (Data Source Name) combines the host, port, and service_name into a single connection string. This tells the program where to find the database.
dsn = db.makedsn(host, port, service_name=service_name)
# Se connecter connection 
try:
    connection = db.connect(user=username, password=password, dsn=dsn, mode=db.SYSDBA)
    print("Successfully connected to Oracle Database as SYSDBA")
    # Example usage - creating a cursor and executing a query
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM hr.employees")  # Replace with your table name
    # Fetch and print the rows
    for row in cursor:
        print(row)
    # Close the cursor and connection
    cursor.close()
    connection.close()
except db.DatabaseError as e:
    error, = e.args
    print(f"Error connecting to Oracle Database: {error}")
