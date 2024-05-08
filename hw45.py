import sqlite3

class Task:
    def _init_(self, db_name='tasks.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS tasks (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                title TEXT,
                                description TEXT,
                                completed BOOLEAN DEFAULT 0
                            )''')
        self.conn.commit()

    def add_task(self, title, description):
        self.cursor.execute('INSERT INTO tasks (title, description) VALUES ()', (title, description))
        self.conn.commit()

    def edit_task(self, task_id):
        self.cursor.execute('UPDATE tasks SET completed =  WHERE id = ', (True, task_id))
        self.conn.commit()

    def view_tasks(self):
        self.cursor.execute('SELECT * FROM tasks')
        task = self.cursor.fetchall()
        for task in task:
            print(task)

if __name__== "_main_":
    manager = Task()
    manager.add_task("Покупки", "Купить молоко")
    manager.add_task("Уборка", "Пылесосить дом")
    manager.edit_task(1)
    manager.view_tasks()