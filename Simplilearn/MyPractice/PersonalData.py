# Function for basic mathematical operation
def add_numbers(a, b):
    return a + b

def greet(name,age=25,gender="Not Specified"):
    return f"Hello, {name}! You are {age} years old. and gender is {gender}"

def math_operations(x, y):
    return {
        "sum": x + y,
        "difference": x - y,
        "product": x * y,
        "quotient": x / y if y != 0 else None
    }

print(add_numbers(5, 10))
print(greet("Alice","30","Female"))
print(math_operations(20, 4))

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"My name is {self.name} and I am {self.age} years old."
    
person1 = Person("Bob", 28)
print(person1.introduce())

class PersonalDetails(Person):
    def __init__(self,name,age,phone):
        super().__init__(name, age)
        self.phone = phone

    def display_personal_details(self):
        parent_details = self.introduce()
        return f"{parent_details} My phone number is {self.phone}."
    
person2 = PersonalDetails("John", 30, "123-456-7890")
print(person2.display_personal_details())
