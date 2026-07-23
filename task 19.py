n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
m = int(input())
b = []
for i in range(m):
    b.append(int(input()))
print(list(set(a)&set(b)))
