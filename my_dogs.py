class Dog:
    def __init__(self, name, age, breed):# init method takes in attributes
        self.name = name
        self.age = age
        self.breed = breed
    
    def bark(self): #this is a method, it describes the dog's behaviours
        return f"{self.name} says woof!"
    
    def celebrate_birthday(self):
        self.age += 1
        return f"Happy {self.age}th bithday, {self.name}!"
    def brak(self):
        return "Woof"
    
#Object Creation  
my_dog1 = Dog("Buddy", 5, "Golden Retriever")
my_dog2 = Dog("Max", 3, "German Shepherd")
print(my_dog1.bark())
print(my_dog1.celebrate_birthday())
print(my_dog2.celebrate_birthday())

#Accessing object Properties and Methods
print(f"{my_dog1} is a {my_dog1.breed}. He says {my_dog1.brak()}")
print(f"{my_dog2} is a {my_dog2.breed}. He says {my_dog2.brak()}")