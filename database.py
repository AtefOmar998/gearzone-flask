import sqlite3

# اتصال بقاعدة البيانات (أو إنشاءها إن لم تكن موجودة)
conn = sqlite3.connect('gearzone.db')
c = conn.cursor()

# إنشاء جدول المستخدمين
c.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        type TEXT NOT NULL
    )
''')

# إنشاء جدول المنتجات
c.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price REAL NOT NULL,
        description TEXT,
        owner_id INTEGER,
        FOREIGN KEY (owner_id) REFERENCES users (id)
    )
''')

conn.commit()
conn.close()

print("✅ Database and tables created successfully.")