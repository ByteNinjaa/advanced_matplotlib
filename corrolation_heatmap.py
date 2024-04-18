import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('student_scores1.csv')

correlation_matrix = df.corr()

sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')

plt.title('Correlation Heatmap')
plt.xticks(rotation=45)
plt.yticks(rotation=0)

plt.savefig('correlation_heatmap.png')
