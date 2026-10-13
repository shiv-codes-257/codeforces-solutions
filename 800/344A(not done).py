'''''
n = int(input())
count_01 = 0
count_10 = 0
for values in range(n):
    a = input()
    for i in str(a):
        if i == "01" :
            count_01 += 1
        elif i == "10":
            count_10 += 1
print((count_10+count_01))

'''

n = int(input())
count_01 = 0
count_10 = 0
remaining = 0
for values in range(n):
    a = input()
    count_01 += a.count("01")
    count_10 += a.count("10")
    
if count_01 % 2 != 0 or count_10 % 2 != 0:
    remaining +=1
print(((count_01//2)+(count_10//2))+remaining)





#you use .count("") to find any substring in a string, and count how many times it appears.