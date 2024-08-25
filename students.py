class Student:
    def __init__(self, name, age, gender, year, email, phone):
        self.name = name
        self.age = age
        self.gender = gender
        self.year = year
        self.email = email
        self.phone = phone

    def eat(self):
        name = f"{self.name} eats very first"

    def __str__(self): # Encapsulation/ representation of object with all its attributes
        return f"{self.name} {self.age} {self.gender} {self.year} {self.email} {self.phone}"

student1  =Student("Kelvin", 28, "M", "Third", "kelvinsibuta254@gmail.com", "0796370516S")
print(student1)