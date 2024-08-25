class Dog:

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def brak(self):
        return "Woof"
    
#Object Creation
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Max", "Germany Shepherd")

#Accessing Object Properties and Methods
print(f"{dog1.name} is a {dog1.breed}. He says {dog1.brak()}")
print(f"{dog2.name} is a {dog2.breed}. He says {dog2.brak()}")