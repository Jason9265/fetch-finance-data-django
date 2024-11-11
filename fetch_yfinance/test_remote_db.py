import MySQLdb as Database

def test_mysql_connection():
    try:
        connection = Database.connect(
            host='jason97965.helioho.st',
            user='jason97965_admin',
            password='admin',
            db='jason97965_practice',
            ssl_mode='DISABLED'
        )
        
        if connection.is_connected():
            db_info = connection.get_server_info()
            print(f"Successfully connected to MySQL Server version {db_info}")
            
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print(f"Connected to database: {record[0]}")
            
            # Test table creation
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS test_connection (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(100),
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            print("Test table created successfully!")

    except Database.Error as e:
        print(f"Error while connecting to MySQL: {e}")
    
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

if __name__ == "__main__":
    test_mysql_connection()