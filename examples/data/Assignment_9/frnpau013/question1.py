"""analyses student marks read in from a file and determines 
which students need to see a student advisor.
Paul Freund
11 May 2014"""

def dict_maker(s):
    """returns a dictionary of names and marks from a file named 's'"""
    file = open(s, 'r')
    _dict = {}
    for line in file:
        name, mark = line.split(",")
        _dict[name] = int(mark)
    file.close()
    return _dict

def name_lister(s):
    file = open(s, 'r')
    names = []
    for line in file:
        name, mark = line.split(",")
        names.append(name)
    file.close()
    return names

def average(mark_list):
    """returns average of a list of numbers"""
    mark_sum = 0
    for mark in mark_list:
        mark_sum += mark
    average = mark_sum/len(mark_list)
    return average

def std_dev(mark_list, average):
    """returns the std deviation of a list of numbers, given the average"""
    import math
    mark_sum = 0
    for mark in mark_list:
        mark_sum += (mark - average)**2
    variance = mark_sum/len(mark_list)
    std_dev = math.sqrt(variance)
    return std_dev

def advisor_checker(marks_dict, mean, std_dev):
    """returns a list of names whose marks fall below (mean - std_dev)"""
    advisor_threshold = mean - std_dev
    need_advice = []
    for i in marks_dict:
        if marks_dict[i] < advisor_threshold:
            need_advice.append(i)
    return need_advice
            

def main():
    """formats input and output"""
    file = input('Enter the marks filename:\n')
    # turning file data into a dictionary and a list of keys and list of values
    marks_dict = dict_maker(file)
    marks_list = marks_dict.values()
    names = name_lister(file)
    # creating output variables
    the_average = average(marks_list)
    the_std_dev = std_dev(marks_list, the_average)
    need_advice = advisor_checker(marks_dict, the_average, the_std_dev)
    # formatting output
    print("The average is: {0:.2f}".format(the_average))
    print("The std deviation is: {0:.2f}".format(the_std_dev))
    if need_advice != []:
        print("List of students who need to see an advisor:")
        for i in names:
            if i in need_advice:
                print(i)
    
if __name__ == '__main__':
    main()