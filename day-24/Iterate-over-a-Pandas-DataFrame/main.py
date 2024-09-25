import pandas as pd
student_dict={
    "student":["Pavan","Babu","saan","kumar"],
    "score":[56,76,98,55]
}

student_data_frame= pd.DataFrame(student_dict)
print(student_data_frame)


#loop through rows of a data frame
for (index,row) in student_data_frame.iterrows():
    if row.student=='Pavan':
        print(row.score)