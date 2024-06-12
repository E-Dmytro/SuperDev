arr=[1,2,3,4,5,6,7,-5,-6,-6,-2]

def count_positives_sum_negatives(arr):
    if not arr: return []
    pos = 0
    neg = 0
    for x in arr:
      if x > 0:
          pos += 1
      if x < 0:
          neg += x
    return [pos, neg]

print(count_positives_sum_negatives(arr))