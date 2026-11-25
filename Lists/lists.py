# ------------------------------ Lists ----------------------------------

# a list is a data structure that holds an ordered collection of items

# values in lists - elements or items

# elements of list dont have to be the same type we can mix different types 

# we can create a list in another list ---> nested list

# integers = [1,2,3,4]
# print(integers)

# StringList = ['Milk','Cheese','Butter']
# print(StringList)

# mixedList = [1,'Milk',1.5,'Butter']
# print(mixedList)

# nestedList = [1,2,3,4,[1.5,1.6], ['test']]
# print(nestedList)

# empty = []
# print(empty)

# ---------------- How to access/traverse elements in the list --------------

# shopping_list = ['Milk', 'Cheese', 'Butter']

# print(shopping_list[0]) #access 1 element in the list
# print(shopping_list[2])


# print('Milk' in shopping_list) # means we have. aMilk here
# print('Bread ' in shopping_list)

# print(shopping_list[-1]) # accessing the last element
# print(shopping_list[-2])

#------------Traversing -----------------

# for i in shopping_list:
#     print(i)

# for i in range(len(shopping_list)):
#     shopping_list[i] = shopping_list[i] + ' +'
#     print(shopping_list[i])    

# empty = []
# for i in empty:
#     print('i a empty')

# ---------------------------------------- Update/Insert a List ----------------------------
#list are mutable so u can update elements etc

# my_List = [1,2,3,4,5,6,7]
# print(my_List)

# my_List[2] = 33     #update 3rd elemet
# my_List[4] = 55     #update 5rd element
# print(my_List)

# # Time complexity ----------> O(1)
# # Space Complexity ---------> O(1)


# --------------------- Inserting a value to the list --------------------

# 1. Inserting an element to the beginning of the list
# 2. Inserting an element to the any given place in the list
# 3. Inserting an element to the end of the list
# 4. Inserting another list to the list

# List methods 
# - insert()
# - append()
# - extend()

# myList = [1,2,3,4,5]
# print(myList)


# myList.insert(0,11) # 1st el of the list is not 11
# print(myList)
# # every element moves 1 step right

# myList.insert(4,15) #-------------->O(n) --------> Space complexity O(1)
# print(myList)       

# # append() method --- > only append at the end of list
# myList.append(55)    # -----------------> O(n) ----->Space complexity 0(1)
# print(myList)

# # extend() method ----> add one list to other list
# newList = [11,12,13,14]
# myList.extend(newList) # ---------------> O(n), Space complexity --->O(n)
# print(myList)
# # all el of new_list is added to myList 



# ---------------------- Slice/Delete from a List -----------------------
# myList = ['a','b','c','d','e','f']
# print(myList[0:2]) #2nd list is not included
# print(myList[:2])
# print(myList[1:]) # from 2nd el to the last 


# myList[0:2]= ['x','y']
# print(myList[:]) # first few elements changed to x and y

#List method for deletion
# - pop()
# - delete()
# - remove()


# ------------------------- pop ---------------------------------

# myList.pop(1) #delete 2 element and all elements moved 1 space left
# print(myList) 
# myList.pop() # delete last element
# # print(myList)
# print(myList.pop()) # it deleted f(the last element) so it returns the element which is supposed to be deleted if calling without print statement
# print(myList.pop(2))
# print(myList) # now there is list with no last and 3rd element , they are removed and their values returned using print


# time complexity -----------> O(1) but it can be O(n) if a lot of numbers and it has left shifts
# space complexity ----> O(1)
# 
# ------------------------- pop ---------------------------------

myList = ['a','b','c','d','e','f']

# ----------------------- delete() method --------------------------
# del myList[1]
# print(myList) #1st eement is deleted
# del myList[3]
# print(myList) #4th eement is deleted

# ! delete() function does not return anything

# del myList[2:3] #3el is removed
# print(myList)

# del myList[2:4] #3 and 4 el is removed
# print(myList)



#time complexity ------------> O(n)
#space complexity ------------> O(1)
# ----------------------- delete() method --------------------------

# -------------------------- remove() function -----------------------

# myList.remove('e')
# print(myList)
# # element e is deleted

# Time complexity ---------------> O(m)
# Space complexity --------------> O(1)

# -------------------------- remove() function -----------------------

# ---------------------------------Searching for an element in the list ------------------

# myList = [10,20,30,40,50,60,70,80,90]

# -------------------------using in operator ---------------

# target = 500

# if target in myList:
#     print(f'number {target} is in the list')
# else:
#     print(f'number {target} is not in the list')

# time complexity ------>O(n)

# -------------------------using in operator ---------------

# -------------------------Linear search ---------------
# myList = [10,20,30,40,50,60,70,80,90]
# target = 500
# def linear_search(p_list, p_target):
#     for i, value in enumerate(p_list): #i-indexes , value - actual numbers
#         if value ==p_target:
#             return i
#     return -1 #element does not exist

# print(linear_search(myList,target)) #return index of 50

        
# # Time complexity -----------> O(n)
# # Space complexity ---------->  O(1)

# -------------------------List operations / functions---------------
# a = [1,2,3]
# b = [4,5,6,7]

# c = a+b
# print(c)

# a = [0]
# a = a*4
# print(a) #will repeat 0 2 times


# b = [0,1]
# b = b*4 # repeat 0,1 4 tims
# print(b)

#--------------------------------------------------------------------------
#to count elmts on the list

# a = [0,1,2,3,4,5,6] # return count of elements in the list
# print(len(a))

# #max() the highest value in the list
# print(max(a)) # 6 is the max element

# #min() returns minimum value of the list
# print(min(a)) 

# #sum() method return the sum of all elements in the list
# print(sum(a)) # sum is 21

# #average of the list
# print(sum(a)/len(a)) # return an average (which is 3.0)


# myList = list()
# while(True):
#     inp = input('Enter a number ')
#     if inp == 'done':
#         break
#     value = float(inp)
#     myList.append(value)


# print('Average', (sum(myList)/len(myList)))

# -----------------List and Strings -------------------------
# a = 'spam'
#if convert string to list
# b = list(a)
# print(b)

# a = 'spam spam spam'
# b = a.split()
# print(b) # creates a list with 3 spams, since they have a space between them

# a = 'spam1-spam2-spam3'
# delimiter = '-'
# b = a.split(delimiter) # they take - as space 
# c = a.split('-') #same thing different implikation
# print(b)
# print(c)

#joint
# a = 'spam-spam1-spam2'
# delimeter = 'a'
# b = a.split(delimeter) # founds a and take a as space and therefore a enumelates
# print(b)

# myList = [2,4,3,1,5,7]

# myList = myList.sort()
# print(myList)

# myList.append(10)
# print(myList)

# myList = myList + [10]
# print(myList)

# myList = [2,4,6,1,10]
# orig = myList[:]
# myList.sort()
# # myList.append([10]) #appends [10]
# # myList.sort() # mistake cannot sort with [10]
# print(myList)
# print(orig)

# myList = [2,4,6,1,10]
# myList.sort() #returns sorted list
# print(myList)


# ------------------ Arrays vs list ----------------
import numpy as np
# Both data structures are mutable(can add smth replace etc)
# Both can be indexed and iterated through
# The can be both sliced

#differences

#arrays is better in - arithmetic operations

# myArray = np.array([1,2,3,4,5,6])
# myList = [1,2,3,4,5] 

# print(myArray/2) #every element is divided by two
# print(myList/2) #error


#List ---- Data types

# myArray = np.array([1,2,3,4,5,6,'a'])
# myList = [1,2,3,4,5,'a']

# print(myArray) #converted as string
# print(myList)  # numbers - integer, letter-string

# -------------------------- List Comprehension ---------------------

# new_list = [new item for item in list]

# prev_list = [1,2,3]
# new_list = [i*2 for i in prev_list]
# print(prev_list)
# print(new_list) # multiplies every element by 2

# lamguage = 'Python'
# new_list = [letter for letter in lamguage]
# print(new_list) #print every letter in list

#you can use list comprehension when dealing with : List,Range,String,Tuple

# ------------------------------- Conditional List comprehension ----------------

# new_list = [new_item for item in list if condition]

# prev_list = [-1,10,-20,2,-90,60,45,20]
# new_list = [item for item in prev_list if item>0] #only positive numbers
# print(new_list)

# new_List = [item**2 for item in prev_list if item<0] #negative numbers squared
# print(new_List)

# sentence = 'My name is Gleb'
# print(sentence.isalpha()) #return True if all characters are in alphabetic order

# def is_consonant(letter):
#     vowels = 'aeiou'
#     return letter.isalpha() and letter.lower() not in vowels

# print(is_consonant('a')) #false because a is vowel

# print(is_consonant('t')) #true because not a vowel

# consonants = [i for i in sentence if is_consonant(i)]
# print(consonants) #print all consonants

# prev_list = [-1,10,-20,2,-90,60,45,20]
# new_list = [number if number >0 else 0 for number in prev_list] #if zero-print, if negative print 0
# print(new_list)

# prev_list = [1,20,35-20,5,15,-100,45,20]
# new_listik = [item if item<0 else 'positive number' for item in prev_list] #positives are 0
# print(new_listik)

# --------------------------------------------------------------------#

# def get_number(number):

#     # if number >0:
#     #     return number
#     # else:
#     #     return 'negative number'

#     return number if number>0 else 'negative number'

# prev_list = [-1,10,-20,2,-90,60,45,20]
# new_list = [get_number(number) for number in prev_list]
# print(new_list)

#----------------------------------------------------------------------#

# def f(value, values): # 44,2,3
#     v = 1
#     values[0] = 44
# t = 3
# v = [1, 2, 3]
# f(t, v)
# print(t, v[0]) 

# fruit_list1 = ['Apple', 'Berry', 'Cherry', 'Papaya']
# fruit_list2 = fruit_list1
# fruit_list3 = fruit_list1[:]
 
# fruit_list2[0] = 'Guava' # Guava 'Berry', 'Cherry', 'Papaya'
# fruit_list3[1] = 'Kiwi' #'Apple', 'Kiwi', 'Cherry', 'Papaya'
 
# sum = 0
# for ls in (fruit_list1, fruit_list2, fruit_list3):
#     if ls[0] == 'Guava':
#         sum += 1
#     if ls[1] == 'Kiwi':
#         sum += 20
 
# print(sum)
# import random
# fruit=['apple', 'banana', 'papaya', 'cherry']
# random.shuffle(fruit)
# print(fruit)

# data = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
# def fun(m):
#     v = m[0][0]
 
#     for row in m:
#         for element in row:
#             if v < element: v = element
 
#     return v
# print(fun(data[0]))


# a=[1,2,3,4,5,6,7,8,9]
# a[::2]=10,20,30,40,50,60
# print(a)

for i in range(1,6):
    print(i)

arr = [1, 2, 3, 4, 5, 6]
for i in range(1, 6):
    arr[i - 1] = arr[i]

print(arr)