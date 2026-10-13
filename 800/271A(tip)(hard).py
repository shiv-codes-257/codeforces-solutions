
y = int(input())
for i in range(y+1,10000000):
    if len(str(i)) == len(set(str(i))):
        print(i)
        break


    #in a for loop it starts the loop from the number itself in a range, or from the first number, and ends a number before the end range, so to not include the first number when going through the loop, if we dont want to ofc, we do y+1 for eg (y,9000), we do (y+1,9000), to not include the first number, when going through other numbers

    #we use break if we only want to go through the loop once, and stop.

    #learnt what is set, we use set, when we want to remove duplicates from an integer, or a string etc.    


'''
y = int(input())
i = y+1
while True:
    if len(str(i)) == len(set(str(i))):
        print(i)
        break
    i += 1
    
'''

#above is another way of writing code, it is more efficient, we use while true as it as an endless loop, and therefore to stop it , we use break, and it gives us the same result
