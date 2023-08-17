def processa_sala():
    cont_ehd = 0
    cont_epr = 0
    cont_outros = 0

    n_alunos = int(input())
    for _ in range(n_alunos):
        _, curso = input().split()

        if curso == "EHD":
            cont_ehd += 1
        elif curso == "EPR":
            cont_epr += 1
        else:
            cont_outros += 1

    print(f"EPR: {cont_epr}")
    print(f"EHD: {cont_ehd}")
    print(f"INTRUSOS: {cont_outros}")


# código principal
while True:
    try:
        processa_sala()
    except EOFError:
        break
