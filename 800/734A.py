n = int(input())
results = input()
count_a = 0
count_d = 0
for i in results:
    if i == "A":
        count_a += 1
    if i == "D":
        count_d += 1
if count_a > count_d:
    print("Anton")
elif count_a < count_d:
    print("Danik")
elif count_a == count_d:
    print("Friendship")