n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
for i in set(arr):
    print(i, ":", arr.count(i))
