#------------------------------------------------------------------------------#
# A program that calculate the number of votes for each political party given  #
# by the user.                                                                 #
# Name: Thubelihle Mdlalose                                                    #
# Student Number: MDLTHU011                                                    #
#------------------------------------------------------------------------------#

def main():
    # Display the headings.
    print("Independent Electoral Commission")
    print("--------------------------------")
    print("Enter names of parties (terminated by DONE):")
    
    names = []
    x = ""
    while x != "DONE":
        x = input()
        if x != "DONE":
            names.append(x)
            
    names.sort()
    print(names[0], names.count(names[0]))
# Call the main function
main()
    
    
        