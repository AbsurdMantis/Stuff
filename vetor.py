
lin = 0
col = 0
matriz = []
while lin < 5:
    linha = []
    col = 0
    while col < 2:
        num = int(input(f"Número: "))
        linha.append(num)
        col+=1
    matriz.append(linha)
    lin+=1

print(matriz)

for linha in matriz:
    for coluna in linha:
        print(coluna, end=' ')
    print(" ")



    
