n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
smallest = arr[0]
for i in arr:
    if i < smallest:
        smallest = i
print("Smallest:", smallest)
