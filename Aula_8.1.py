while True:
    X1, Y1, X2, Y2 = map(int, input().split())

    if X1 == 0 and Y1 ==  0 and X2 == 0 and Y2 == 0:
        break
    if X1 == X2 and Y1 == Y2:
        print(0)
    elif X1 == X2 or Y1 == Y2:
        print(1)
    elif abs(X1 - X2) == abs(Y1 - Y2):
        print(1)
    else:
        print(2)