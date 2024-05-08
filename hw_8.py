import sqlite3

connect = sqlite3.connect("mbank.db")
cursor = connect.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS clients(
                id INT PRIMARY KEY,
                full_name VARCHAR(60) NOT NULL,
                surname VARCHAR(60) NOT NULL,
                age DEFAULT(20) NOT NULL,
                adress TEXT NOT NUL,
                email TEXT NOT NULL, 
                group DEFAULT (15,16), 
                study DEFAULT(2,3),
                balance DOUBLR(7,2) DEFAULT 0.0, 
)
""")
class Mentor:
    def __init__ (self):
        self.full_name = None
        self.surname = None
        self.age = None
        self.adress = None
        self.email = None 
        self.group = None
        self.study = None
        self.balance = 0
    def register(self , full_name , surname , age , adress , email , group , study):
           self.full_name = full_name
           self.surname = surname
           self.age = age
           self.adress = adress
           self.email = email
           self.group = group
           self.study = study
           cursor.execute(f"""INSERT INTO clients(full_name , email , phone_number , birth_date , pol , balance)
                    VALUES('{full_name}' , '{surname}' , '{age}' , '{adress}' , '{email}' , '{group}' , '{study}' , 0.0)""")            
    def plus(self , amount):
        cursor.execute(f"UPDATE clients SET balance = + {amount} WHERE email = '{self.email}'")
        connect.commit()
        self.balance += amount

    def minus(self , amount):
        cursor.execute(f"UPDATE clients SET balance = - {amount} WHERE email = '{self.email}'")
        connect.commit()
        self.balance -= amount
    def __str__(self):
        return f"Ваш баланс {self.balance}"    
    def main(self):
        while True:
            print("Выберите дейсвие:")
            print("0-Выйти , 1-Регистрации , 2-Пополнить баланс , 3-снятие денег , 4-просмотр баланса")
            command = int(input("Введите цифру:"))
            if command == 0:
                break
            elif command == 1:
                full_name = input("Введите свое полное имя") 
                surname = input("Введите свою фамилию")            
                age = input("ВВедите свой возраст") 
                adress = input("Введите свой адрес") 
                email = input("Введите свой email ") 
                group = input("Введите свою группу") 
                study = input("Введите свою группу обучения")  
                self.register(full_name , surname , age , adress , email , group , study)
            elif command == 2:
                amount = int(input("Введите сумму для пополнения коинов "))

                self.plus(amount)
            elif command == 3:
                amount = int(input("Введите сумму снятия коинов"))
            elif command == 4:
                print(self.balance)        