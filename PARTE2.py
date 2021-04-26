
# -*- coding: utf-8 -*-
class_inputValue = input("Insira o valor total do produto:")

PValue = float(class_inputValue)/3
DValue = float(class_inputValue)*0.9

if float(class_inputValue) <= 0:
    print("O produto não tem preço válido")
else:
    print(DValue, "BRL  É o valor com desconto de 10% à vista")
    print(PValue, "BRL  É o valor da parcela dividido em 3x sem juros")
    print(DValue*0.05, "BRL  É o valor de comissão do vendedor para a venda à vista")
    print(int(class_inputValue)*0.05, "BRL  É o valor da comissão do vendedor na venda parcelada")
