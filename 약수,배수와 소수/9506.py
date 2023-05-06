measure = [1]

while True:
    measure = [1]
    n = int(input())

    if n == -1:
        break
    
    for i in range(2, n):
        if n%i == 0:
            measure.append(i)
    
    if n != sum(measure):
        print(n, "is NOT perfect.")
    else:
        print(n, '=', end = ' ')
        for i in measure:
            print(i, end = ' ')
            if measure[len(measure)-1] != i:
                print("+", end = ' ')
        print()
