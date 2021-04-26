import matplotlib.pyplot as plt

data = open("original.csv").readlines()

x = []
y = []

for i in range(len(data)):
	if i != 0:
		line1 = data[i].split(";")
		x.append(int(line1[0]))
		y.append(int(line1[1]))

plt.plot(x, y,  color = "k")
plt.bar(x, y, color = "#e4e4e4", linestyle= "-.")
plt.xlabel("Ano")
plt.ylabel("Populacao PPT")
plt.title("Crescimento Populacional 1980-2016")
plt.show()
plt.savefig("crescimentopop.png",  dpi = 350)