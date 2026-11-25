import array
from array import *

# my_araay = array.array('i') 
# #empy array of integer 
# # time complexity - O(1)

# print(my_araay)
# my_araay1 = array.array('i', [1,2,3,4],)
# print(my_araay1)

# import numpy as np

# np_array = np.array([], dtype =int) # time complexity - O(1)
# print(np_array)

# np_array1 = np.array([1,2,3]) #time complexity is linear -> O(N) & Space Complexity : O(N)
# print(np_array1)


# -----------------------------  import number into an array  --------------------------------#

# import array
# my_araay1 = array.array('i', [1,2,3,4])
# print(my_araay1)
# # array('i', [1, 2, 3, 4])

# my_araay1.insert(0,6) # 0 - index , 6-number
# print(my_araay1)
# # array('i', [6, 1, 2, 3, 4])

# my_araay1.insert(4,6) # 2 - index , 6-number
# print(my_araay1)

# # time complexity:
# # worst case = O(n)
# # Space_complexoty = O(1)

# ------------------------ Array Traversal ---------------------

# from array import *

# arr1 = array('i', [1,2,3,4,5,6])
# arr2 = array('d', [1.3,1.5,1.6])

# arr1.insert(2,9)
# print(arr1)

# def traverseArray(array):
#     for i in array: # ---------------> O(n)
#         print(i)    # ---------------> O(1)
#                                             # ---> O(n) in total
# traverseArray(arr1)

# def traversefalseArr(array1):
#     for i in range(1,len(array1)+1):
#         print(array1[-i])
# traversefalseArr(arr1)


# ------------------ Searching for an el in array -----------

# arr1 = array('i', [1,2,3,4,5,6])

# def accessElement(array, index):
#     if index >= len(array): #len(array) will return 6 -----> 0(1)
#         print('Index donot exist') # ----->O(1)
#     else:
#         print(array[index]) # -------> O(1)

# accessElement(arr1,6)

# Total time complexity: --------> O(1)
#Space complexity -------> O(1)

# ------------------------ Searching for an element -----------------

# arr1 = array('i', [1,2,3,4,5])

# def linear_search(array,target):
#     for i in range(0,len(array)): # ------> O(n)
#         if array[i] == target: #------->O(1)
#             return i #----->O(1) constant operation
#     return -1 #the lement is not fount in an arr1 -------->O(1)

# print(linear_search(arr1,8))

# total time complexity ------>O(n)
# time complexity for len(array) ----->O(N)
# time complexity for range function ----->O(1)
# Space coplexity --------> 0(1)


# ----------------- Deletion of an elements -----------------

# arr1 = array('i', [1,2,3,4,5])

# arr1.remove(1) # 1 is an element in this case
# print(arr1)

# arr1.remove(4)
# print(arr1)

# time complexity ---> O(1)--> for last element but for middle/second element ---> O(n)

# Space complexity ---> O(1)

# ---------------- Practice ---------
from array import *

arr1 = array('i', [1,2,3,4,5])

for i in arr1:
    print(i)

print(arr1[1])

#append method
arr1.append(6) #----->O(1)
print(arr1) 

#insert method
arr1.insert(3,1) # 3-index , 1 -number
print(arr1)
# -->O(n)

# extend method
print('step 5')
arr2 = array('i', [10,11,12]) #new array
arr1.extend(arr2) #but them at the end
print(arr1)

# add items from list into array using fromlist() method
print('step6')
temp_list = [20,21,22]
arr1.fromlist(temp_list) # elements come from list datatype
print(arr1)

#remove method
print('step7')
print(arr1)
arr1.remove(22) #it dins 1 element with 11 and removes it so if there is 2 22s it will remove only the 1st one
print(arr1) #---- 22 is removed
#time complexity ------->O(N)

#remove element using pop() method
print('step8')
print(arr1)
arr1.pop(3) #element of index 3 is poped
print(arr1)

#using index() method
print('st9')
print(arr1.index(21)) #---->O(1)

#reverse using reverse()
print('st10')
print(arr1)
arr1.reverse()
print(arr1)

#get array buffer information through buffer_info() method
print('st11')
print(arr1.buffer_info()) # start from ... this point and has ... elements

# check fr number of occurences of an element using count() method
print('st12')
arr1.append(11)
print(arr1.count(11)) # count how many times element 11 occurs
print(arr1)

# convert array t0 string using tobytes() method
print('step 13')
strTemp = arr1.tobytes() 
print(strTemp)

ints = array('i')
ints.frombytes(strTemp)
print(ints) # same array as we had before

# conver an array to a python list using tolist() method
print('step14')
# print(arr1.tolist())



# slice elements from an array

print('step 16')
print(arr1)
print(arr1[::3]) # prints with a step of 2
print(arr1[1:3])
print(arr1[:])