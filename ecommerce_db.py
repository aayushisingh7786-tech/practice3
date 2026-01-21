import sqlite3

# 1. Connect to database (it creates the file if it doesn't exist)
conn = sqlite3.connect('ecommerce.db')
cursor = conn.cursor()

# 2. CREATE TABLES (The Structure)
def create_tables():
    # USERS Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL
        )
    ''')
    # CATEGORIES Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS categories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    ''')
    # PRODUCTS Table (Linked to Categories via Foreign Key)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL,
            category_id INTEGER,
            FOREIGN KEY (category_id) REFERENCES categories (id)
        )
    ''')
    # ORDERS Table (Linked to Users via Foreign Key)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            product_id INTEGER,
            order_date TEXT,
            FOREIGN KEY (user_id) REFERENCES users (id),
            FOREIGN KEY (product_id) REFERENCES products (id)
        )
    ''')
    print("✅ Tables created successfully.")

# 3. INSERT DATA (CRUD - Create)
def insert_dummy_data():
    # Add Categories
    cursor.execute("INSERT OR IGNORE INTO categories (name) VALUES ('Electronics')")
    cursor.execute("INSERT OR IGNORE INTO categories (name) VALUES ('Books')")
    # Add Users
    cursor.execute("INSERT OR IGNORE INTO users (name, email) VALUES ('Rahul', 'rahul@example.com')")
    cursor.execute("INSERT OR IGNORE INTO users (name, email) VALUES ('Priya', 'priya@example.com')")
    # Add Products (Using Category IDs 1 and 2)
    cursor.execute("INSERT INTO products (name, price, category_id) VALUES ('Laptop', 45000.00, 1)")
    cursor.execute("INSERT INTO products (name, price, category_id) VALUES ('Python Guide', 500.00, 2)")
    # Add an Order (Rahul bought a Laptop)
    cursor.execute("INSERT INTO orders (user_id, product_id, order_date) VALUES (1, 1, '2025-10-25')")
    conn.commit()
    print("✅ Dummy data inserted.")

# 4. QUERY DATA (CRUD - Read with JOIN)
def show_all_orders():
    print("\n--- ALL ORDERS (Using SQL JOIN) ---")
    # This query joins 3 tables to show readable names instead of just IDs
    sql = '''
        SELECT users.name, products.name, products.price, orders.order_date
        FROM orders
        JOIN users ON orders.user_id = users.id
        JOIN products ON orders.product_id = products.id
    '''
    cursor.execute(sql)
    rows = cursor.fetchall()
    for row in rows:
        print(f"Customer: {row[0]} | Bought: {row[1]} | Price: ₹{row[2]} | Date: {row[3]}")

# RUN THE FUNCTIONS
if __name__ == "__main__":
    create_tables()
    insert_dummy_data()
    show_all_orders()
    # Close connection
    conn.close()
