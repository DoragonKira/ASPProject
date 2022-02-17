import pandas as pd
cars = pd.read_csv('mtcars.csv')
import matplotlib.pyplot as plt
plt.scatter(cars['mpg'], cars['hp'])
plt.show();




