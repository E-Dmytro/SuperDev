class Car:
    def __init__(self,name,kind,model):
        self.name=name
        self.kind=kind
        self.model=model
    def startcar(self):
        print(f"Car of {self.name} was started")
    def stopcar (self):
        print(f"Car of {self.name} was started")


t1=Car("Audi","A","6")
t1.startcar()
t2=Car("Lamborghini","Huracan","EVO")
t2.stopcar()

# def inputNameModelKind(self):
#     self.name=[input(f"Enter name car --")]
#     self.kind = [input(f"Enter name kind --")]
#     self.model = [input(f"Enter name model --")]
# def dispNameModelKind(self):
#     print(f"Name car -- {self.name} ")
#     print(f"Kind car -- {self.kind} ")
#     print(f"Model car -- {self.model} ")