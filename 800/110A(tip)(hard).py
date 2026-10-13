n = int(input())
lucky_count = 0
for i in str(n):
    if i == "4" or i == "7":
        lucky_count += 1
if lucky_count == 4 or lucky_count == 7:
    print("YES")
else:
    print("NO")

    #if u want to print something once, but ur writing inside a for loop, then you should move the print or the if function outside the for loop,

    #if u want to iterate through a string, then you should convert it a string first.