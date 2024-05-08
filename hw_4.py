# 1
class People():
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
    def __str__(self):
        pass
class Geeks(People):
    def __str__(self):
        return f"Name: {self.name}, Email: {self.email}, Phone: {self.phone}"
geek = Geeks("John Doe", "john@example.com", "123-456-7890")
print(geek)
# 2
class People():
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
    def __str__(self):
        pass

class Student(People):
    def __init__(self, name, email, phone, student_id):
        super().__init__(name, email, phone)
        self.student_id = student_id

    def __str__(self):
        return f"Student: {self.name}, Email: {self.email}, Phone: {self.phone}, Student ID: {self.student_id}"

    def study(self):
        print(f"{self.name} is studying.")

class Teacher(People):
    def __init__(self, name, email, phone, subject):
        super().__init__(name, email, phone)
        self.subject = subject

    def __str__(self):
        return f"Teacher: {self.name}, Email: {self.email}, Phone: {self.phone}, Subject: {self.subject}"

    def teach(self):
        print(f"{self.name} is teaching {self.subject}.")

class Admin(People):
    def __init__(self, name, email, phone, role):
        super().__init__(name, email, phone)
        self.role = role

    def __str__(self):
        return f"Admin: {self.name}, Email: {self.email}, Phone: {self.phone}, Role: {self.role}"

    def manage(self):
        print(f"{self.name} is managing as {self.role}.")
student = Student("Alice", "alice@example.com", "1234567890", "S12345")
teacher = Teacher("Bob", "bob@example.com", "9876543210", "Math")
admin = Admin("Charlie", "charlie@example.com", "5555555555", "System Admin")

print(student)
print(teacher)
print(admin)

student.study()
teacher.teach()
admin.manage()
# 3
class People():
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
    def __str__(self):
        pass

class Student(People):
    def __init__(self, name, email, phone, student_id, group_where_study):
        super().__init__(name, email, phone)
        self.student_id = student_id
        self.group_where_study = group_where_study

    def __str__(self):
        return f"Student: {self.name}, Email: {self.email}, Phone: {self.phone}, Student ID: {self.student_id}, Group: {self.group_where_study}"

    def study(self):
        print(f"{self.name} is studying in group {self.group_where_study}.")

student = Student("Alice", "alice@example.com", "1234567890", "S12345", "Group A")

print(student)
student.study()
# 4
class People():
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
    def __str__(self):
        pass

class Teacher(People):
    def __init__(self, name, email, phone, teacher_id, group_where_teach):
        super().__init__(name, email, phone)
        self.teacher_id = teacher_id
        self.group_where_teach = group_where_teach

    def __str__(self):
        return f"Teacher: {self.name}, Email: {self.email}, Phone: {self.phone}, Teacher ID: {self.teacher_id}, Teaching Group: {self.group_where_teach}"

    def teach(self):
        print(f"{self.name} is teaching in group {self.group_where_teach}.")

teacher = Teacher("Bob", "bob@example.com", "987-6543210", "T98765", "Group B")

print(teacher)
teacher.teach()
# 5
class People():
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
    def __str__(self):
        pass

class Admin(People):
    def __init__(self, name, email, phone, admin_id):
        super().__init__(name, email, phone)
        self.admin_id = admin_id

    def __str__(self):
        return f"Admin: {self.name}, Email: {self.email}, Phone: {self.phone}, Admin ID: {self.admin_id}"

    def create_group(self, group_name):
        print(f"{self.name} created a new group: {group_name}")

admin = Admin("Charlie", "charlie@example.com", "555-555-5555", "A123")

print(admin)
admin.create_group("Group X")
# 
class Mentor(student, teacher):
    def __init__(self, name, email, phone, student_id, group_where_study, teacher_id, group_where_teach):
        student.__init__(self, name, email, phone, student_id, group_where_study)
        teacher.__init__(self, name, email, phone, teacher_id, group_where_teach)

    def __str__(self):
        return f"Mentor: {self.name}, Email: {self.email}, Phone: {self.phone}, Student ID: {self.student_id}, Teaching Group: {self.group_where_teach}, Teacher ID: {self.teacher_id}, Studying Group: {self.group_where_study}"


mentor = Mentor("Mentor Name", "mentor@example.com", "123-456-7890", "S123", "Group A", "T456", "Group B")

print(mentor)
mentor.study()  
mentor.teach()  
# 7
class Mentor(Student, Teacher):
    def __init__(self, name, email, phone, student_id, group_where_study, teacher_id, group_where_teach):
        Student.__init__(self, name, email, phone, student_id, group_where_study)
        Teacher.__init__(self, name, email, phone, teacher_id, group_where_teach)

    def __str__(self):
        return f"Mentor: {self.name}, Email: {self.email}, Phone: {self.phone}, Student ID: {self.student_id}, Group: {self.group_where_study}, Teacher ID: {self.teacher_id}, Teaching Group: {self.group_where_teach}"

student = Student("Alice", "alice@example.com", "123-456-7890", "S12345", "Group A")
teacher = Teacher("Bob", "bob@example.com", "987-654-3210", "T98765", "Group B")
mentor = Mentor("Charlie", "charlie@example.com", "555555ф  5555", "S99999", "Group C", "T55555", "Group D")

print(student)
student.study()

print(teacher)
teacher.teach()

print(mentor)
mentor.study()  
mentor.teach()  

