import mysql.connector

def create_database_connection():
    db = mysql.connector.connect(
        host="db",
        user="root",
        password="senha",
        database="composedatabase"
    )
    return db

def create_tables():
    db = create_database_connection()
    cursor = db.cursor()

    create_user_table = """
    CREATE TABLE IF NOT EXISTS user_table (
        id INT AUTO_INCREMENT PRIMARY KEY,
        user_name VARCHAR(255),
        user_email VARCHAR(255)
    )
    """

    cursor.execute(create_user_table)
    db.commit()

    cursor.close()
    db.close()

def insert_initial_data():
    db = create_database_connection()
    cursor = db.cursor()

    data_to_insert = [
        ("larissa", "larissa@gmail.com"),
        ("daniel", "daniel@gmail.com")
    ]

    insert_query = "INSERT INTO user_table (user_name, user_email) VALUES (%s, %s)"
    cursor.executemany(insert_query, data_to_insert)
    db.commit()

    cursor.close()
    db.close()

if __name__ == "__main__":
    create_tables()
    insert_initial_data()
