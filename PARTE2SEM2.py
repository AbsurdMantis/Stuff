
def e():
	cuEuro = inputC*0.31
	print(cuEuro, "EUR  É o valor em euros")

def d():
	cuDolar = inputC*0.42
	print(cuDolar,"USD  É o valor em dólares")

def m():
	cuMexico = inputC*5.55
	print(cuMexico,"MEP  É o valor em pesos mexicanos")

def a():
	cuArgentino = inputC*2.84
	print(cuArgentino,"ARP  É o valor em pesos argentinos")

def l():
	cuLibra = inputC*0.26
	print(cuLibra,"GBP  É o valor em libras esterlinas")

print("-----", "Tabela de conversão", "-----")
print("Letra", "-----", "Moeda", "-----", "Valor")
print("e", "-----", "Euro", "-----", "0.31")
print("d", "-----", "Dolar", "-----", "0.42")
print("m", "-----", "P. Mexicano", "-----", "5.55")
print("a", "-----", "P. Argentino", "-----", "2.841")
print("l", "-----", "Libra", "-----", "0.26")

while True:
	try:
		inputC = float(input("Insira o valor em BRL que deseja converter:"))
		break
	except:
		print("invalido")



def cuLet():
	inputL = str(input("Insira a letra da moeda desejada para conversão:"))
	allowLet = 'edmal'
	while inputL not in allowLet:
		print("Moeda inexistente, tente novamente")
		inputL = str(input("Insira a letra da moeda desejada para conversão:"))
	if inputL == 'e':
		e()
	elif inputL == 'd':
		d()
	elif inputL == 'm':
		m()
	elif inputL == 'a':
		a()
	elif inputL == 'l':
		l()
	else:
		print("invalido")


if inputC <= 0:
	print("Valores iguais ou menores que 0 são inválidos")
else:
	cuLet()
