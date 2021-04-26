# -*- coding: utf-8 -*-
while True:
  try:
    inputHouse = float(input("Informe o valor do imóvel a ser comprado:"))
    inputSalary = float(input("Informe o salário que você recebe:"))
    inputYears = float(input("Informe a quantidade de anos a pagar:"))
    break
  except:
      print("Insira apenas números")
if float(inputHouse) < 0 or float(inputSalary) < 0 or float(inputYears) < 0:
  print("Não é possível números negativos. Tente novamente.")
elif float(inputHouse) == 0 or float(inputSalary)== 0 or float(inputYears) == 0:
  print("O valor informado não pode ser 0. Tente novamente.")
else:
  inputTime = float (inputYears) * 12
  K = 0.3 * float (inputSalary)
  Z = float (inputHouse)/ float (inputTime)

  if Z > K:
    print("Seu salário não atinge a alíquota da prestação da casa")
  else:
    print (Z, "BRL  é o valor da prestação que você deverá pagar.")
