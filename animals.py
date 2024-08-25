class Animal:

    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Lion(Animal):

    def speak(self):
        return f"{self.name} the lion roars"
    
    # def __init__(self, name):
    #     super().__init__(name)

class Elephant(Animal):
    def speak(self):
        return f"{self.name} the elephant trumpet"
    
#Polymorphism
Zoo = [
    Lion("Simba"),
    Elephant("Ndovu")
]

for animal in Zoo:
    print(animal.speak())