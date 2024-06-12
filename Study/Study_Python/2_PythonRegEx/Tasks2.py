########## Exercise 1 #########

# 1
# def double_string(data):
#     data_copy = {i+j for i in data for j in data}
#
#     counter = 0
#     for element in data:
#         if element in data_copy:
#             counter += 1
#     return counter
#
# data = ['aa', 'aaaa', 'aaaaaaaa', 'aaaa', 'qwer', 'qwerqwert']
# print(double_string(data))

# 2
# def double_string(data):
#     counter = 0
#     options = {word + word1 for word in data for word1 in data}
#     for word in data:
#         if word in options:
#             counter += 1
#     return counter
#
# data = ['aa', 'aaaa', 'aaaaaaaa', 'aaaa', 'qwer', 'qwerqwert']
# print(double_string(data))



########## Exercise 2 #########

# 1

# MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
#                    'C': '-.-.', 'D': '-..', 'E': '.',
#                    'F': '..-.', 'G': '--.', 'H': '....',
#                    'I': '..', 'J': '.---', 'K': '-.-',
#                    'L': '.-..', 'M': '--', 'N': '-.',
#                    'O': '---', 'P': '.--.', 'Q': '--.-',
#                    'R': '.-.', 'S': '...', 'T': '-',
#                    'U': '..-', 'V': '...-', 'W': '.--',
#                    'X': '-..-', 'Y': '-.--', 'Z': '--..',
#                    '1': '.----', '2': '..---', '3': '...--',
#                    '4': '....-', '5': '.....', '6': '-....',
#                    '7': '--...', '8': '---..', '9': '----.',
#                    '0': '-----', ', ': '--..--', '.': '.-.-.-',
#                    '?': '..--..', '/': '-..-.', '-': '-....-',
#                    '(': '-.--.', ')': '-.--.-'}
#
#
#
# def morse_number(message):
#   cipher = ''
#   for letter in message:
#     if letter != ' ':
#       cipher += MORSE_CODE_DICT[letter] + ' '
#     else:
#       cipher += ' '
#
#   return cipher

# 2

# def morse_number(num):
#     def convert(digit):
#         if digit <= 5:
#             return '.' * digit + '-' * (5 - digit)
#         return '-' * (digit-5) + '.' * (10 - digit)
#
#     return ''.join([convert(int(i)) for i in num])
#
# print(morse_number("295444"))


########## Exercise 3 #########

# 1

# import re
# from math import *
#
#
# def figure_perimetr(data):
#     a = []
#     result = re.findall(r'\d', data)
#
#     for i in result:
#         a.append(float(i))
#
#     [x1, y1, x2, y2, x3, y3, x4, y4] = a
#     dist1 = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
#     dist2 = sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2)
#     dist3 = sqrt((x4 - x3) ** 2 + (y4 - y3) ** 2)
#     dist4 = sqrt((x4 - x2) ** 2 + (y4 - y2) ** 2)
#     dist = dist1 + dist2 + dist3 + dist4
#
#     return round(dist, 14)

# 2

# import re
#
# def figure_perimetr(s):
#     lst = [[int(i) for i in point.split(':')] for point in re.findall(r'\d+:\d+',s)]
#     points = lst[:2] + lst[-1:] + lst[2:3] + lst[0:1]
#     sum_ = 0
#     for i, point in enumerate(points[1:]):
#         sum_ += ((points[i][0] - point[0]) ** 2 + (points[i][1] - point[1]) ** 2) ** 0.5
#     return sum_
#
# # 3
#
# from math import sqrt
#
# def figure_perimetr(data):
#     list_of_points = data.split('#')[1:]
#     figure_dict = dict()
#
#     for item in list_of_points:
#         figure_dict.update({item[:2]: (item[2:].split(':'))})
#
#     def vector_length(point_1, point_2):
#         return sqrt((int(point_2[0])-int(point_1[0]))**2 + (int(point_2[1])-int(point_1[1]))**2)
#
#     return vector_length(figure_dict['LB'], figure_dict['LT']) + vector_length(figure_dict['LT'], figure_dict['RT'])

########## Exercise 4 #########


# # 1

# import re
#
# def pretty_message(data_string):
#
#     pattern = r'([a-z])\1{2,}|(..)\2+|(...)\3+'
#     result = re.sub(pattern, r'\1\2\3', data_string)
#
#     return (result)
#
#
# data = "Thisssssssss isisisis echooooooo stringggg. Replaceaceaceace repeatedededed groupssss of symbolssss"
# print(pretty_message(data))


# # 2

# import re
# def pretty_message(data):
#
#     pattern = r'(\w{1}|\w{2}|\w{3})\1+'
#     new_p = r'\1'
#     new = re.sub(pattern, new_p, data)
#     return new
#
#
# data = "Thisssssssss isisisis echooooooo stringggg. Replaceaceaceace repeatedededed groupssss of symbolssss"
# print(pretty_message(data))


########## Exercise 5 #########

# 1
# import re
#
# def max_population(data):
#     def handle(x): return x[0], int(x[1])
#
#     lst = [handle(item.split(',')[1:3]) for item in data[1:]]
#     return sorted(lst, key=lambda x: x[1], reverse=True)[0]
#
#
# data = ["id,name,poppulation,is_capital",
#         "3024,eu_kyiv,24834,y",
#         "3025,eu_volynia,20231,n",
#         "3026,eu_galych,23745,n",
#         "4892,me_medina,18038,n",
#         "4401,af_cairo,18946,y",
#         "4700,me_tabriz,13421,n",
#         "4899,me_bagdad,22723,y",
#         "6600,af_zulu,09720,n"]
#
# print(max_population(data))
#

# # 2

# import re
#
# def max_population(data):
#     pattern = r'(^\d{4})|(?=([a-z]{2,}_[a-z]{1,}),)|(?<=(\d{5}))|(?=(y|n)$)'
#     population = 0
#     province_name = ""
#
#     for key in data:
#         result = re.findall(pattern,key)
#         for item in result:
#             if int(result[2][2]) > population:
#                 population = int(result[2][2])
#                 province_name = result[1][1]
#         return (province_name,population)
#
# data = ["id,name,poppulation,is_capital",
#         "3024,eu_kyiv,24834,y",
#         "3025,eu_volynia,20231,n",
#         "3026,eu_galych,23745,n",
#         "4892,me_medina,18038,n",
#         "4401,af_cairo,18946,y",
#         "4700,me_tabriz,13421,n",
#         "4899,me_bagdad,22723,y",
#         "6600,af_zulu,09720,n"]
#
# print(max_population(data))