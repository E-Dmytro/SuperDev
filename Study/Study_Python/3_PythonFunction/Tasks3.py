########## Exercise 1 #########

# 1

# def outer(name):
#   def inner():
#     print(f"Hello, {name}!")
#   return inner

# alice = outer("Alice")
# alice()

# 2

# def outer(name):
#     """
#     make function more welcome
#     """
#     def inner():
#         print("Hello,{name}!".format(name=name))
#         return outer(name)
#     return inner()

# alice = outer("Alice")
# alice()

# 3

# def outer(name):
#   def inner():
#     print("Hello, {}!".format(name))
#   return inner


# alice = outer("Alice")
# alice()


########## Exercise 2 #########

# 1

# def create(a:str):
#     b=a
#     return lambda b : (b==a)


# print(secondValue("SecreT")


# 2

# def create(name):
#   return lambda a: a == name  # replace outer with a
#
#
# firstValue = create("secret")


########## Exercise 3 #########


# 1

# import copy
# import re
#
# def create_account(user_name: str, password: str, secret_words: list):
#     if re.match (r"^(?=.{6,}$)(?=.*[A-Z])(?=.*[\W_]).*$",password):
#         def check(p,sw):
#             nonlocal password, secret_words
#             error = 0
#             if (len(secret_words)!=len(sw)):
#                 return False
#             else:
#                 secret_words1 = copy.deepcopy(secret_words)
#                 sw1 = copy.deepcopy(sw)
#                 for i in secret_words1:
#                     if i not in sw1:
#                         error += 1
#                     else:
#                         sw1.remove(i)
#                     return (p == password) and (len(secret_words)==len(sw)) and (error < 2)
#     else:
#         raise ValueError
#
#
# tom = create_account("Tom", "Qwerty1_", ["1", "word"])
# print(tom)

# 2

# def creat_account(user_name, password, secret_words):
#     import re
#     pattern = ("(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^a-zA-Z0-9])")
#     if not re.search(pattern, password) or len(password) < 6: raise ValueError
#
#     def check(cmp_pd, cmp_secwords):
#         if (len([i for i in cmp_secwords if not i in secret_words]) > 1 or
#         len([i for i in secret_words if not i in cmp_secwords]) >1 ):
#             return False
#         elif password != cmp_pd or len(cmp_secwords) != len(secret_words):
#             return False
#         else: return True
#
#     return check
#
#
# tom = create_account("Tom", "Qwerty1_", ["1", "word"])
# print(tom)


########## Exercise 4 #########

# 1
# def divisor(num):
#     for i in range(1, num + 1):
#         if num % i == 0:
#             yield i
#
#     while True:
#         yield
#
# # 2
#
# def divisor(a):
#     n=1
#     while n<=100:
#         if a%n=0:
#             yield n
#         if n > a:
#             yield None
#         n+=1


########## Exercise 5 #########

# # 1

# def logger(func):
#     def wrapper(*args, **kwargs):
#         return_value = func(*args, **kwargs)
#         print(f"Executing of function {func.__name__}with arguments {','.join(map(str, args + tuple(kwargs.values())))}...")
#         return return_value
#     return  wrapper
#
# @logger
#
# def concat(*args,**kwargs):
#     if kwargs == {}:
#         return ''.join(map(str,args))
#     else:
#         return ''.join(map(str,list(args) + list(kwargs.values())))
#
#
# # # 2
#
# def logger(func):
#     def inner(*args, **kwargs):
#         print_args=', '.join([str(a) for a in args] + [str(a) for a in kwargs.values()])
#         res = func(*args, **kwargs)
#         print(f'Executing of function {func.__name__} with arguments {print_args}...')
#         return res
#
#     return inner
#
# @logger
# def concat(*args, *kwargs):
#     return ''.join([str(a) for a in args] + [str(a) for a in kwargs.values()])


########## Exercise 6 #########

# # # 1
# import random
#
#
# def randomWord(list):
#     if list:
#         while True:
#             random.shuffle(list)
#
#             for e in list:
#                 yield e
#     yield None
#
# # # # 2
#
# def randomWord(book):
#
#     inner_list = books.copy()
#
#     if len(books) == 0:
#         yield None
#
#     while True:
#
#         book = inner_list.pop()
#
#         if len(inner_lest) == 0:
#             inner_list = book.copy()
#             random.shuffle(inner_list)
#
#         yield book
#
# # # # 3
#
# def randomWord(words):
#     temp = []
#     wordy = list(words)
#     while True:
#         try:
#             word = random.choice(wordy)
#         except:
#             yield None
#         yield word
#         temp.append(wordy.pop(wordy.index(word)))
#         if len(wordy) == 0:
#             wordy = temp
#             temp = []
#

##########QUIZ############

# 1

# def function(item, stuff = 5):
#     stuff += item
#     print(stuff, end = ' ')
#
# function(1)
# function(3)

# 2

# def outer():
#     message = 'Outer string variable'
#     def inner():
#         global message
#         message = "Inner string variable"
#     inner()
#     return message
#
# print(outer())

