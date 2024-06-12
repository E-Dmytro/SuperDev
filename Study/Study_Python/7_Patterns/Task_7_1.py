from abc import ABC, abstractmethod

class Product(ABC):

    @abstractmethod
    def cook(self):
        pass

class FettucineAlfredo(Product):
    name = "Fettuccine Alfredo"
    def cook(self):
        print("Italian main course prepared:"+self.name)

class Tiramisu(Product):
    name = "Tiramisu"
    def cook(self):
        print("Italian dessert prepared: "+self.name)

class DuckALOrange(Product):
    name = "Duck A L'Orange"
    def cook(self):
        print("French main course prepared:")

class CremeBrulee(Product):
    name = "Creme bulee"
    def cook(self):
        print("Frnch dessert prepared: "+self.name)

class Factory(ABC):

    @abstractmethod
    def get_dish(type_of_meal):
        pass

class ItaliaDishesFactory(Factory):
    def get_dish(type_of_meal):
        if type_of_meal == "main":
            return FettucineAlfredo()
        if type_of_meal == "dessert":
            return Tiramisu()

    def crete_dessert(self):
        return Tiramisu()

class FrenchDishesFactory():
    def get_dish(type_of_meal):
        if type_of_meal == "main":
            return DuckALOrange()

        if type_of_meal == "dessert":
            return CremeBrulee()

class FactoryProducer:
    def get_factory(self,type_of_factory):
        if type_of_factory == "italian":
            return ItaliaDishesFactory
        if type_of_factory == "french":
            return FrenchDishesFactory