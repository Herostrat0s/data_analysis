some_list = ['a', 'b', 'c', 'd', 'e'] 
(first, second, *rest) = some_list 
print(rest)
(first, *middle, last) = some_list 
print(middle)
(*head, penultimate, last) = some_list 
print(head)