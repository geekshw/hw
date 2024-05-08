class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory
        
    @property
    def cpu(self):
        return self.__cpu
    
    @property
    def memory(self):
        return self.__memory
    
    def __make_computations(self):
        print(f"""Результат сложения : {self.cpu + self.memory},
              Результат вычитания : {self.cpu - self.memory},
              Результат деления : {self.cpu / self.memory},
              Результат умножения : {self.cpu * self.memory}""")
        
    @property
    def make_computations(self):
        return self.__make_computations
    
ae = Computer(182, 831)
ae.make_computations()
    
class Laptop(Computer):
    def __init__(self, cpu, memory, memory_card):
        Computer.__init__(self, cpu, memory)
        self.__memory_card = memory_card
        
    @property
    def memory_card(self):
        return self.__memory_card
    
    def info(self):
        print(f"Ваш процессор:  {self.cpu}, память : {self.memory}, карта памяти : {self.memory_card} ")
        
o = Laptop(2564, 2456, 2456)
o.make_computations()
o.info()