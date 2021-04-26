inputAP1 = input("Insira o valor da aposta do primeiro jogador:")
inputAP2 = input("Insira o valor da aposta do segundo jogador:")
inputAP3 = input("Insira o valor da aposta do terceiro jogador:")

inputP = input("Insira o prêmio atualmente acumulado:")
premio = float(inputAP1) + float(inputAP2) + float(inputAP3) + float(inputP)


input1 = float(inputAP1)
input2 = float(inputAP2)
input3 = float(inputAP3)
inputT = (input1 + input2 + input3)/100


print(float(premio), "BRL  É o prêmio total acumulado pelas apostas")
print(input1*inputT*premio*10/float(inputP), "BRL  É o valor adquirido pelo apostador 1")
print(input2*inputT*premio*10/float(inputP), "BRL  É o valor adquirido pelo apostador 2")
print(input3*inputT*premio*10/float(inputP), "BRL  É o valor adquirido pelo apostador 3")


