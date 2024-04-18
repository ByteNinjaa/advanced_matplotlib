import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("student_scores1.csv")
median_scores = data.groupby('Subject')['Score'].median().reset_index()

fig, ax = plt.subplots()

bar_width = 0.35
x = range(len(median_scores))

ax.bar(x, median_scores['Score'], width=bar_width, label='Median Score')

ax.set_xticks(x)
ax.set_xticklabels(median_scores['Subject'])

ax.set_xlabel('Subject')
ax.set_ylabel('Median Score')
ax.set_title('Median Scores of Students in Different Subjects')

ax.legend()

plt.savefig('clustered_bar_chart.png')
