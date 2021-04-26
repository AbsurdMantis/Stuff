inputA = int(input("Insira o dividendo:"))
inputB = int(input("Insira o divisor:"))



rating = 0

while inputA > 0:
    if inputB <= inputA:
        inputA = inputA - inputB
        rating += 1
        if inputA == 0 or inputA < 0 or inputA < inputB:
            print(abs(inputA), "É o resto")
            #olhar o operador de módulo de python eu esqueci kk
            print(rating, "É o produto da divisão inteira")
            break
    elif inputB == 0:
        print("Não é possível dividir por 0")
    elif inputA > inputB:
        print("Esta operação não é permitida")
        #Não sei se ele queria só com naturais sendo assim teria de mudar os 
        #inputs pra float também, caso não é só alterar essa condição pra 
        #fazer a mesma divisão

    