t= int(input())
v=0

for i in range(10):
    print(f"N[{i}] = {v}")
    v+=1
    if v==t:
        v=0
