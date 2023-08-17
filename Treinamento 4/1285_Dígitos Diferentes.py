def digitos_repetidos(n):
    digitos = []
    while n > 0:
        d = n % 10
        if d in digitos:
            return True
        digitos.append(d)
        n //= 10
    return False
        

def main():
    n, m = input().split()
    n = int(n)
    m = int(m)
    
    cont = 0
    for num in range(n, m+1):
        if not digitos_repetidos(num):
            cont += 1
    
    print(cont)

    
while True:
    try:
        main()
    except EOFError:
        break
