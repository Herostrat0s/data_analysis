def calculate_mean(*args):
    if len(args) == 0:
        return 0
    mean = (len(args) // 2) + 1
    # With this function we will find the index of mean value from a list
    return mean
print(calculate_mean(3,5,7,9,10,12,13)) 