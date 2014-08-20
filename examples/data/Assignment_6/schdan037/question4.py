"""Daniel Schwartz
SCHDAN037
question 4
draws a histogram of marks
april 2014"""


def main():
    """main"""

    marks = []
    categories = {"1": 0, "2+": 0, "2-": 0, "3": 0, "F": 0}

    # receive input of marks
    marks = input("Enter a space-separated list of marks:\n").split(" ")

    # make marks into workable integers instead of strings
    for i in range(len(marks)):
        marks[i] = int(marks[i])

    # categorizing all the marks

    for mark in marks:
        if mark >= 75:
            categories["1"] += 1
        elif 70 <= mark < 75:
            categories["2+"] += 1
        elif 60 <= mark < 70:
            categories["2-"] += 1
        elif 50 <= mark < 60:
            categories["3"] += 1
        else:
            categories["F"] += 1

    # print the histogram of marks according to cat.
    sorted_catagories = sorted(categories.keys())

    for row in sorted_catagories:
        print_str = "{0:<2}|{1}"
        num_of_X = categories[row]
        X = "X" * num_of_X
        print_str = print_str.format(row, X)
        print(print_str)


#runs main on entry
if __name__ == '__main__':
    main()