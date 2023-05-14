n = int(input())

cnt = 0
user = set()

for _ in range(n):

    s = input()
    
    if s != 'ENTER':
        if s not in user:
            cnt += 1
            user.add(s)
    else:
        user = set()

print(cnt)
