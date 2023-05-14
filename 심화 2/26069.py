n = int(input())

dance = set()
dance.add("ChongChong")

for _ in range(n):
    t1, t2 = input().split()

    if t1 in dance:
        dance.add(t2)

    if t2 in dance:
        dance.add(t1)

print(len(dance))
