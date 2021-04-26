
while True:
  try:
    inputAP1 = float(input("Insira o valor da aposta do primeiro jogador:"))
    inputAP2 = float(input("Insira o valor da aposta do segundo jogador:"))
    inputAP3 = float(input("Insira o valor da aposta do terceiro jogador:"))
    inputP = float(input("Insira o prêmio atualmente acumulado:"))
    break
  except:
      print("invalido")

if float(inputAP1) < 0 or float(inputAP2) < 0 or float(inputAP3) < 0:
 print("Nao existe aposta negativa")
elif float(inputAP1) + float(inputAP2) + float(inputAP3) == 0:
  print("Nao foram feitas apostas")
elif float(inputP) < 0:
  print("Nao tem premio negativo")
elif float(inputP) == 0:
  print("Nao tem premio acumulado")
else:
  inputT = (inputAP1 + inputAP2 + inputAP3)
  z = float(inputAP1)/float(inputT)
  x = float(inputAP2)/float(inputT)
  y = float(inputAP3)/float(inputT)

  premio = float(inputAP1) + float(inputAP2) + float(inputAP3) + float(inputP)

  AP1 = premio*z
  AP2 = premio*x
  AP3 = premio*y

  print(premio,"BRL  É o prêmio total acumulado")
  print(AP1,"BRL  É quanto recebe o apostador 1")
  print(AP2,"BRL  É quanto recebe o apostador 2")
  print(AP3,"BRL  É quanto recebe o apostador 3")




