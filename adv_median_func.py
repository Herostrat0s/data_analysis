def adv_calculate_mean(*args):
    if len(args) == 0:
        return 0
    sort_numbers = sorted(args)
    middle1 = len(args) // 2
    middle2 = middle1 - 1

    median = (sort_numbers[middle1] + sort_numbers[middle2]) // 2
    
    return median

print(adv_calculate_mean(3,5,7,9))