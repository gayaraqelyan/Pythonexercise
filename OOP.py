# Write a Python program to create a Vehicle class with max_speed and mileage attributes.
# class Vehicle:
#   def __init__(self, max_speed, mileage):
#        self.max_speed = max_speed
#        self.mileage = mileage

#    def show(self):
#        print(f"School Bus mileage:{self.mileage} ")
#        print(f"School Bus max_speed:{self.max_speed}")


# SchoolBus = Vehicle("90 km/h", "10 km/l")
# Motorcycle = Vehicle("605 kmk/h", "30000 km/l")
# SchoolBus.show()
# Motorcycle.show()

# print("School Bus max_speed:", SchoolBus.max_speed, "School Bus mileage ", SchoolBus.mileage)
# print("Motorcycle max_speed:", Motorcycle.max_speed, "Motorcycle mileage:", Motorcycle.mileage)

# ----------------------------------------------------------------------------------------------------------------------
# Inheritance in Python

# class Person:
#     def __init__(self, id, name):
#        self.id = id
#        self.name = name

#    def show(self):
#        print(self.id, self.name)


# epm = Person("103", "Vazgen")
# epm.show()


# class Emp(Person):
#     def display(self):
#        print("Employment")


# Emp_detail = Emp("106", "Saro")
# Emp_detail.show()
# Emp_detail.display()

# ----------------------------------------------------------------------------------------------------------------------
# Single inheritance

# Create a Python class Person with attributes:name and age of type string:

# class Person:
#    def __init__(self, name, age):
# self.name = name
#        self.age = age

# Create a display() method that displays the name and age of an object created via the Person class.

#   def display(self):
#       print(self.name, self.age)


# Emp = Person("Vazgen", "23")
# Emp.display()


# Create a child class Student which inherits from the Person class and which also has a section attribute

# class Student(Person):

# Create a method displayStudent() that displays the name , age and section of an object created via the Student class
#     def displayStudent(self):
#        print("This is a Student information")


# Create a student object via an information on the Student class and then test the displayStudent method .

# disStudent = Student("Armen", "18")
# disStudent.displayStudent()
# disStudent.display()


# -----------------------------------------------------------------------------------------------------------------------
# Write a Rectangle class in Python language,allowing you to build a rectangle with length and width attributes.

# class Rectangle:
#    def __init__(self, length, width):
#        self.length = length
#        self.width = width

# Create a Perimater() method to calculate the perimater of the rectangle and a Area() method to calculate the area of
# the rectangle.

#  def Perimater(self):
#      return 2 * (self.length + self.width)


#  def Area(self):
#      return self.length * self.width

# Create a method display() that display the length,width ,perimater and area of an created using an instantiation or
# rectangle class


#  def display(self):
#      return self.length, self.width


#  countrectangle = Rectangle(5, 5)
# print(f"Length:{countrectangle.length}")
# print(f"Wedth: {countrectangle.width}")
# print(f"Area:{countrectangle.Area()}")
# print(f"Perimater:{countrectangle.Perimater()}")

# Create a Parallelepipede child class inheriting from the Rectangle class and with a height attribute and another
# Volume() method to calculate the volume of the Parallelepipede.
# class Parallelepipede(Rectangle):
#    def __init__(self, length, width, height):
#        super().__init__(length, width)
#        self.height = height

#    def Volume(self):
#        return self.Area() * self.height


# parallelepipede = Parallelepipede(2, 5, 6)
# print(f"Length:{parallelepipede.length}")
# print(f"Width:{parallelepipede.width}")
# print(f"Heigt:{parallelepipede.height}")
# print(f"Area of base: {parallelepipede.Area}")
# print(f"Volume:{parallelepipede.Volume()}")
