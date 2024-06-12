import HW7
print('1. rectangle \n2. triangle \n3. circle')
enter_ch=input("Enter which square you want to find (rectangle,triangle,circle) - ")


if enter_ch==("1"):
    a = int(input(" side a = "))
    b = int(input(" side b = "))
    print(f'Square of rectangle = {HW7.square_r(a,b)} m')
elif enter_ch == ("2"):
    a = int(input(" leg a = "))
    b = int(input("height h = "))
    print(f"Square of triangle = {HW7.square_tr(a,h)} m")
elif enter_ch==("3"):
    r = int(input(" radius r = "))
    print(f"Square of circle = {HW7.square_cr(r)} m")

