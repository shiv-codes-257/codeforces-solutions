t = int(input())
for values in range(t):
    count = 0
    n,c = map(int,input().split())
    a = list(map(int,input().split()))
    new_a = []
    for i in a:
        if i > c:
            del i
            count += 1
        elif i <= c:
            del i
            count += 0
            for num in a:
                new_a.append(num*2)
                for j in new_a:
                    if j > c:
                        del j
                        count += 1
                    elif j <= c:
                        del j
                        count+=0
    print(count)
