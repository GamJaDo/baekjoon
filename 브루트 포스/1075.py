n = input()
f = int(input())

n = int(n[:-2]+'00') #뒷2자리 인덱스 까지

while True:
    if n%f == 0:
        print(str(n)[-2:]) # 뒷 2자리만
        break
    n += 1
