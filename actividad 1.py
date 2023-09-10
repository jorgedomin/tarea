a = [[15,11,14],[23,25,19],[19,22,23]]
for x in range (len(a)):
    a[x]=sorted(a[x])
print(a)
numero = int(input("Ingresa el número:  "))
for i in range(len(a)):
    for j in range(len(a[i])):
        if a [i][j] == numero:
            print (f"el número{numero} se envuentra en la fila{[i]}  y en la columna {[j]}")