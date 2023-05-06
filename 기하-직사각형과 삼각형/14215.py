line = list(map(int, input().split()))
line.sort()

if line[0]+line[1] > line[2]:
    print(sum(line))
else:
    print(line[0]+line[1] + line[0]+line[1]-1)
#           ㄴ a+b            ㄴ 나머지 한변은 a+b보다 작아야 하지만
#최대한의 둘레를 구하는 문제이므로 a+b의 값에 1을 빼주면 최대 둘레가 나온다.
# 참고: https://codecollector.tistory.com/1440
