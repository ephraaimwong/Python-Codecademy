last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Your code below: 
subjects = ["physics", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]
gradebook = []
#zips subjects and grades into a 2D list
for i, ix in zip(subjects, grades):
    gradebook.append([i, ix])

gradebook.append(["computer science", 100])
gradebook.append(["visual arts", 93])
print(gradebook)
#adding 5 marks to visual arts
gradebook[-1][-1] += 5 
#changing poetry grades from 85 to "pass"
gradebook[2][1] = "Pass"


full_gradebook = last_semester_gradebook + gradebook

print(full_gradebook)

