""" Analyse student marks read in from a file and determine which students need to see a student advisor.
The students who (hypothetically!) need to see a student adviser are those with marks less than one standard deviation
below the mean.
The marks file is composed of lines of text, where each line contains a student number and mark separated by a comma """
__author__ = 'Stephen Temple'
__date__ = '2014/05/12'


def main():
    # Open file
    file_name = input("Enter the marks filename:\n")
    with open(file_name, 'r') as file:
        file_lines = file.readlines()

    # Convert to 2D array
    marks = []
    sum_ = 0
    for line in file_lines:
        line = line.split(',')
        if line[1][:-1] == '\n':
            line[1] = line[1][:-1]
        marks.append([line[0], int(line[1])])
        sum_ += int(line[1])

    # Calculate and print mean
    mean = sum_ / len(marks)
    print("The average is: " + "{0:.2f}".format(mean))

    # Calculate and print standard deviation
    std_dev = (sum([(m[1] - mean)**2 for m in marks]) / len(marks))**(1/2)
    print("The std deviation is: " + "{0:.2f}".format(std_dev))

    # Print student names below mean - standard deviation
    students = []
    for m in marks:
        if m[1] < mean - std_dev:
            students.append(m[0])
    if len(students) > 0:
        print("List of students who need to see an advisor:")
        for student in students:
            print(student)



if __name__ == '__main__':
    main()