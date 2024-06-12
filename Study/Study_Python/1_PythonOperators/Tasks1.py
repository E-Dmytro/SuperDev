######### Exercise 1 #############
# # Exercise 1
#
# # Example 1
#
# def kthTerm(n, k):
#     a =[]
#     b = a.append
#     for i in range(9):
#         b(n**i)
#         l = len(a)-1
#         for j in range(l) :
#             b(a[l]+a[j])
#     return a[k-1]
#
# # Example 2
#
# def kthTerm(n, k):
#     mas = []
#     for i in range(10):
#         mas.append(n**i)
#         for j in range(1, len(mas)):
#             mas.append(n**i + mas[j-1])
#     return mas[k-1]
#
# # Example 3
#
# def kthTerm(n,k):
#     seq =[0,1]
#     counter =1
#     while len(seq) <= k:
#         for i in range(len(seq)):
#             seq.append(n**counter + seq[i])
#         counter += 1
#     return seq[k]
#
# # Example 4
#
# def kthTerm(n, k):
#     list = []
#     for i in range(0,k):
#         list.append(0**i)
#         last_element_number = len(list) - 1
#         if last_element_number >= k:
#             break;
#         elif last_element_number >= 1:
#             for j in range(0, len(list) - 1):
#                 list.append(list[last_element_number]+list[j])
# #     if k <= len(list):
#     return list[k-1]
# # else
# #    return None



######### Exercise 2 #############

# Example 1

# filterBible = lambda s, b, c: [i for i in s if i[:5] == b +c]

# Example 2

# def filterBible (scripture, book, chapter):
#     return [verse for verse in scripture if verse.startwith(book + chapter)]
#
# # Example 3
#
# def filterBible (scripture, book, chapter):
#     result = []
#     pattern = book + chapter
#     for item in scripture:
#         if item.startwith(pattern):
#             result.append(item)
#     return result
#
# #Example 4
#
# def filterBible (scripture, book, chapter):
#     bookchapter = book + chapter
#     reab = []
#     for i in range(0, len(scripture)):
#         if scripture[i].startswith(bookchapter):
#             reab.append(scripture[i])
#
#     return reab
#     pass

######### Exercise 3 #############

# #Example 1

# isPalindrome = lambda s: sum(s.count(c) % 2 for c in set(s))  < 2
#
# # #Example 2
#
# def isPalindrome(str):
#     total = 0
#     tally = {}
#     oddly = False
#     for char in str:
#         if char.isalnum():
#             total += 1
#             index =char.lower()
#             tally[index] = tally.get(index,0) +1
#     if total % 2 :
#         for entry in tally:
#             if tally[entry]%2:
#                 if oddly:
#                     return False
#                 oddly = True
#             return  oddly
#         else:
#             for entry in tally:
#                 if tally[entry]%2:
#                     return False
#         return True


######### Exercise 4 #############
# #Example 4

# #Example 1

# findPermutation = lambda n,p,q: [p.index(i)+1 for i in q]
#
# # #Example 2
#
# def findPermutation(n,p,q):
#     return [p.index(q[i])+1 for i in range(n)]
#
#
# # #Example 3
#
# def findPermutation(n,p,q):
#
#     r = []
#     for i in q:
#         r.append( p.index(i) + 1 )
#     return r

# #Example 4

# def findPermutation(n,p,q):
#     r=[]
#     for i in range(0, n):
#         for j in range(0,n):
#             if q[i] == p(j):
#                 r.append(j+1)
#     return print(r)


# def findPermutation(n,p,q):
#     x=p+q+n
#     return x

######### Exercise 5 #############

# # #Example 1
#
# def toPostFixExprssion(e):
#     p = {
#         '+': 2,
#         '-': 2,
#         '*':3,
#         '/':3,
#         '%':3,
#         ')':1,
#         '(':1
#     }
#     s = []
#     r = []
#     for c in e:
#         if c in p and p[c] > 1:
#             while s and p[c] <= p[s[-1]]:
#                 r += [s.pop()]
#             s+=[c]
#         elif c == '(':
#             s +=[c]
#         elif c == ')':
#             while s [-1] != '(':
#                 r += [s.pop()]
#             s.pop()
#         else:
#             r += [c]
#     for c in s[::-1]:
#         r += [c]
#     return r
#
# # #Example 2
#
# OPERATORS = ['+','-','*','/','%','(',')']
# PRECEDENCE = {'+':1, '-':1,'*':2,'/':2,'%':2}
#
# def toPostFixExpression(e):
#     stack = []
#     output = []
#     for symbol in e:
#         if symbol not in OPERATORS:
#             output.append(symbol)
#         elif symbol == ")":
#             while stack and stack[-1] != '(':
#                 output.append(stack.pop())
#             stack.pop()
#         else:
#             while stack and stack[-1] != '(':
#                 for operator in stack:
#                     if PRECEDENCE[operator] >= PRECEDENCE[symbol]:
#                         output.append(stack.pop())
#                 break
#             stack.append(symbol)
#
#     while stack:
#         output.append(stack.pop())
#
#     return output

######### Exercise 6 #############

# #Example 1

# def order(a):
#     return 'ascending' if sorted(a) == a else "descending" if sorted(a) == a[::-1] else 'not sorted'
# # return [["not sorted", "descending][sorted(a) == a[::-1]], "ascending"][sorted(a) == a]
#
#
# # #Example 2

# def order(a):
#     sort_a = sorted(a)
#     revers_sort_a = sort_a[::-1]
#     if a == sort_a:
#         return 'ascending'
#     elif a == revers_sort_a:
#         return 'descending'
#     else:
#         return 'not sorted'

######### Exercise 7 #############

# #Example 1

# def Cipher_Zeroes(N):
#     t = N.count
#     t = t('6') + t('0') + t('9') + 2* t('8')
#     t += [-1, 1][t % 2]
#     return int(bin([0, t][t>0])[2:])
#
# # #Example 2
#
# def Cipher_Zeroes(N):
#     point = 0
#     for symbol in N:
#         if int(symbol) in  (0, 6, 9):
#             point += 1
#         elif int(symbol) == 8:
#             point += 2
#         else:
#             continue
#     if point > 0:
#         if point % 2:
#             point += 1
#         else:
#             point -= 1
#     return bin(point)[2:]
#
#
# ######### Exercise 8 #############
#
# # #Example 1
#
# def studying_hours(a):
#     w = []
#     r = 0
#     x = 0
#     for i in a:
#         r = [1, r + 1][x <= i]
#         w += [r]
#         x = i
#     return max(w)
#
# # #Example 2
#
# def studying_hours(a):
#     i = 0
#     cur_len = 1
#     max_len = 0
#     while i < len(a) - 1 :
#         if a[i] <= a[i+1]:
#             cur_len += 1
#         else:
#             if max_len < cur_len:
#                 max_len = cur_len
#             cur_len = 1
#         i += 1
#     if max_len < cur_len:
#         max_len = cur_len
#     return max_len
#
# # #Example 3
#
# def studying_hours(a):
#     max = 0
#     i = 0
#     while i + 1 < len(a):
#         couter = 1
#         while i + 1 < len(a) and a[i] <= a[i + 1]:
#             couter += 1
#             i += 1
#         if couter > max:
#             max = couter
#         i += 1
#     return max


# ######### QUIZ #############

# input_string = "1010 0101 1111 0001"
# output_string = input_string[:4]+' '+input_string[:-4]
# print(output_string)

x=3
print((x<<5))