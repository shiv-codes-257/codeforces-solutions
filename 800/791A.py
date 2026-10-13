a,b = map(int,input().split())
count = 0
for i in range(10):
    if a*3 <= b*2:
        count +=1 
print(count)