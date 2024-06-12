n = int(input("Enter the number:"))
num_str=str(n)
suma=0
mult=1

while n>0:
    digit=n % 10
    suma = suma + digit
    mult = mult * digit
    n = n // 10
print(suma)
print(mult)

print(f" {num_str[::-1]}")
print(f" {sorted(num_str)}")