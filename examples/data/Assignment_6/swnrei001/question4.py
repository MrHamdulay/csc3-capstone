"""Question 4 of assignment 6
Histogram of inputted list of marks
SWNREI001
20/04/2014"""

def markcounter(marks):
    """Counts the number of 1, 2+, 2-, 3 and F in a list of marks;
    Returns a counted list in order: 1, 2+, 2-, 3, F"""
    ans = {"1": 0, "2+": 0, "2-": 0, "3": 0, "F": 0}
    for i in marks:
        if i >= 75:
            ans["1"] += 1
        elif i >= 70:
            ans["2+"] += 1
        elif i >= 60:
            ans["2-"] += 1
        elif i >= 50:
            ans["3"] += 1
        else:
            ans["F"] += 1
    return ans

def marksgram(markscount):
    """Takes a dictionary of numbers of marks in each category; prints histogram of this"""
    for i in sorted(markscount.keys()):
        print(i.center(2), end = "|")
        print("X" * markscount[i])

def main():
    """Main function of module
    Gets a space-separated list of marks
    Outputs as a histogram"""
    print("Enter a space-separated list of marks:")
    marks = eval("[" + input().replace(" ", ",") + "]")
    # the above transforms 'a b c ... n' into '[a, b, c, ..., n]'
    # eval transforms this into a list
    marksgram(markcounter(marks))

if __name__ == "__main__":
    main()