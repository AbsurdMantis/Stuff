
while True:
  try:
    inputH = float(input("Insira a altura do reservatório em centímetros:"))
    inputW = float(input("Insira a largura do reservatório em centímetros:"))
    inputL = float(input("Insira o comprimento do reservatório em centímetros:"))
    inputA = float(input("Insira o consumo diario de litros de água:"))
    break
  except:
      print("invalido")

if inputH <= 0 or inputW <= 0 or inputL <= 0:
  print("Não existem dimensões negativas em geometria")
  exit()
elif inputA <= 0:
  print("Não existe consumo diário negativo ou 0")
  exit()


inputV = inputH * inputW * inputL/1000
inputT = inputV/inputA

def Consumption():
	if inputT < 2:
		print("Consumo elevado de água para as dimensões")
	elif 2 <= inputT < 7:
		print("Consumo moderado de água para as dimensões")
	elif inputT >= 7:
		print("Consumo baixo de água para as dimensões")
	else:
		print("Consumo de água inválido")


print(inputV, "L  é a capacidade total do reservatório")
print(inputT, "Dias de autonomia para as dimensões do reservatório")
Consumption()
