n = int(input())
x= 0
for values in range(n):
    user_input = input().strip()
    if user_input == "++X" or user_input == "X++":
        x+=1
    elif user_input == "--X" or user_input == "X--": 
        x-=1
print(x)
    

    #strip removes any whitespaces before or after the input or a text for eg "hello world    " and we use strip , then it prints hello by removing all the spaces.
    

    #if you define a variable or a number inside the for loop, then when the for loop resets it will lose the value and become the number again for eg. if we do x = 0 inside a for loop, and add 1, then it will add 1 but then return back to the for loop start, and x = 0 again, so if we want to maintain the value of a variable, then we take x = 0 outside the for loop.
