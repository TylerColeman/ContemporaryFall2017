from re import *
import math
"""
    Intro: basic python syntax Problems
"""
#EX1
def grade():
    num_grade = int(input("Please enter a numeric grade between 0 and 100.\n"))
    if num_grade >= 90: print('A')
    elif num_grade >= 80: print('B')
    elif num_grade >= 70: print('C')
    elif num_grade >= 60: print('D')
    else: print('F')

#EX2
def converter_ft_in(val, typeof, typeto):
    if typeof.lower() == 'feet' and typeto.lower() == 'inches':
        return val * 12
    elif typeof.lower() == 'inches' and typeto.lower() == 'feet':
        return val / 12
    else:
        return val

#EX3
def qudratic_solutions(CoeffA, CoeffB, CoeffC):
    discriminant = CoeffB**2 - (4 * CoeffA * CoeffC)
    if discriminant >= 0:
        val1 = (-CoeffB + math.sqrt(discriminant)) / (2 * CoeffA)
        val2 = (-CoeffB - math.sqrt(discriminant)) / (2 * CoeffA)
        if abs(val1 - val2) == 0:
            print(val1)
        else:
            print(str(val1), ' ', str(val2))
    else:
        print("No real solutions.")

"""
    Python: Functions, loops, and recursion
"""
#EX1 Brute Force
def perf_num(num):
    summ = 0
    for i in range(1,num):
        if num % i == 0:
            summ += i
    if summ == num:
        print("Perfect")
    elif summ > num:
        print("abundant")
    else:
        print("Deficient")

#EX2
def perf_num2(num):
    summ = 0
    for i in range(1,num):
        if num % i == 0:
            summ += i
    if summ == num:
        return('p')
    elif summ > num:
        return('a')
    else:
        return('d')

#EX2
def base10_to_base2(num):
    if num == 1:
        print(1)
    else:
        print(num % 2)
        base10_to_base2(num // 2)
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



fruit = 'banana'
i = fruit.find('a')
print(i)
x = [1, 2, 3]
del x[1]
print (x)