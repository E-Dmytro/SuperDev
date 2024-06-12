
print('rectangle \ntriangle \ncircle')
enter_ch=input("Enter which square you want to find (rectangle,triangle,circle) - ")
import math

def square_r(a,b):
    return a * b
def square_tr(a,h):
    return (a * h)/2
def square_cr(r):
    return math.pi*(r**2)

if enter_ch==("rectangle"):
    a = int(input(" side a = "))
    b = int(input("side b = "))
    print('Square of rectangle =',square_r(),'m')
elif enter_ch==("circle"):
    r = int(input(" radius r = "))
    print('Square of circle =',square_cr(r),'m')
elif enter_ch == ("triangle"):
    a = int(input(" leg a = "))
    b = int(input("height h = "))
    print('Square of triangle =', square_tr(), 'm')
