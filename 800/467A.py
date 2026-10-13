n = int(input())
count= 0
for values in range(n):
    p,q = map(int,input().split())
    if q - p < 2:
        count += 0
    elif q - p >=2 :
        count += 1
print(count)

#no need to add extra for loops for no reason if not required, think  properly

#print always needs to be in line with the first for loop, when printing only once