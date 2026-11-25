# def pairsofIntegers(newlist,target):
#     for i in range(len(newlist)):
#         for j in range(i+1,len(newlist)):
#             if newlist[i] == newlist[j]:
#                 continue
#             if newlist[i]+newlist[j] == target:
#                 return i,j

# def two_sum(nums, target):
#     seen = {}
    
#     for i, num in enumerate(nums):
#         complement = target - num
        
#         if complement in seen:
#             return [seen[complement], i]
        
#         seen[num] = i
 
# nums = [2, 7, 11, 15]
# target = 9
# indices = two_sum(nums, target)
# print(f"Indices of the two numbers are: {indices}")
            
        
# lst = [3,2,4]
# target = 6
# print(pairsofIntegers(lst,target))

import numpy as np

# myArr = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])

# def findNumber(array,number):
#     for i in range(len(array)):
#         if array[i] == number:
#             return i
#     return -1

# print(findNumber(myArr,101))

arr = [1, 7, 3, 4, 9, 5] 

# def muxProduct(arr):
#     max = arr[0]*arr[1]
#     for i in range(len(arr)):
#         for j in range(i+1,len(arr)):
#             if max<= arr[i]*arr[j]:
#                 max = arr[i]*arr[j]
#     return max


# def max_product(arr):
#     max1,max2  = 0,0
#     for num in arr:
#         if max1<num:
#             max2= max1
#             max1=num
#         elif num >max2:
#             max2=num
#     return max1*max2


# print(max_product(arr)) # Output: 63 (9*7)


# list = [1, 2, 3, 4]
# def middle(lst):
#     return lst[1:-1]

# print(middle(list))


# def diagonal_sum(matrix):
#     lst = []
#     for i in range(len(matrix[0])):
#         lst.append(matrix[i][i])
#     return sum(lst)
    
# myList2D= [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
#     ] 

# print(diagonal_sum(myList2D))

# myList = [84,85,86,87,85,90,85,83,23,45,84,1,2,0]

# def first_second(my_list):
#     max1,max2 = 0,0

#     for num in myList:
#         if max1<num:
#             max2 = max1
#             max1 = num
#         elif max2<num:
#             max2 = num
#     return max1,max2

# print(first_second(myList))

# def remove_duplicates(arr):
#     lst = []
#     for i in arr:
#         if i not in lst:
#             lst.append(i)

# remove_duplicates([1, 1, 2, 2, 3, 4, 5])

# def pair_sum(myList, sum):
#     lst = []
#     for i in range(len(myList)):
#         for j in range(i+1,len(myList)):
#             if myList[i]+myList[j] == sum:
#                 lst.append(f'{str(myList[i])} + {str(myList[j])}')
#     return list(lst)


# print(pair_sum([2, 4, 3, 5, 6, -2, 4, 7, 8, 9],7))


# def contains_duplicate(nums):
#     seen = set()
#     for i in nums:
#         if i in seen:
#             return True
#         seen.add(i)

#     return False
    
    

# nums = [1,2,3,1]
# print(contains_duplicate(nums))

# Question 6 - Permutation(Palindrome)

# def permutation(list1,list2):
#     if len(list1) != len(list2): return False

#     list1.sort()
#     list2.sort()

#     if list1 == list2: return True
#     else: return False

# # list1 = ['a','b','c']
# # list2 = ['c','a','b']

# list1 = [1,3,2,4]
# list2 = [4,3,2,1]
# print(permutation(list1,list2))
