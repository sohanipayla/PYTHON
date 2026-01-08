import matplotlib.pyplot as plt
languages = ['Python', 'Java', 'Javascript', 'C#', 'PHP', 'C/C++', 'R']
popularity = [29, 19, 8, 7, 6, 5, 3]
explode = [0.1, 0, 0, 0, 0, 0, 0] # 0.1 pulls the first slice out slightly
plt.pie(popularity, labels=languages, explode=explode)
plt.title("Popularity of Programming Languages")
plt.show()