def main():



    print("Independent Electoral Commission")
    print("--------------------------------")
    party = input("Enter the names of parties (terminated by DONE):\n")
    parties = dict()
    while party != "DONE":
        if party in parties.keys():
            parties[party] += 1
        else:
            parties[party] = 1
        party = input()
    print()
    print("Vote counts:")
    for i in sorted(parties.keys()):
        print("{:10}".format(i),"-",parties[i])
main()

