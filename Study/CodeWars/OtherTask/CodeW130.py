# 1

# def make_negative( number ):
#     return -abs(number)  

# ____

# def make_negative( number ):
#     if number <0:
#         return number
#     return -number

# 2

# def str_count(strng, letter):
#     count = 0
#     for i in strng:
#         if i == letter:
#             count = count + 1
#     return count  
#     # Your code here ;)

# print(str_count('hello', 'l'))

# ____

# def strCount(string, letter):
#     return string.count(letter)


# 3


# def shark(pontoon_distance, shark_distance, you_speed, shark_speed, dolphin):
#     if dolphin:
#         shark_speed = shark_speed / 2
        
#     shark_eat_time = shark_distance / shark_speed
#     you_safe_time = pontoon_distance / you_speed
    
#     return "Shark Bait!" if you_safe_time > shark_eat_time else "Alive!"


# def shark(pontoonDistance, sharkDistance, youSpeed, sharkSpeed, dolphin):
#     if dolphin:
#         sharkSpeed /= 2
#     return "Alive!" if pontoonDistance / youSpeed <= sharkDistance / sharkSpeed else "Shark Bait!"


# 4


def powers_of_two(n):
    x = list(range(n))
    return x  

print(powers_of_two(5))

# l1 = list(range(5))     # call list __init__
# print(l1)