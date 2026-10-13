n, k = map(int,input().split())
a = list(map(int,input().split()))
count = 0
for i in a:
    if i >= a[k-1] and i>0:
        count += 1
    elif i >= a[k-1] and i<=0:
        count +=0
print(count)