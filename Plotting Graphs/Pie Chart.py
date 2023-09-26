import codecademylib
from matplotlib import pyplot as plt

unit_topics = ['Limits', 'Derivatives', 'Integrals', 'Diff Eq', 'Applications']
num_hardest_reported = [1, 3, 10, 15, 1]

#Make your plot here
plt.figure(figsize = (10, 8))
plt.pie(num_hardest_reported, labels = unit_topics, autopct = "%d%%") #autopct will auto assign values to the pie chart
plt.axis("equal") #adjusts the pie chart to be 2D instead of 3D
plt.title("Hardest Topics")
plt.savefig("my_pie_chart.png")
plt.show()
