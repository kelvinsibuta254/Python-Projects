#Classes and Objects
#Inheritance
#Polymorphisms
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        pass
#inheritance
class Lion(Animal):# inherits from Parent class (Animal)
    def speak(self):
        return f"{self.name} the lion roars"
    
class Elephant(Animal):
    def speak(self):
        return f"{self.name} the elephant trumpets"

#Polymorphism
zoo = [
    Lion("Simba"),
    Elephant("Ndovu")
]

for animal in zoo:
    print(animal.speak())


