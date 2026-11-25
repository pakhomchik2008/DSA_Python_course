# insert daily temperatures to our program and program should return average of this temperature and irt needs to finds a number of days above the average temperature

# n = int(input('How many days\'s temperature? '))
# total = []
# for i in range(n):
    
#     answer = int(input(f'Day {i+1}s high temp: '))
#     total.append(answer)

# average = sum(total)/len(total)
# print(f'Average {average}')

# count = 0
# for i in total:
#     if average < float(i):
#         count+=1
# print(f'{count} Day(s) above the average')


# def missing_number1(arr, n):
#     for i in range(arr[1],n+1):
#         if i not in arr:
#             return i
# print(missing_number1([1,2,3,4,5,6,7,8,10], 10)) # 5
# #time complexity - O(n^2) --- not efficient


# def missing_number(arr, n):
#     total = n * (n + 1) // 2
    
#     # Calculate the sum of numbers in the array
#     sum_arr = sum(arr)
    
#     # Find the missing number by subtracting sum_arr from total
#     missing = total - sum_arr
    
#     return missing
        

# print(missing_number([1,2,3,4,5,6,7,8,10], 10)) # 5

# # time complexity - O(n) - efficient

# def pairsofIntegers(newlist,target):
#     list = sorted(newlist)
#     l=0
#     r=len(list)-1

#     while(l!=r):
#         if list[l]+list[r] > target:
#             r-=1
#         if list[l]+list[r] < target:
#             l+=1
#         if list[l] + list[r] == target:
#             return [list[l], list[r]]
        

        