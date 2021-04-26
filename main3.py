inputName = input("Indique o nome do paciente:")
inputQuanty = input("Indique a quantidade de cigarros fumados por dia:")
inputime = input("Indique à quanto tempo o paciente é fumante em anos:")

inputime = float(inputime)
inputQuanty = float(inputQuanty)

cig = 0.0069
time = int(inputime)*365
timelost = int(inputQuanty) * cig * time
print(inputName, "perdeu ao todo:" , timelost, "dias de vida")
