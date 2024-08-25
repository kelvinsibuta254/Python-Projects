try:
    f = open("cars.txt")
    # if f.name == "cars.txt":
    #     raise Exception
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print("Error!")
else: 
    print(f.read())
    f.close()
finally: #when working with databases
    print("Executing Finally")