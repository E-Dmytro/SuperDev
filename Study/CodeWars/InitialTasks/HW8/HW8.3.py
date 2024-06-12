class Employee:
    """
        The Employee.
    Salary and name employee"""
    counter=0

    def __init__(self,name,salary):
        Employee.counter+=1
        self.name=name
        self.salary=salary

    @classmethod
    def get_counter(cls):
        return cls.counter

    def name_salary_employee(self):
        print(f'Name {self.name} \n'
              f'Salary {self.salary}')



Donatello=Employee("Donatello",89782)
Donatello.name_salary_employee()
Raphael=Employee("Raphael",79782)
Raphael.name_salary_employee()
Leonardo=Employee("Leonardo",69782)
Leonardo.name_salary_employee()
Michelangelo=Employee("Michelangelo",99782)
Michelangelo.name_salary_employee()
print(f"Count of employees {Employee.counter}")
print(f"The employee class is inherited from {Employee.__base__}")
print(f"the class namespace is {Employee.__dict__}")
print(f"the class name is {Employee.__name__}")
print(f"the module name in which the class is defined {Employee.__module__}")
print(f"The documentation bar is {Employee.__doc__}")
