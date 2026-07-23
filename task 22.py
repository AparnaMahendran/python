n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
arr.sort()
key = int(input())

low = 0
high = n-1
while low <= high:
    mid = (low+high)//2
    if arr[mid] == key:
        print("Found at", mid)
        break
    elif arr[mid] < key:
        low = mid+1
    else:
        high = mid-1
else:
    print("Not Found")
