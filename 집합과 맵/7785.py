n = int(input())

log = {}

for i in range(n):
    name, enter = input().split()

    if enter == 'enter':
        log[name] = enter
    else:
        del log[name] # 필요없는건 삭제 //시간 때문
        
log = sorted(log.keys(), reverse = True) # 출력할 부분이 key이므로 key 기준으로 역순 출력(사전순)

for i in log:
    print(i)
