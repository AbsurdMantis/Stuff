inputAP1 = input("Insira o valor da aposta do primeiro jogador")
inputAP2 = input("Insira o valor da aposta do segundo jogador")
inputAP3 = input("Insira o valor da aposta do terceiro jogador")
aplist = [int(inputAP1), int(inputAP2), int(inputAP3)]
for x in aplist:
	x = x/100

inputP = input("Insira o prêmio atualmente acumulado")

premio = float(inputAP1) + float(inputAP2) + float(inputAP3) + float(inputP)
y = premio * x
print(y)