# Задача 1+2+3+1+2
# class Person:
#     def __init__(self, fullname, age, is_married):
#         self.fullname = fullname
#         self.age = age
#         self.is_married = is_married

#     def introduce_myself(self):
#         print(f"Меня зовут {self.fullname}. Мне {self.age} лет. Я {'женат' if self.is_married else 'замужем'}.")

# class Teacher(Person):
#     salary = 0

#     def __init__(self, fullname, age, is_married, experience):
#         super().__init__(fullname, age, is_married)
#         self.experience = experience

#     def introduce_myself(self):
#         super().introduce_myself()
#         print(f"У меня {self.experience} лет опыта убийство .")

#     def calculate_salary(self):
#         bonus = self.experience * 3000
#         total_salary = self.salary + bonus
#         return total_salary

# teacher1 = Teacher("Джон Уик", 40, True, 20)
# teacher1.salary = 50000
# teacher1.introduce_myself()
# print("Зарплата киллера :", teacher1.calculate_salary())

# teacher2 = Teacher("Хелен Уик", 35, False, 10)
# teacher2.salary = 60000
# teacher2.introduce_myself()
# print("Зарплата киллера:", teacher2.calculate_salary())


# Доп.задача 3
# class Teacher:
#     def __init__(self, name, subject, hourly_rate, hours_worked):
#         self.name = name
#         self.subject = subject
#         self.hourly_rate = hourly_rate
#         self.hours_worked = hours_worked

#     def info(self):
#         print(f"Учитель {self.name} преподает  {self.subject}. Он работает по {self.hours_worked} часа в день.")

#     def calculate_salary(self):
#         salary = self.hourly_rate * self.hours_worked
#         return salary


# teacher = Teacher("Сыймык Абдыкадыров", "IT програмирования", 300, 3)


# teacher.info()


# print(f"Примерная зарплата учителя: {teacher.calculate_salary()} евро.")




    