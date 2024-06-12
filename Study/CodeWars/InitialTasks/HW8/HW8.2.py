class Human:
    species = "Homosapiens"

    def __init__(self,name):
        self.name=name

    def welcome_messege(self):
        print(f"Welcome {self.name} !!!")

    @classmethod
    def return_species(cls):
        return cls.species

    @staticmethod
    def arbitraty_messege():
        messege=input(f"Enter your messege to = ")
        print(f"Messege is {messege}")

Donatello=Human("Donatello")
Donatello.welcome_messege()
print(f"{Donatello.name}s species is, " , Donatello.return_species())
Donatello.arbitraty_messege()


