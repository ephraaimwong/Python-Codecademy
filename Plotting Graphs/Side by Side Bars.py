import codecademylib
from matplotlib import pyplot as plt

unit_topics = ['Limits', 'Derivatives', 'Integrals', 'Diff Eq', 'Applications']
middle_school_a = [80, 85, 84, 83, 86]
middle_school_b = [73, 78, 77, 82, 86]

def create_x(t, w, n, d): #to be determine position on x-axis to place the bar so bars can stack side-by-side
    # t = total datasets
    # w = width of bar
    # n = nth number of total 
    # d = number of datapoints
    return [t*x + w*n for x in range(d)]

# Make your chart here
plt.figure(figsize = (10, 8))
school_a_x = create_x(2, 0.8, 1, 5)
plt.bar(school_a_x, middle_school_a)
school_b_x = create_x(2, 0.8, 2, 5)
plt.bar(school_b_x, middle_school_b)

ax = plt.subplot()
#middle_x will find the middle position of each set of side-by-side bars so that labels can be centered 
middle_x = [(i + ix) / 2 for i, ix in zip(school_a_x, school_b_x)]
ax.set_xticks(middle_x)
ax.set_xticklabels(unit_topics)

legend = ["Middle School A", "Middle School B"]
plt.axis([0, 11, 70, 90])
plt.legend(legend)
plt.xlabel("Unit")
plt.ylabel("Test Average")
plt.title("Test Averages on Different Units")

plt.show()
plt.savefig("my_side_by_side.png")