n= int(input())

for i in range(n):
    x= int(input())
    divisores=[]

    for t in range(1,x):
        if x%t == 0:
            divisores.append(t)

    if sum(divisores) == x:
        print(f"{x} eh perfeito")
    else:
        print(f"{x} nao eh perfeito")
