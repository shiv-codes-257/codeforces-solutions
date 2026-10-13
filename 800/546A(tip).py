k,n,w = map(int,input().split())
price = 0
for i in range(1,w+1):
    price += i*k
    borrow = price - n
    if borrow <= 0:
        borrow = 0
print(borrow)


#had to look at the range, as the range for a list always starts from 0
#needed to apply logic, that if the amount borrowed, is less than 0 or equal to 0 then he doesnt need to borrow money.