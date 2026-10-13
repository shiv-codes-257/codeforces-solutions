n = int(input())
s = input()
count = 0
for i in s:
    for j in s:
        if i == j:
            
            count += 1
        elif i != j:
            count += 0
print(count)