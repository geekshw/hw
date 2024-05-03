
class MagicCalculator:
    def _init_(self, number_1, number_2):
        self.number_1 = number_1
        self.number_2 = number_2
    
    def _add_(self, other):
        return self.number_1 + other.number_1, self.number_2 + other.number_2
    
    def _sub_(self, other):
        return self.number_1 - other.number_1, self.number_2 - other.number_2
    
    def _mul_(self, other):
        return self.number_1 * other.number_1, self.number_2 * other.number_2
    
    def _truediv_(self, other):
        return self.number_1 / other.number_1, self.number_2 / other.number_2
    
    def _floordiv_(self, other):
        return self.number_1 // other.number_1, self.number_2 // other.number_2

class Book:
    def _init_(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    
    def _lt_(self, other):
        return self.year < other.year
    
    def _le_(self, other):
        return self.year <= other.year
    
    def _gt_(self, other):
        return self.year > other.year
    
    def _ge_(self, other):
        return self.year >= other.year
    
    def _eq_(self, other):
        return self.year == other.year
    
    def _str_(self):
        return f"Title:{self.title}, Author:{self.author}, Year:{self.year}"