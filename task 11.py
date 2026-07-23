n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
dup = []
for i in arr:
    if arr.count(i) > 1 and i not in dup:
        dup.append(i)
print(dup)
