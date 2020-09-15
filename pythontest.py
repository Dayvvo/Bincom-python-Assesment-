import re
import random
import math
import psycopg2
from psycopg2 import OperationalError
import postgres
import numpy as np
import postgres



#   TASK A-EXTRACT WITH PYTHON

colors_arr = []
#   open file, readlines into lines_arr & define regex expression and variables
with open('python_class_test.html') as python_class_test:
    lines = python_class_test.readlines()
    color2 = re.compile(r'(<td>(?P<stuff>.*)</td>)')
    lines_arr = []
#   loop through rows in colors column and append entire rows for each day into lines_arr
    for i in range(len(lines)):
        result = ''
        if color2.search(lines[i]) and re.search(',', lines[i]):
            result = color2.search(lines[i])
            lines_arr.append(result.group('stuff'))
#   loop through each element in lines_arr and add only color names into colors_arr by removing the comma before appending
    def remove_trailing_commas(n):
        if not ',' in n:
            return n
        else:
            return n[:n.find(',')]
#   remove commas from color strings
    for ij in lines_arr:
        colors_arr += ij.split(', ')
    colors_arr = list(map(remove_trailing_commas, colors_arr))
    print('TASK A', colors_arr)




#   TASK B

# create new list containing only unique values of extracted colors
unique_arr = list(dict.fromkeys(colors_arr))
dictionary = {}
for i in unique_arr:
    dictionary[i] = colors_arr.count(i)
print('TASK B', dictionary)



#   TASK 1

# sum up list of shirts and divide by len(shirt_arrays)  ie sum of dictionary values
sumup = sum(list(dictionary.values()))
avg = sumup / 10
print('TASK 1', avg)





#   TASK 2
#   loop through dictionary and check for max_Value
maxval = 0
maxkey = None
for i in dictionary:
    if dictionary[i] > maxval:
        maxval, maxkey = dictionary[i], i
print('TASK 2', maxkey)







#   TASK 3

#   sort the list of color and find the middle index
sorted_arr = sorted(colors_arr)
median = sorted_arr[int(len(sorted_arr)/2)]
print('TASK 3', median)






#   TASK 4 - VARIANCE

#use numpys built in variance
# variance = np.var(dictionary.values())
print('TASK 4- Variance: ', np.var(list(dictionary.values())))




#   TASK 5- PROBABILITY

# calculate probability = required outcome / possible outcomes
red_probability = dictionary["RED"] / sum(dictionary.values())
print("TASK 5-Probability", red_probability)








#   TASK 7 - RECURSIVE SEARCH
def binary_search(sorted_array, element):
#   set the value of first and last value of array, and define element found variable
    start, end, found = 0, len(sorted_array)-1, False
    for i in range(len(sorted_array)):
        if start <= end and not found:
            middle = int((start + end) / 2)
# check if middle element = desired element
            if sorted_array[middle] == element:
                found = True
                break
# if not check if element is on the left or right side of the array
            else:
                if sorted_array[middle] > element:
                    end = middle - 1
                elif sorted_array[middle] < element:
                    start = middle + 1
    if found:
        return "Task 7, Element Found"
    else:
        return "Task 7, Not Found"

print(binary_search([i for i in range(10)], 16))





#   TASK 8 - RANDOM 4 DIGIT DIGIT
def random_int():
    int_value = ""
#   loop through length of digits i.e 4
    for ii in range(4):
#   catenate int_val with a randomly generated binary digit
        int_value += str(random.randint(0, 1))
    print("TASK 8 - RANDOM DIGIT: ", int(int_value, base=2), int_value)


random_int()









#   TASK 9 fibonacci generator

def fibonacci_generator(arr=50):
    arr2 = []
#   loop through range (1,arr)
    for fb in range(arr):
# if fb = 0 append
        if fb == 0:
            arr2.append(fb)
#   if fb = 1 append 0 + 1
        elif fb == 1:
            arr2.append(fb + int(arr2[fb-1]))
# else append sum of two previous array elements
        else:
            arr2.append(int(arr2[fb-1] + int(arr2[fb-2])) )
    print("TASK 9:", arr2)

fibonacci_generator(50)

  # TASK 6 - MIGRATE TO POSTGRES
print("TASK 6")
username = input("Enter username")
password_2 = input("Enter password again")
port = input("Enter port")
host = input("Enter host IP")
while password != password_2:
    password = input("both passwords must match")
else:
    # connect = postgres.connect("postgres", username, password, port, host)
    insert_query = (
        f"INSERT INTO color_table (color, frequency) VALUES {dictionary.items()}"
    )
    # postgres.insert_todo(insert_query, connect)

