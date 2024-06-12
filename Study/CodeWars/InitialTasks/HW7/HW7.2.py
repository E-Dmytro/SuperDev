import re
def valid(value):
    if len(value) >= 6 and len(value) <= 16 :
        parameter_1=re.findall("[a-z]", value)
        parameter_2=re.findall("[A-Z]", value)
        parameter_3=re.findall("[1-9]", value)
        parameter_4=re.findall("[!@#$%^&*]", value)
        if len(parameter_1) > 0 and len(parameter_2) > 0 \
                and len(parameter_3) > 0 and len(parameter_4) > 0:
            print("Good password!!!")
        else:
            print("\nError!\nTry again!")
    else:
        print("Try again!\n Please,change something!")






password = input(" Enter your password =")
valid (password)