import sqlite3

def create_table(connection):
    connection.execute("""
    CREATE TABLE IF NOT EXISTS books (
        book_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        author TEXT,
        publication_year INTEGER,
        genre TEXT,
        number_of_pages INTEGER,
        number_of_copies INTEGER
    )
    """)
    connection.commit()

def insert_book(connection, name, author, year, genre, pages, copies):
    connection.execute("""
    INSERT INTO books
    (name, author, publication_year, genre, number_of_pages, number_of_copies)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (name, author, year, genre, pages, copies))
    connection.commit()

if __name__ == "__main__":
    conn = sqlite3.connect("library.db")
    create_table(conn)

    insert_book(conn, "Sapiens", "Юваль Ной Харари", 2011, "История", 512, 5)
    insert_book(conn, "Братья Карамазовы", "Фёдор Достоевский", 1880, "Роман", 824, 3)
    insert_book(conn, "Левиафан", "Томас Гоббс", 1651, "Философия", 736, 2)
    insert_book(conn, "Код", "Чарльз Петцольд", 1999, "Программирование", 400, 4)
    insert_book(conn, "Политика", "Аристотель", -350, "Философия", 350, 2)
    insert_book(conn, "Государь", "Никколо Макиавелли", 1532, "Политическая философия", 160, 3)
    insert_book(conn, "Бесы", "Фёдор Достоевский", 1872, "Роман", 768, 2)
    insert_book(conn, "Логика", "Аристотель", -330, "Философия", 300, 2)
    insert_book(conn, "Моя борьба", "Адольф Гитлер", 1925, "Политика", 720, 1)
    insert_book(conn, "Преступный человек", "Чезаре Ломброзо", 1876, "Криминология", 560, 2)