n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
print("Maximum Difference:", max(arr)-min(arr))
