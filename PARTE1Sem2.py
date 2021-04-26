
while True:
  try:
    input1 = float(input("Insira o valor do salário atual do funcionário:"))
    input2 = float(input("Insira o tempo de serviço do trabalhador em anos:"))
    break
  except:
  	print("Insira apenas números")


if input1 <= 0 or input2 <= 0:
  print("Não são permitidos valores como 0, muito menos salário negativo ou tempo negativo")
  exit
elif input1 < 500:
	input500 = input1*1.25
	if input2 <1:
		print(input500, "O salário teve apenas reajuste, não houve bônus")
	elif 1 < input2 < 3:
		print(input500 + 100, "O salário teve reajuste e bônus de 100 BRL")
	elif 4 < input2 < 6:
		print(input500 + 200, "O salário teve reajuste e bônus de 200 BRL")
	elif 7 < input2 < 10:
		print(input500 + 300, "O salário teve reajuste e bônus de 300 BRL")
	elif input2 > 10:
		print(input500 + 500, "O salário teve reajuste e bônus máximo de 500 BRL")
	else:
		print("Tempo de serviço inválido")
elif 1000 < input1 < 1500:
	input100 = input1*1.20
	if input2 <1:
		print(input500, "O salário teve apenas reajuste, não houve bônus")
	elif 1 < input2 < 3:
		print(input500 + 100, "O salário teve reajuste e bônus de 100 BRL")
	elif 4 < input2 < 6:
		print(input500 + 200, "O salário teve reajuste e bônus de 200 BRL")
	elif 7 < input2 < 10:
		print(input500 + 300, "O salário teve reajuste e bônus de 300 BRL")
	elif input2 > 10:
		print(input500 + 500, "O salário teve reajuste e bônus máximo de 500 BRL")
	else:
		print("Tempo de serviço inválido")
elif 1500 < input1 < 2000:
	input150 = input1*1.15
	if input2 <1:
		print(input150, "O salário teve apenas reajuste, não houve bônus")
	elif 1 < input2 < 3:
		print(input150 + 100, "O salário teve reajuste e bônus de 100 BRL")
	elif 4 < input2 < 6:
		print(input150 + 200, "O salário teve reajuste e bônus de 200 BRL")
	elif 7 < input2 < 10:
		print(input150 + 300, "O salário teve reajuste e bônus de 300 BRL")
	elif input2 > 10:
		print(input150 + 500, "O salário teve reajuste e bônus máximo de 500 BRL")
	else:
		print("Tempo de serviço inválido")
elif input1 < 2000:
	input200 = input1*1.10
	if input2 <1:
		print(input200, "O salário teve apenas reajuste, não houve bônus")
	elif 1 < input2 < 3:
		print(input200 + 100, "O salário teve reajuste e bônus de 100 BRL")
	elif 4 < input2 < 6:
		print(input200 + 200, "O salário teve reajuste e bônus de 200 BRL")
	elif 7 < input2 < 10:
		print(input200 + 300, "O salário teve reajuste e bônus de 300 BRL")
	elif input2 > 10:
		print(input200 + 500, "O salário teve reajuste e bônus máximo de 500 BRL")
	else:
		print("Tempo de serviço inválido")
elif input1 >= 2000:
	if input2 <1:
		print(input1, "O salário teve apenas reajuste, não houve bônus")
	elif 1 < input2 < 3:
		print(input1 + 100, "O salário teve reajuste e bônus de 100 BRL")
	elif 4 < input2 < 6:
		print(input1 + 200, "O salário teve reajuste e bônus de 200 BRL")
	elif 7 < input2 < 10:
		print(input1 + 300, "O salário teve reajuste e bônus de 300 BRL")
	elif input2 > 10:
		print(input1 + 500, "O salário teve reajuste e bônus máximo de 500 BRL")
	else:
		print("Tempo de serviço inválido")

