n, k = map(int, input().split())

measure = [1]
for i in range(2, n):
    if n%i == 0:
        measure.append(i)
measure.append(n)

if k <= len(measure):
    print(measure[k-1])
else:
    print('0')
