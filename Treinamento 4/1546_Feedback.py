nomes = ["Rolien", "Naej", "Elehcim", "Odranoel"]

n = int(input())

for _ in range(n):
    k = int(input())

    for _ in range(k):
        feedback = int(input())

        print(nomes[feedback - 1])
