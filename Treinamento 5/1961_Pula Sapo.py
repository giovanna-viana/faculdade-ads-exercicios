def jogar(pulo, n, canos):
    for i in range(1, n):
        if abs(canos[i] - canos[i-1]) > pulo:
            return False

    return True


pulo, n = map(int, input().split())
canos = [int(x) for x in input().split()]

if jogar(pulo, n, canos):
    print('YOU WIN')
else:
    print('GAME OVER')
