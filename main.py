import matplotlib.pyplot as plt
import pandas as pd

plt.style.use('bmh')
df = pd.read_csv('movie_info.csv')

x = df['Title']
y = df['Ratings']

plt.pie(y, labels=x)

plt.show()