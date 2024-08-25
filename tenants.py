class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self): #object's (person's) behaviour
        return f"I can walk"
    def __str__(self):#represents object entirity, pass all the attributes from the class
        return f"{self.name} {self.age}"#represents object with all its attributes from the class
    
person1 = Person("Kelvin", 28) #object1
print(person1.walk())
print(person1.name)
print(person1.age)

#Inheritance
class Tenant(Person):
    def __init__(self, name, age, tenant_id): #constructs the object from the class
        super().__init__(name, age)# calls the parent constructor, passing the params of attributes we wanna inherit from our parent
        self.tenantID = tenant_id
        self.house = []

    def rent(self, house):
        self.house.append(house)
        return f"{self.name} rent in {self.house}"

    def __str__(self):
        return f"{self.name} {self.age} {self.walk()}"

# tenant1 = Tenant("Kelvin", 30, 2)
# print(tenant1.rent("Flat"))
# print(tenant1.rent("single"))
# print(tenant1.age)
# #print(tenant1.ten)
# print(tenant1.walk())

class Male(Tenant):
    def __init__(self, name, age, tenant_id, major): #conector        super().__init__(name, age, tenant_id)
        self.major = major

    def rent(self, house):
        if len(self.house) < 2:
            return super().rent(house)
        else:
            return f"Cannot rent {self.name} in {self.house}"
    
    def __str__(self):
        return f"{self.name} {self.age} {self.major}"
    
Man1 = Male("Quetta", 17, 3, "Immunology")
# print(Man1)
# print(Man1.rent("Single"))
# print(Man1.rent("Bungalo"))
# print(Man1.rent("Double"))
def new_tenants(tenant, house):
    return tenant.rent(house)

letting = new_tenants(Man1, "Luhya")
print(letting)