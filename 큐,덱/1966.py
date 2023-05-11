n = int(input())

def max(q):
    m = -1
    for i in range(len(q)):
        if q[i][0] > m:
            m = q[i][0]
            it = i

    return it

for _ in range(n):
    rank = 1
    index = 0
    
    q = []
    cnt, peek = map(int, input().split())

    temp = list(map(int, input().split()))
    p = (temp[peek], peek)
    
    for i in temp:
        q.append((i, index))
        index += 1
        
    max_value = q[max(q)]
    
    while True:
        t = q.pop(0)
        
        if max_value == t:
            if t == p:
                print(rank)
                break
            else:
                rank += 1
                max_value = q[max(q)]
        else:
            q.append(t)
