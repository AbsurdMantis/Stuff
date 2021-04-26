import matplotlib.pyplot as plt

x = [3, 5, 7, 9]
y = [2, 4, 7, 8]
z = [10.,20,30, 69]#tamanhho de cada ponto

title = "Yoshikage Kira Kills"
Xaxis = "Kills"
Yaxis = "Time"


plt.title(title)
plt.xlabel(Xaxis)
plt.ylabel(Yaxis)

plt.scatter(x, y, label= "Women", color = "g", marker = "x", s=z)#s eh pra o tamanho do marker kkkkkk
plt.plot(x, y, color = "000000", linestyle = "--")#tambem   eh possivel usar em numero as   cozrinha

plt.legend()
plt.show()
plt.savefig("graph1scatter.pdf")#como pdf eh vetorial eh melhor pra aplicacao cientifica, png pra imagem msmo fodass
plt.savefig("graph1scatter.png", dpi = 1200)#300 ta bom mas revista pede 1200 fodass

