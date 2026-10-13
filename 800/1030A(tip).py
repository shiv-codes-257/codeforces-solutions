
''''
n = int(input())
opinion = list(map(int,input().split()))
problem = ""
for i in opinion:
    if i == 1:
        problem = "HARD"
    else:
        problem = "EASY"
print(problem)

'''

#the above code is fine, but is long and unneccessary u dont need a for loop to just go through a list, unless u want to examine it or do something specific it, u only need to use an if function if u want to go through the items in a list, as shown in the code below"

n = int(input())
opinion = list(map(int,input().split()))
if 1 in opinion:
    print("HARD")
else:
    print("EASY")
