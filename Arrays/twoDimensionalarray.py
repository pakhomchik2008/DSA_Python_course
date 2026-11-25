import numpy as np

# twoDArray = np.array([[11,15,10,6],[10,14,11,5],[12,17,12,8],[15,18,14,9]])
# print(twoDArray)

#time complexity --> O(mn) because we have m number of columns and n number of rows


# ------------- Insertion (2D Array)---------------

# time complexity for inserting rows and columns -----> O(m,n)
# space compplexity ---> O(mn)


# twoDArray = np.array([[11,15,10,6],[10,14,11,5],[12,17,12,8],[15,18,14,9]])
# print(twoDArray)

# newTwoDArray = np.insert(twoDArray, 0,[1,2,3,4], axis=1) #inserted a column , axis=1 is a column
# print(newTwoDArray)


# newTwoDArray = np.insert(twoDArray, 0,[1,2,3,4], axis=0) #inserted a row , axis=0 is a column
# print(newTwoDArray)

# newTwoDArray = np.insert(twoDArray, 1,[1,2,3,4], axis=0) #inserted a row(index1) , paxis=0 is a column
# print(newTwoDArray)

# newTwoDArray = np.append(twoDArray,[[1,2,3,4]],axis=0) # new row must be 2D: [[...]]
# print(newTwoDArray)


#--------------------------------- Accessing elements in 2D Array ----------------------
# twoDArray = np.array([[11,15,10,6],[10,14,11,5],[12,17,12,8],[15,18,14,9]])
# print(twoDArray)
# def accessElements(array,rowIndex,colIndex): 
#     if rowIndex>=len(array) or colIndex >= len(array[0]): #----->O(1)
#         print('incorrect index')    #----->O(1)
#     else:
#         print(array[rowIndex][colIndex]) #----->O(1)

# accessElements(twoDArray,1,2) #element 11 is in 1 row and 2 column
# accessElements(twoDArray,2,3) #element 11 is in 2 row and 3 column

#len(array) - return number of rows
#len(array[0]) - return number of rows
#time complexity ------->O(1)
#Space complexity ------>O(1)

# --------------------- Traversing elements in 2D Array -------------

# we start from array[0][0] and continue s.t array[0][1] and so on
# you have to finsh with the first row and than carry on to next row

# twoDArray = np.array([[11,15,10,6],[10,14,11,5],[12,17,12,8],[15,18,14,9]])
# print(twoDArray)
# def traverseTDArray(array): 
#     for i in range(len(array)): #will return number of rows --------->O(mn)
#         for j in range(len(array[0])): # will return number of columns ---->0(n)
#             print(array[i][j]) # i-row , j-column ------->O(1)

# traverseTDArray(twoDArray)

#time complexity ----> O(m,n) 
# if number of rows = number of columns ---->0(n^2) because n=m
# Space compelxity = O(1)


# ------------------- Searching for an Element in 2D Array ----------
# if the given value exist in an array or not

# linear search - search through every el and check if it is the el we looking for
#starts from the 1 el
# twoDArray = np.array([[11,15,10,6],[10,14,11,5],[12,17,12,8],[15,18,14,9]])
# print(twoDArray)

# def searchTDArray(array, value):
#     for i in range(len(array)):
#         for j in range(len(array[0])):
#             if array[i][j] == value:
#                 return 'The value is located at index ' + str(i)+',' + str(j)
#     return 'The element is not found'

# print(searchTDArray(twoDArray,14))
# #it returns the first occurence of 14

# print(searchTDArray(twoDArray,114))

# Time complexity ------>O(mn)
# Space complexity -----> 0(1)

# --------------------- Deletion of column or row in 2D Array --------------

# whether u delete row or column numpy creates a new 2D array
# time complexity ---->O(mn) cause u copy all the left numbers
# Space compelxity ---->0(mn) 

# twoDArray = np.array([[11,15,10,6],[10,14,11,5],[12,17,12,8],[15,18,14,9]])
# print(twoDArray)

# newTDArray = np.delete(twoDArray,0,axis=0) #should delete first row of the array
# print(newTDArray)

# newTDArray = np.delete(twoDArray,0,axis=1) #should delete first column of the array
# print(newTDArray)



# ------ WHen to use/avoid avoid Arrays ---------------
# When to Use:
# - To store multiple variables of same data type
# - Random access

# When to avoid:
# - Same data type elements
# - Reserve memory
