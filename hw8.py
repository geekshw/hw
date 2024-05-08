import sqlite3
connect = sqlite3.connect('bank.db')
cursor = connect.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS accounts( 
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
             first_name TEXT, 
             last_name TEXT, 
             age INTEGER, 
             address TEXT, 
             email TEXT, 
             balance REAL)''')

class BankAccount:
    def _init_(self, first_name, last_name, age, address, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.address = address
        self.email = email
        self.balance = 0
        cursor.execute("INSERT INTO accounts (first_name, last_name, age, address, email, balance) VALUES (?, ?, ?, ?, ?, ?)", (self.first_name, self.last_name, self.age, self.address, self.email, self.balance))
        connect.commit()
    
    def deposit(self, amount):
        self.balance += amount
        cursor.execute("UPDATE accounts SET balance=? WHERE id=?", (self.balance, self.id))
        connect.commit()
        return f"Сумма {amount} успешно зачислена на ваш счет. Текущий баланс: {self.balance}"
    
    def withdraw(self, amount):
        if amount > self.balance:
            return "Недостаточно средств на счете."
        else:
            self.balance = amount
            cursor.execute("UPDATE accounts SET balance=? WHERE id=?", (self.balance, self.id))
            connect.commit()
            return f"Сумма {amount} успешно списана со счета. Текущий баланс: {self.balance}"
    
    def check_balance(self):
        return f"Текущий баланс на вашем"
user_account = BankAccount("Alihan", "Abidov", 14, "Масалиева", "alihan@gmail.com")
print(user_account.deposit(1000)) 
print(user_account.check_balance())
print(user_account.withdraw(500))
print(user_account.check_balance())
print(user_account.withdraw(1000)) 