px1, py1= input().split()
px1= float(px1)
py1= float(py1)

px2, py2= input().split()
px2= float(px2)
py2= float(py2)

distancia= ((px2-px1)**2+ (py2-py1)**2)**(1/2)

print(f"{distancia:.4f}")
