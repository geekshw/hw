import sqlite3

connect = sqlite3.connect("desc.db")
connect.cursor()

class ZAmetki:
    def __init__(self,desc,title) :
        self.desc = desc
        self.title = title
        self.completed = False  
        

        



