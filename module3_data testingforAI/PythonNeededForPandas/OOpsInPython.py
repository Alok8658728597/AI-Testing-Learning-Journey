# 🧱 Object-Oriented Programming (OOP) in Python – Reviewed & Expanded

"""
Object-Oriented Programming is a way to structure code using classes and objects. 
It helps organize logic, especially when working with data models, test cases, or reusable components.
"""

# ✅ 1. Class – Blueprint for Objects
# A class defines attributes and behaviors.
# Think of a class like a template.

# Without __init__ constructor method
class Pen:
    color = "Black"

my_pen = Pen()
print(my_pen.color)  # Output: Black

# With __init__ constructor method
class Pen:
    def __init__(self, color):
        self.color = color

penColor = Pen("Blue")
print(penColor.color)  # Output: Blue

# Adding a method to perform an action
class Pen:
    def __init__(self, color):
        self.color = color

    def write(self, text):
        print(f"Write '{text}' with {self.color} pen")

my_pen = Pen("Red")
my_pen.write("Paragraph")  # Output: Write 'Paragraph' with Red pen

# ✅ 2. Another Example – Mobile Phone
class Mobile:
    def __init__(self, Brand, Price):
        self.Brand = Brand
        self.Price = Price

    def call(self, number):
        print(f"Calling {number} using {self.Brand} mobile")

mobile = Mobile("Nokia A14", 23455)
mobile.call(8678567834)  # Output: Calling 8678567834 using Nokia A14 mobile

# ✅ 3. Important OOP Concepts in Python
"""
class        : Blueprint for creating objects
object       : Instance of a class
__init__     : Constructor method to initialize object attributes
self         : Refers to the current object instance
method       : Function inside a class that defines behavior
attribute    : Variable inside a class or object
encapsulation: Hiding internal details (can be done using private variables)
inheritance  : One class can inherit properties from another
polymorphism : Same method name can behave differently in different classes
"""

# ✅ 4. Tricky & Revision-Friendly Points
"""
- self is mandatory in method definitions to access instance variables.
- __init__ is not a keyword, it's a special method name.
- You can create multiple objects from the same class.
- Class variables are shared across all objects; instance variables are unique.
- Methods must always have 'self' as the first parameter.
- You can define default values in __init__ using: def __init__(self, color="Black")
- You can override methods in child classes using inheritance.
- Use dir(object) to inspect available methods and attributes.
"""

# ✅ 5. Why OOP is Useful in AI Testing
"""
- Helps organize test logic into reusable components.
- Makes it easier to manage test data and validation.
- Can be combined with Pandas to read test cases from CSV and run them using class methods.
"""
