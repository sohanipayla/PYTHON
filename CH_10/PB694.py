import matplotlib.pyplot as plt
D1 = {"aryan": 66, "bob": 70, "jack": 66, "seema": 34}
D2 = {"joy": 45, "sid": 85, "hina": 90}
names1, values1 = list(D1.keys()), list(D1.values())
names2, values2 = list(D2.keys()), list(D2.values())
plt.subplot(2, 1, 1) 
plt.bar(names1, values1, color='skyblue')
plt.subplot(2, 1, 2)
plt.barh(names2, values2, color='salmon')
plt.suptitle("BAR PLOT")
plt.tight_layout() 
plt.show()