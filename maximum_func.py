def find_max(numbers):
    if len(numbers) == 0:
        return 0
    maxnumber = numbers[0]
    for number in numbers:
        if number > maxnumber:
            maxnumber = number
    return maxnumber

my_list = [3,5,7,9,12,15,-99]
print(find_max(my_list))