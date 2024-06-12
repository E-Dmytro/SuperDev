import random
#Generate 5 random numbers between 10 and 30
random_numb = (random.randint(0, 99))
print("Random number was selected")
# for floatlist in randomlist_int:
#     print(float(floatlist), end=' ')
while True:
    try:
        user_numb = int(input("Enter your number = "))
        user_numb=abs(user_numb)#no minus
        if user_numb!=random_numb:
            if user_numb >= random_numb:
                print(f"\nYour number is bigger than random number \n Please.Try again.\n")
            else:
                print(f"\nYour number is smaller than random number \n Please.Try again.\n")
        else:
            print(f"\nYou are lucky. \nMy congratulations!!!")
            break
    except:
        print("Error")
        continue

