def large_numb(numb_1,numb_2):
    '''Fuction that detects a larger number'''
    return max(numb_1,numb_2)

numb_1=int(input("Write number 1 = "))
numb_2=int(input("Write number 2 = "))

print(f"\n{large_numb.__doc__}")
print("\nThe largest number is ", large_numb(numb_1,numb_2))