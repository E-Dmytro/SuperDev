import Calc
symbol=input("Enter symbol - ")
a=float(input("Enter parameter a = "))
b=float(input("Enter parameter b = "))
if symbol=="-":
    print(f'Result = {Calc.substract(a,b)}')
if symbol=="+":
    print(f'Result = {Calc.addition(a, b)}')
if symbol=="*":
    print(f'Result = {Calc.multiplication(a,b)}')
if symbol=="/":
    print(f'Result = {Calc.substract(a, b)}')
