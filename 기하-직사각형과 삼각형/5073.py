while True:

    line = list(map(int, input().split()))
    line.sort()
    
    if line[0]==0 and line[1]==0 and line[2]==0:
        break

    if line[0]+line[1] <= line[2]:
        print("Invalid")
    elif line[0]==line[1] and line[1]==line[2] and line[0]==line[2]:
        print("Equilateral")
    elif line[0]==line[1] or line[1]==line[2] or line[0]==line[2]:
        print("Isosceles")
    elif line[0]!=line[1] and line[1]!=line[2] and line[0]!=line[2]:
        print("Scalene")
