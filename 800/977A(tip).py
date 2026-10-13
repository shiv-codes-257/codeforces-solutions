n,k = map(int,input().split())
i = 0
while i<k:
    if n % 10 != 0:
        n -= 1
    elif n % 10 == 0:
        n /= 10

    i+=1
print(int((n)))

#learnt how to use the testcases thing with while loop, need to add +1 to i , define i as 0 for loop to work.

