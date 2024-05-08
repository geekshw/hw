import sqlite3

connect = sqlite3.connect("Geeks.db")
cursor = connect.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               full_name VARCHAR(20) NOT NULL,
               hobby TEXT DEFAULT NULL,
               phone_number INTEGER NOT NULL DEFAULT 996,
               birth_date DATE,
               mark DOUBLE(7, 3) DEFAULT 0.0,
               agreement BOOLEAN DEFAULT FALSE
)
""")

class Geeks:
    def __init__(self):
        self.full_name = None
        self.hobby = None
        self.phone_number = 0
        self.birth_date = None
        self.mark = 0.0
        self.agreement = False

    def register(self, full_name, hobby, phone_number, birth_date):
        self.full_name = full_name
        self.hobby = hobby
        self.phone_number = phone_number
        self.birth_date = birth_date
        cursor.execute(f"""INSERT INTO students (full_name, hobby, phone_number, birth_date)
                       VALUES ('{full_name}', '{hobby}', {phone_number}, '{birth_date}')""")

        cursor.execute("""INSERT INTO students (full_name, hobby, phone_number, birth_date)
                       VALUES (?, ?, ?, ?)""", (full_name, hobby, phone_number, birth_date))
        
        connect.commit()

geeks_students = Geeks()
geeks_students.register("Abdykadyrov Syimyk", "coding", 771244745, "07-08-2005")