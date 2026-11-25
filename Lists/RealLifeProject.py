# insert daily temperatures to our program and program should return average of this temperature and irt needs to finds a number of days above the average temperature

n = int(input('How many days\'s temperature? '))
total = []
for i in range(n):
    
    answer = int(input(f'Day {i+1}s high temp: '))
    total.append(answer)

average = sum(total)/len(total)
print(f'Average {average}')

count = 0
for i in total:
    if average < float(i):
        count+=1
print(f'{count} Day(s) above the average')