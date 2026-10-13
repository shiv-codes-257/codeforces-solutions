t = int(input())
count = 1
for values in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    for i,j in zip(a,b):
        if i > j:
            i -= 1 
            count += 1
        if i < j:
            j += 1
            count += 1
print(count)