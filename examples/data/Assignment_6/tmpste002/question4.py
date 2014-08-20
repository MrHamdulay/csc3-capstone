""" Takes in a list of marks (separated by spaces)
and outputs a histogram representation of the marks
according to the mark categories at UCT """
__author__ = 'Stephen Temple'
__date__ = '2014/04/23'


def main():
    marks = input('Enter a space-separated list of marks:\n').split(' ')
    mark_count = {'1': 0, '2+': 0, '2-': 0, '3': 0, 'F': 0}
    for mark in marks:
        mark = int(mark)
        if mark >= 75:
            mark_count['1'] += 1
        elif mark >= 70:
            mark_count['2+'] += 1
        elif mark >= 60:
            mark_count['2-'] += 1
        elif mark >= 50:
            mark_count['3'] += 1
        else:
            mark_count['F'] += 1
    output = '{0: <2}|{1}'
    for grade in sorted(mark_count.keys()):
        print(output.format(grade, 'X'*mark_count[grade]))


if __name__ == '__main__':
    main()