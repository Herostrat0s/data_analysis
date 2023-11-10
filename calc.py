def calc(x,y, operation):
    if operation == 'add':
        return x+y
    if operation == 'sub':
        return x-y
    if operation == 'mul':
        return x*y
    if operation == 'div':
        return x/y
operation = calc(7,3, 'div')
print(operation)