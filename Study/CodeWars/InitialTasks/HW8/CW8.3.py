def double_char(s):
    n = 2
    return ''.join([char * n for char in s])
s=input("Write -- ")
print(double_char(s))


def double_char(s):
    word=''
    for char in list(s):
        n=2
        word+=char*n
    return ''.join(word)
s=input("Write -- ")
print(double_char(s))