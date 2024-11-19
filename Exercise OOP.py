class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name, self.age)


Via = Person("Davit", "33")
Via.display()


class Student(Person):
    def showStudent(self):
        print("This is information the Student")


Student_object = Student("Gayane", "30")
Student_object.display()
Student_object.showStudent()
