import sqlite3

def init_db():
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_title TEXT NOT NULL,
            price REAL NOT NULL DEFAULT 0.0,
            quantity INTEGER NOT NULL DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()

def add_items():
    items = [
        ('Мыло жидкое', 90.0, 15),
        ('Мыло хозяйственное', 25.0, 40),
        ('Шампунь', 150.5, 10),
        ('Зубная паста', 85.0, 20),
        ('Зубная щетка', 45.0, 30),
        ('Порошок 1кг', 350.0, 5),
        ('Кондиционер', 280.0, 4),
        ('Влажные салфетки', 55.0, 50),
        ('Освежитель', 120.0, 8),
        ('Чистящее средство', 95.0, 12),
        ('Губки 3шт', 35.0, 60),
        ('Тряпка микрофибра', 65.0, 25),
        ('Гель для душа', 190.0, 7),
        ('Пена для бритья', 210.0, 3),
        ('Мыло детское', 40.0, 45)
    ]
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()
    cursor.executemany('INSERT INTO products (product_title, price, quantity) VALUES (?, ?, ?)', items)
    conn.commit()
    conn.close()

def update_q(p_id, val):
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE products SET quantity = ? WHERE id = ?', (val, p_id))
    conn.commit()
    conn.close()

def update_p(p_id, val):
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE products SET price = ? WHERE id = ?', (val, p_id))
    conn.commit()
    conn.close()

def delete_by_id(p_id):
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM products WHERE id = ?', (p_id,))
    conn.commit()
    conn.close()

def print_all():
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM products')
    rows = cursor.fetchall()
    for r in rows:
        print(r)
    conn.close()

def filter_data():
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM products WHERE price < 100 AND quantity > 5')
    rows = cursor.fetchall()
    for r in rows:
        print(r)
    conn.close()

def find_by_title(name):
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM products WHERE product_title LIKE ?', ('%' + name + '%',))
    rows = cursor.fetchall()
    for r in rows:
        print(r)
    conn.close()

# Тестирование
init_db()
add_items()

print("Весь список:")
print_all()

update_q(1, 100)
update_p(2, 55.5)
delete_by_id(14)

print("\nПосле изменений:")
print_all()

print("\nФильтр (цена < 100 и кол-во > 5):")
filter_data()

print("\nПоиск 'мыло':")
find_by_title('мыло')