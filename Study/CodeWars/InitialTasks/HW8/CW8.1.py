# def summation(num):
#     pos = 0
#     while (num > 0):
#             pos += num
#             print(pos)
#             num -= 1
#             print(num)
#     return pos
#         # Code here

def summation(num):
    pos = 0
    for num in range(1,num + 1):
            pos += num
            print(num)
    return pos
        # Code here

num = int(input("Write number = "))
print(summation(num))