n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
key = int(input())
if key in arr:
    print("Found at", arr.index(key))
else:
    print("Not Found")
