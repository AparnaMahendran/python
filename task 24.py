n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
x = int(input())
for i in range(n-1,-1,-1):
    if arr[i] == x:
        print(i)
        break
