def zero_fuel(distance_to_pump, mpg, fuel_left):
    #Happy Coding! ;)
    if distance_to_pump<=fuel_left*mpg:
        return 1
    else:
        return 0
