grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_sorted = sorted(students)
average_scores = {}
for i in range(len(students_sorted)):
    average_score = sum(grades[i]) / len(grades[i])
    average_scores[students_sorted[i]] = average_score
print(average_scores)
