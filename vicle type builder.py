# Parent class
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def info(self):
        print("This is a vehicle.")

# Child class
class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)   # Use super()
        self.model = model

    # Method overriding
    def info(self):
        print("Car Brand:", self.brand)
        print("Car Model:", self.model)

# Create object
c = Car("Toyota", "Corolla")

# Call overridden method
c.info()

# Check inheritance
print("Is Car subclass of Vehicle?", issubclass(Car, Vehicle))