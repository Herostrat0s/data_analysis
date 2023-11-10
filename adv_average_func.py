def calculate_average(*args):
    if len(args) == 0:
        return 0
    total = sum(args)
    avg = total // len(args)
    return avg
print(calculate_average(100,8,7,6,5))