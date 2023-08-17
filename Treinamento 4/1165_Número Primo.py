def eh_primo(n):
    y = 2
    while y < n//2 + 1:
        if n % y == 0:
            return False
        y += 1
    return True


qtd_testes = int(input())
for _ in range(qtd_testes):
    x = int(input())
    if eh_primo(x):
        print(f'{x} eh primo')
    else:
        print(f'{x} nao eh primo')
