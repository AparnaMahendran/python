n = int(input())
arr = []
for i in range(n-1):
    arr.append(int(input()))
total = n*(n+1)//2
print("Missing Number:", total-sum(arr))
