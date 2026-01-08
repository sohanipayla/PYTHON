import matplotlib.pyplot as plt
movies = ['Comedy', 'Action', 'Romance', 'Drama', 'SciFi']
votes = [4, 5, 6, 1, 4]
colors = ['gold', 'red', 'pink', 'gray', 'cyan']
wedge_effect = [0, 0.2, 0, 0, 0]  # 0.2 pulls the 2nd slice (Action) out
plt.pie(votes, labels=movies, colors=colors, explode=wedge_effect)
plt.title("Survey analysis of movie")
plt.show()