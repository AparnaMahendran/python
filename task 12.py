n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
new = []
for i in arr:
    if i not in new:
        new.append(i)
print(new)
