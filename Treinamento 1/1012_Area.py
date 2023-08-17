valores = input() .split()
a= float(valores[0])
b= float(valores[1])
c= float(valores[2])
a_triangulo= (a*c)/2
a_circulo= 3.14159 * c**2
a_trapezio= ((a+b)*c)/2
a_quadrado= b**2
a_retangulo= a*b
print(f"TRIANGULO: {a_triangulo:.3f}")
print(f"CIRCULO: {a_circulo:.3f}")
print(f"TRAPEZIO: {a_trapezio:.3f}")
print(f"QUADRADO: {a_quadrado:.3f}")
print(f"RETANGULO: {a_retangulo:.3f}")
