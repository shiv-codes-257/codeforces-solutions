s = input()
count_upper = 0
count_lower = 0
for letter in s:
    if letter.isupper():
        count_upper += 1
    elif letter.islower():
        count_lower += 1
    if count_upper > count_lower:
        s = s.upper()
    elif count_lower > count_upper:
        s = s.lower()
    elif count_upper == count_lower:
        s = s.lower()
print(s)

#need to think when and where to use for loop or any loop appopriately.

#if u use print in the for loop again and again it will it those many time, so if u want to print something and have many if conditions, just put print after the functions in the loop havee finished

#recheck for correct answer later