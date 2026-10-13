s = input()
t = input()
if ''.join(reversed(s)) == t:
    print("YES")
else:
    print("NO")


    #we could use the above ''.join(reveresed(s)) to reverse the string, or we could use string slicing, which s[::-1] to reverse the string the square brackets are need to slice it and treat as a string dont forget