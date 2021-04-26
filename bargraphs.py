import matplotlib.pyplot as plt

x  = [1, 2, 3, 4 ,5, 6]
y = [2, 4 , 6, 8, 10, 12]

x2 = [2, 4 , 6, 8, 10, 12]
y2 = [2, 4, 7, 13, 24, 2]


title = "Crimes comitted in yugoslavia per month"
Xaxis = "Bimester"
Yaxis = "Crimes"

#Title
plt.title(title)
plt.xlabel(Xaxis)
plt.ylabel(Yaxis)


plt.bar(x,y, label = "2019")
plt.bar(x2,y2, label = "2020")
plt.legend()
plt.show() #coloca em barras(favor n  colocar os dois juntos como eu fiz isso   eh so pra demonstrar como escrevecada funcao separa ou usa so um bar pra barra plot pra linha)(x,y))