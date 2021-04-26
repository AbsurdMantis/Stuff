import matplotlib.pyplot as plt
import random

vector = []

for i in range(20):
	num_random = random.randint(0, 20)
	vector.append(num_random)


plt.boxplot(vector)
plt.title("Box")
plt.show()