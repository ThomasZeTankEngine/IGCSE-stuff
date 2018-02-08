student = int(input("What is the number of students?"))
name = []
score = []

for i in range(student):
    name.append(str((input("Gimme a name"))))
    score.append(int(input("Gimme their score")))

for i in range(len(score)):
    max = score[0]
    if score[i]>max:
        max = score[i]

position = score.index(max)
print(name[max])










    








































