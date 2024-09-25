import random
names=['Alex','Caroline','Dave','Eleanor','Freddie']
students_score={student: random.randint(1,100) for student in names}
print(students_score)

#conditional dictionary Comprehension
#new ={key:value for {key,value} in dict.items() if test}

passed_students={student:score for (student,score) in students_score.items() if score>=35}
print(passed_students)