"""A6Q3 - Vote Count
CRNKEE002
21/4/2013"""

parties = {}

def main():
    print("Independent Electoral Commission")
    print("--------------------------------")
    get_list()
    print("") #because automatic marker, that's why
    print_list(parties)
    
def get_list():
    global parties
    print("Enter the names of parties (terminated by DONE):")
    name = ""
    name = input()
    while name.upper() != "DONE":        
        if name in parties:
            parties[name] = parties[name] + 1
        else:
            parties[name] = 1
        name = input()
        
        
def print_list(dictionary): 
    print("Vote counts:")
    for i in sorted(parties):
        print("{0: <10}".format(i), '-', parties[i])
    
if __name__ == "__main__":
    main()