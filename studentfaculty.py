import csv
f1=open(r"/mnt/c/Users/ammas/Downloads/students.csv")
faculty_file=open(r"/mnt/c/Users/ammas/Downloads/data.csv")
student_file=open(r"/mnt/c/Users/ammas/Downloads/students.csv")
faculty_data=csv.reader(faculty_file)
data2=csv.reader(f1)
list=[]
for data in data2:
    list.append(data)
f1.close()
# print(list)

for i in list:
    if i[1].lower()=="mathematics":
        print(i)

student_phsics_data=[]
for i in list:
    if i[1].lower()=="physics":
        student_phsics_data.append([i[0],i[2]])
print(student_phsics_data)

new_faculty_list=[]
for info2 in faculty_data:
    new_faculty_list.append(info2)

student_data=csv.reader(student_file)
top_faculty=[]
maths=0
physics=0
chemistry=0
social=0
english=0
telugu=0
for i in list:
    if i[2]>"90":
        sub=i[1]
        if sub.lower() == "Mathematics":
            maths+=1
        elif sub.lower()== "Telugu":
            telugu+=1
        elif sub.lower()=="Physics":
            physics+=1
        elif sub.lower()=="social":
            social+=1
        elif sub.lower()=="chemistry":
            chemistry+=1
        elif sub.lower()=="english":
            english+=1

max_count_data={"maths":maths,"physics":physics,"chemistry":chemistry,"telugu":telugu,"english":english,"social":social}
# max_count=max([maths,physics,chemistry,telugu,english,social])
# max_count=max(max_count_data.values())
max_subject=max(max_count_data,key=max_count_data.get)
# print(max_subject)
# print(new_faculty_list)
for top_faculty in new_faculty_list:
    if top_faculty[0].lower()==max_subject:
        print(top_faculty[1])


students=[]
for s in list:
    if s[0] not in students:
        students.append(s[0])
# print(students)

students_marks_list=[]
for sl in students:
    total_marks_sum=0
    for s in list:
        if s[0]==sl:
            total_marks_sum+=int(s[2])
    students_marks_list.append([sl,total_marks_sum])

# print(students_marks_list)
topper=max(students_marks_list,key=lambda x:x[1])
print(topper)

min_student=min(students_marks_list,key=lambda x:x[1])
print(min_student)

maths_marks=0
telugu_marks=0
physics_marks=0
social_marks=0
chemistry_marks=0
english_marks=0
for i in list:
        sub=i[1]
        if sub.lower() == "mathematics":
            maths_marks+=int(i[2])
            maths+=1
        elif sub.lower()== "telugu":
            telugu_marks+=int(i[2])
            telugu+=1
        elif sub.lower()=="physics":
            physics_marks+=int(i[2])
            physics+=1
        elif sub.lower()=="social":
            social_marks+=int(i[2])
            social+=1
        elif sub.lower()=="chemistry":
            chemistry_marks+=int(i[2])
            chemistry+=1
        elif sub.lower()=="english":
            english_marks+=int(i[2])
            english+=1
maths_avg=maths_marks//maths
telugu_avg=telugu_marks//telugu
chemistry_avg=chemistry_marks//chemistry
social_avg=social_marks//social
english_avg=english_marks//english
physics_avg=physics_marks//physics

sub_avg_marks=[maths_avg,telugu_avg,chemistry_avg,english_avg,social_avg,physics_avg]
fac_highest_pass_percetage=[]
fac_highest_pass_percetage2=[]
for m in sub_avg_marks:
    if m>40:
        fac_highest_pass_percetage.append(m)
    elif m<=40:
        fac_highest_pass_percetage2.append(m)
print(fac_highest_pass_percetage)

result=[[data[0], int(data[2])] for data in list if data[1].lower()=="mathematics"]
print(max(result, key=lambda x: x[1]))
