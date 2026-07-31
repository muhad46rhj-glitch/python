#creat a class name pet
class pet:
    def __init__(self,name,animal,age,colour):
        self.name = name
        self.age = age
        self.animal = animal
        self.colour = colour
ob = pet("tommy","dog",12,"black")
ob1 = pet("cutypie","cat",7,"white") 
ob2 = pet("greeny","parrot",2,"green") 
print(ob.name,ob.animal,ob.age,ob.colour)
print(ob1.name,ob1.animal,ob1.age,ob1.colour)
print(ob2.name,ob2.animal,ob2.age,ob2.colour)