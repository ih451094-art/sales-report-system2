import sqlite3


DATABASE = "database.db"


def get_connection():
    connection = sqlite3.connect(DATABASE)

    connection.row_factory = sqlite3.Row

    return connection
def create_tables():

    connection = get_connection()

    cursor = connection.cursor()


    # المستخدمين
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            username TEXT NOT NULL UNIQUE,

            password TEXT NOT NULL,

            role TEXT NOT NULL DEFAULT 'user'

        )
    """)


    # المطاعم
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS restaurants (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            name TEXT NOT NULL UNIQUE

        )
    """)


    # الفروع
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS branches (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            restaurant_id INTEGER NOT NULL,

            name TEXT NOT NULL,

            FOREIGN KEY (restaurant_id)
                REFERENCES restaurants(id)

        )
    """)


    # شركات التوصيل
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS delivery_companies (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            name TEXT NOT NULL UNIQUE

        )
    """)


    # التقارير
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS reports (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            restaurant_id INTEGER NOT NULL,

            report_date TEXT NOT NULL,

            created_at TEXT DEFAULT CURRENT_TIMESTAMP,

            FOREIGN KEY (restaurant_id)
                REFERENCES restaurants(id)

        )
    """)


    # تفاصيل التقرير
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS report_rows (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            report_id INTEGER NOT NULL,

            branch_id INTEGER NOT NULL,

            delivery_company_id INTEGER NOT NULL,

            orders_count INTEGER NOT NULL DEFAULT 0,

            amount REAL NOT NULL DEFAULT 0,

            FOREIGN KEY (report_id)
                REFERENCES reports(id),

            FOREIGN KEY (branch_id)
                REFERENCES branches(id),

            FOREIGN KEY (delivery_company_id)
                REFERENCES delivery_companies(id)

        )
    """)


    connection.commit()

    connection.close()
    

if __name__ == "__main__":
    create_tables()

    print("Database created successfully.")