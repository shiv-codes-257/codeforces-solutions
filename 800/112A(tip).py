a = str(input())
b = str(input())
if a.lower() == b.lower() or  a == b:
    print("0")
elif a.lower() > b.lower():
    print("1")
elif a.lower() < b.lower():
    print("-1")

    #learnt how to use lower and upper for words and letters. lower converts string to lowercase and vice versa. 

    #we can compare words and letters as well, depending on which one is bigger/smaller.
    