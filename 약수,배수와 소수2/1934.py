n = int(input())

for i in range(n):
    a, b = map(int, input().split())

    while b != 0:
        r = a%b
        a = b
        b = r
    print(a)
