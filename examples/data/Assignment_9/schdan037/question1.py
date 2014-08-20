"""Daniel Schwartz
SCHDAN037
QUESTION 1
may 2014"""

import math


def standard_deviation(numbers):
    """Standard deviation calculator"""
    sd = 0
    N = len(numbers)
    mean = mean_average(numbers)
    inner = 0
    for x in numbers:
        inner += (x - mean) ** 2
    sd = math.sqrt(inner / N)
    return sd

def mean_average(numbers):
    """calculates the mean average of numbers"""
    mean = 0
    N = len(numbers)
    for n in numbers:
        mean += n
    mean /= N
    return mean


def main():
    """main"""
    filename = input("Enter the marks filename:\n")
    f = open(filename, "r")
    text = f.readlines()
    f.close()
    for i in range(len(text)):
        text[i] = text[i][:-1]          # strips the \n off
        text[i] = text[i].split(",")    # splits each line into a list of name and number
    numbers = []
    names = []
    for line in text:
        names.append(line[0])
        numbers.append(int(line[1]))
    sd = round(standard_deviation(numbers), 2)
    mean = round(mean_average(numbers), 2)
    print("The average is: {0:.2f}".format(round(mean, 2)))
    print("The std deviation is: {0:.2f}".format(round(sd, 2)))
    print("List of students who need to see an advisor:")
    for i in range(len(names)):
        if numbers[i] < (mean - sd):
            print(names[i])

#entry point runs main
if __name__ == '__main__':
    main()