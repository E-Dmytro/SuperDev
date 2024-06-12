def solution(number):
    additional=0
    for x in range(number):
        if x%3==0 or x%5==0:
            additional+=x
    return additional
