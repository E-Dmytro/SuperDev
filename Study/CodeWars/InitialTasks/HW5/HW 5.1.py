numb_even = [ x for x in range (11) if x%2==0 and x!=0 ]
numb_odd =  [x for x in range (1,11) if x%3==0 and x!=0 ]
numb_other = [x for x in range (11) if x%2!=0 and x%3!=0]
print(f"All even number in range [0,10] are {numb_even}")
print(f"All divisible number in range [0,10] are {numb_odd}")
print(f"All other number in range [0,10] are {numb_other}")


