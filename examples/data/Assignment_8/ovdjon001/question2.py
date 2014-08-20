""" Assingment 8, question2.py
by Jonathan Ovadia 
on 4th May 2014"""
def main():
    string = input ("Enter a message:\n")
    number_of_repeated_pairs(string)
def number_of_repeated_pairs(string,number = 0):
    if len(string) ==1 or len(string) == 0:
        print("Number of pairs:",number)
    elif string[0] == string[1]:
        number_of_repeated_pairs(string[2::],number+1)
    else:
        number_of_repeated_pairs(string[1::],number)


if __name__ == "__main__": main()