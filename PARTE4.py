
def patientname():
  for i in inputName:
    if "a"<=i<="z" or "A"<=i<="Z":
      return True
    else:
      return None
      
inputName = str(input("Indique o nome do paciente:"))
patientname()

while patientname() == None:
  if patientname() == True:
    continue
  else:
    print("nome invalido")
    inputName = str(input("Indique o nome do paciente:"))
    patientname()
  
while True:
  try:
    inputQuanty = int(input("Indique a quantidade de cigarros fumados por dia:"))
    inputime = float(input("Indique a quanto tempo o paciente é fumante em anos:"))
    break
  except:
    print("invalido")
if inputQuanty < 0 or inputime < 0:
 print("valor menor que 0 invalido")
elif inputQuanty == 0:
  print("fumo não pode ser 0")
elif inputime == 0:
  print("tempo não pode ser 0")
else:
  cig = 0.0069  
  time = int(inputime)*365
  timelost = int(inputQuanty) * cig * time
  horasd = float(timelost) - int(timelost)
  horasfloat = horasd * 24 
  horas = float(horasfloat) - int(horasfloat)
  hora = horasfloat - horas
  minutes = horas*60
  print(inputName, "perdeu ao todo:" , timelost - horasd, "dias, ", hora, "horas e",int(minutes),"minutos de vida.")
