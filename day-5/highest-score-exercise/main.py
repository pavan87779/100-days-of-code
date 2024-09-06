student_scores=[150,120,160,190,135,242,235,540,454,554,335,369]
print(sum(student_scores))
sum=0
for score in student_scores:
    sum+=score
print(sum)

print(max(student_scores))
max=0
for score in student_scores:
    if score>max:
        max=score

print(max)