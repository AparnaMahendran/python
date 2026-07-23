n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
p = ne = z = 0
for i in arr:
    if i > 0:
        p += 1
    elif i < 0:
        ne += 1
    else:
        z += 1
print("Positive:", p)
print("Negative:", ne)
print("Zero:", z)
