d={'Ansh':60, 'Yash':65, 'Aryan':70, 'Puneet':75, 'Abhinav':80}
print("\nList of students's name and their scores")

for student,score in d.items():
    print(f"{student} = {score}")

print("\nStudent with the highest score: ")
highest_score = 0
highest_score_student = " "
        
for student, score in d.items():
    if score > highest_score:
        highest_score = score
        highest_score_student = student

print(f"{highest_score_student} = {highest_score}")

print("\nUpdating the score for Aryan : ")
d['Aryan']= 83
for student,score in d.items():
    print(f"{student} = {score}")