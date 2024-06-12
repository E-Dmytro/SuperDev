def enough(cap, on, wait):
    if cap >= on and wait - on == 0:
        return 0
    else:
        not_take = on - wait
        return not_take
    # Your code here
