grades_min = {'1 ':75, '2+':70, '2-':60, '3 ':50}
marks = (int(a) for a in input("Enter a space-separated list of marks:\n").split(" "))
grades_chart = {'1 ':0, '2+':0, '2-':0, '3 ':0, 'F ':0}
for x in marks:
    for grade in sorted(grades_min):
        if x >= grades_min[grade]:
            grades_chart[grade] += 1
            break
    else:
        grades_chart['F '] += 1

for grade in sorted(grades_chart):
    print(grade + "|" + "X"*grades_chart[grade])