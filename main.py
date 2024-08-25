# class Car: #mercedes, Toyota

#     def __init__(self, car_name, car_price, car_year, car_color):#
#         self.name = car_name # e.g in this case self is car1, so car1.name = "mercedes", car2.name = "Toyota", car3.name = "Ford"
#         self.price = car_price #self in this point refers to car1 and car2
#         self.year = car_year
#         self.color = car_color #self means current object
#         self.odometer_reading = 0# hard coded
    
# car1 = Car("mercedes", 2500, 2016, "green")
# car2 = Car("Toyota", 3000, 2017, "red")
# car3 = Car("Ford", 4000, 2020, "brown")
# pass

# class House:
#     def 

#     pass #means its an empty class

# class Phone: #Samsung, Tecno
#     pass

class employees:
    def __init__(self, p_name, p_age, PID, p_phone):
        self.name = p_name #p_name is value
        self.age = p_age #p_age is value
        self.id = PID #PID is value
        self.phone = p_phone
#in addition to attributes, objects have behaviours i.e click, song, dance, jump, sleep, wave, sit, dance
    def open_computers(self, type): #this is a method i.e. behaviours of employees i.e, action an employee can perform
        #logic i.e methods represents behaviours in code
        # a function can only be a method if its assocated with an object (self)
        pass

    def create_folder(self, folder_name):
        command = f"mkdir {folder_name}"
        print(command)
        print(f"{self.employee_name} is dancing")

employee1 = employees("Quetta", 28, 105, 100)
employee2 = employees("Patrick", 30, 106, 524)
employee3 = employees("Hannah", 26, 254, 144)
employee4 = employees("Auxilia", 23, 200, 534)
employee5 = employees("Eliyah", 21, 444, 522)
employee6 = employees("Charchil", 20, 700, 333)
employee7 = employees("Betty", 19, 444, 500)
employee8 = employees("Lilian", 22, 800, 377)
employee9 = employees("Ita", 25, 888, 300)

#a parameter can only be an attribute if it is attached to an object i.e. self



# class learners:
#     def __init__(self, name, cohort, tech, average_score):
#         self.name = name
#         self.track = tech
    
# leaner1 = learners("Kelvin Sibuta", "BE")#arguments are name, cohort, tech, average_score
# pass
#     pass

# class laboratory:
#     pass

# class Laptops:
#     pass

# class students:
#     pass

# class PC:
#     def __init__(self, name, price, RAM, Memory, storage, color type, speaker type, keyboard):

#         pass