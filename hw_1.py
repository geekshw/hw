# class Fruit:

#   def __init__(self, name, color, weight):
#     self.name = name
#     self.color = color
#     self.weight = weight

#   def info(self):
#     print(f"ЭТО {self.name} И ОНО {self.color} И ВЕСИТ {self.weight} ГРАММ.")


# apple = Fruit("яблоко", "красное", 100)
# banana = Fruit("персик", "оранжевое", 120)
# orange = Fruit("баклажан", "фиолетовое", 150)

# apple.info()
# banana.info()
# orange.info()


# Задача 2+3
# class Car:
#     def __init__(self, model, year, color):
#         self.model = model
#         self.year = year
#         self.color = color
#         self.fuel = 0

#     def refuel(self, liters):
#         if liters <= 40:
#             self.fuel += liters
#             print(f"Бак пополнен на {liters} литров. Текущий уровень топлива: {self.fuel} л.")
#         else:
#             print("Вы не можете заправить бак на более чем 40 литров.")

#     def drive(self, city, distance):
#         fuel_needed = distance / 10
#         if fuel_needed <= self.fuel:
#             self.fuel -= fuel_needed
#             print(f"Машина - {self.model} едет в {city}. Остаток топлива: {self.fuel} л.")
#         else:
#             distance = self.fuel * 10
#             print(f"Машина не сможет доехать до {city}. Максимальное расстояние, которое может проехать: {distance} км.")

# my_car = Car("Toyota Camry", 2022, "черный")
# my_car.refuel(40)
# my_car.drive("Ош", 300)










