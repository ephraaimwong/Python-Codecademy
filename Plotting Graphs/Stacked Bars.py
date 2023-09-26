import codecademylib
from matplotlib import pyplot as plt
import numpy as np

unit_topics = ['Limits', 'Derivatives', 'Integrals', 'Diff Eq', 'Applications']
As = [6, 3, 4, 3, 5]
Bs = [8, 12, 8, 9, 10]
Cs = [13, 12, 15, 13, 14]
Ds = [2, 3, 3, 2, 1]
Fs = [1, 0, 0, 3, 0]

x = range(5)

c_bottom = np.add(As, Bs) #Cs will start where Bs end, currently holds As and Bs
d_bottom = np.add(c_bottom, Cs) #Ds will start where Cs,end, currently holds As, Bs, Cs
f_bottom = np.add(d_bottom, Ds) #Fs will start where Ds end, currently holds As, Bs, Cs, Ds

plt.figure(figsize = (10, 8))
plt.bar(range(len(unit_topics)), As)
plt.bar(range(len(unit_topics)), Bs, bottom = As)
plt.bar(range(len(unit_topics)), Cs, bottom = c_bottom)
plt.bar(range(len(unit_topics)), Ds, bottom = d_bottom)
plt.bar(range(len(unit_topics)), Fs, bottom = f_bottom)

ax = plt.subplot()
ax.set_xticks(range(len(unit_topics)))
ax.set_xticklabels(unit_topics)

plt.title("Grade Distribution")
plt.xlabel("Unit")
plt.ylabel("Number of Students")
plt.legend(["A's", "B's", "C's", "D's", "F's"])

plt.savefig("my_stacked_bar.png")
plt.show()