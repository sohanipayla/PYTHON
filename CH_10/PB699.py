import matplotlib.pyplot as plt
animals = ['Zebra', 'Lions', 'Monkeys', 'Elephants', 'Ostriches']
counts = [25, 5, 50, 10, 20]
plt.scatter(animals, counts, color='red', marker='o')
plt.xlabel("Type of Animal")
plt.ylabel("Number of Animals")
plt.title("Zoo Animal Population")
plt.show()