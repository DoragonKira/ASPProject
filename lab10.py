import pandas as pd
import matplotlib.pyplot as plt

# reading the file
excel_file = 'Project_File.xlsx'
df = pd.read_excel(excel_file)


# retrieving the data and finding the sum
total = df.iloc[:, 1:6].sum()


# sorting the values in ascending order
sorttop3 = total.sort_values()


# selecting the top 3 values
top3 = sorttop3.tail(3)
print(top3)

# plotting the graph
plt.xlabel('Countries', fontsize=5)
plt.ylabel('Total visitors in 10 years', fontsize=10)
plt.title('Top 3 countries with the most visitors')
plt.ticklabel_format(style='plain')
plt.bar(top3.index, top3.values)
plt.show()




