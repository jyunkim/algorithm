pic_num = int(input())
total_rec = int(input())
recommendations = list(map(int, input().split()))
student_rec = [0] * 101
pictures = []

def find_min_rec():
    min_rec_student = pictures[0]
    min_rec = student_rec[min_rec_student]
    for student in pictures:
        if student_rec[student] < min_rec:
            min_rec_student = student
            min_rec = student_rec[student]
    return min_rec_student
            
for student in recommendations:
    if student in pictures:
        student_rec[student] += 1
    else:
        if len(pictures) < pic_num:
            pictures.append(student)
            student_rec[student] += 1
        else:
            temp = find_min_rec()
            pictures.remove(temp)
            student_rec[temp] = 0
            pictures.append(student)
            student_rec[student] += 1
    
pictures.sort()

for student in pictures:
    print(student, end=" ")
