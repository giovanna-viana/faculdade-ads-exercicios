x=[]

for i in range(10):
    n = int(input())
    if n <= 0:
        n = 1
        x.insert(i,n)
    else:
        x.insert(i,n)

    print(f"X[{i}] = {n}")

