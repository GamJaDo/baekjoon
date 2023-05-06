n = int(input())

a = 2
result = a**2

for i in range(n):
    b = 2**i
    a += b
    result = (a)**2

print(result)
