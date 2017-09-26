from re import *
"""
    Python Files, strings, lists, dictionaries
"""
#EX4
def has_duplicates(list_of_stuff):
    tmp = sorted(list_of_stuff)
    has_dup = False
    i = 0
    while i < len(tmp) - 1 and not has_dup:
        if tmp[i] == tmp[i + 1]:
            has_dup = True
        i += 1    
    return has_dup

# x = [1, 5, 3, 5, 2, 32, 2]
# y = [1, 2, 3, 4, 5, 6, 7, 8]

# print(has_duplicates(x))
# print(has_duplicates(y))
# print(x)
# print(y)

#EX5
def has_duplicates_dict(list_of_stuff):
    dict_stuff = {}
    

#Regular Expressioni

#Find chapter numbers and titles in alice.txt
def ex1(data):
    print(findall('CHAPTER.*', data))

#run each example re function
def pyth_re():
    #Number 1
    with open('alice.txt') as inf:
        data = inf.read()
        ex1(data)

pyth_re()