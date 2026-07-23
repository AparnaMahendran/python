n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
even = odd = 0
for i in arr:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
print("Even:", even)
print("Odd:", odd)
