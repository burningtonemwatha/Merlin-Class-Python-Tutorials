# One object references another - one to one relationship

class Driver:
    def __init__(self, name):
        self.name = name

class Car:
    def __init__(self, model):
        self.model = model

    def assign_driver(self, driver):
        # Driver references an actual object
        self.driver = driver # Association
        print(f"{driver.name} is now driving {self.model}")


driver1 = Driver("Mwatha")
driver2 = Driver("Leyna")
car1 = Car("the Cardillac")
car2 = Car("the Porsche")
car1.assign_driver(driver1)
car2.assign_driver(driver2)

