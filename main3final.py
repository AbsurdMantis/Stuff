def validationError():
    return "to end"

inputAP1 = input("Insira o valor da aposta do primeiro jogador:")
if float(inputAP1) < 0:
    print("Não é possível apostar valores menores que 0")
else:
    try:
        int(inputAP1)
    except ValueError:
        try:
            float(inputAP1)
        except ValueError:
            exit ("O valor de aposta não é válido") 
        
inputAP2 = input("Insira o valor da aposta do segundo jogador:")
try:
    int(inputAP2)
except ValueError:
    try:
        float(inputAP2)
    except ValueError:
        validationError()
        
inputAP3 = input("Insira o valor da aposta do terceiro jogador:")
try:
    int(inputAP3)
except ValueError:
    try:
        float(inputAP3)
    except ValueError:
        print ("O valor de aposta não é válido")
       
inputT = (float(inputAP1) + float(inputAP2) + float(inputAP3))
try:
    int(inputT)
except ValueError:
    try:
        float(inputT)
    except ValueError:
        print ("O valor de aposta não é válido")
       
inputP = input("Insira o prêmio atualmente acumulado:")
try:
    int(inputP)
except ValueError:
    try:
        float(inputP)
    except ValueError:
        print ("O valor de aposta não é válido")
       
premio = float(inputAP1) + float(inputAP2) + float(inputAP3) + float(inputP)

z = int(inputAP1)/int(inputT)
x = int(inputAP2)/int(inputT)
y = int(inputAP3)/int(inputT)
   
AP1 = premio*z
AP2 = premio*x
AP3 = premio*y

print(AP1)
print(AP2)
print(AP3)
