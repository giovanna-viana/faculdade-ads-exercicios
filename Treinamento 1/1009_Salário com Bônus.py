nome= input()
salario= float(input())
total_vendas= float(input())
comissao= total_vendas * 0.15
salario_final= salario + comissao
print(f"TOTAL = R$ {salario_final:.2f}")
