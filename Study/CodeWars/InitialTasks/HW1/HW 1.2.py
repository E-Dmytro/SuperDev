number_a = int(input("Write number a = "))
number_b = int(input("Write number b = "))
addition_signs=['+', '-', '*', '**', '/', '//', '%']

print(f"Variable of signs: {addition_signs}")
addition_sign= input("\n Choose a sings -")

if addition_sign == '+':
    output=number_a+number_b
elif addition_sign == '-':
    output=number_a-number_b
elif addition_sign == '*':
    output=number_a*number_b 
elif addition_sign == '**':
    output=number_a**number_b 
elif addition_sign == '/':
    output=number_a/number_b 
elif addition_sign == '//':
    output=number_a//number_b 
elif addition_sign == '%':
    output=number_a%number_b

else:
    output="Error"
    print("\n You write wrong combination")
print(f"{number_a}{addition_sign}{number_b}={output}")
input()
 