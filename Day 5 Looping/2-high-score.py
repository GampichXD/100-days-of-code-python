student_score = [78, 65, 89, 86, 55, 91, 64, 89]

total_exam_score = sum(student_score)
print(f"Total exam score: {total_exam_score}")

sum = 0
for score in student_score:
    sum += score

print(f"Total exam score: {sum}")

max_score = 0
for score in student_score:
    if score > max_score:
        max_score = score
    else:
        continue
print(f"Max score: {max_score}")