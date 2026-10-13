n,l,r = map(int,input().split())
s = list(map(str,input()))
if s[l-1]<="o"<=s[r-1] and (len(s)) < n or (len(s)) > n:
    print("No")
elif s[l-1]<="o"<=s[r-1] and len(s) == n:
    print("Yes")
else:
    print("No")