n,h =  map(int,input().split())
a = list(map(int,input().split()))
width = n
for i in a:
    if i > h:
        width += 1
print(width)