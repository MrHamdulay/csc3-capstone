""" Count the number of votes for each political party in an election """
__author__ = 'Stephen Temple'
__date__ = '2014/04/23'


def main():
    # Print welcome message
    print('Independent Electoral Commission')
    print('--------------------------------')

    # Imput party names
    party = input('Enter the names of parties (terminated by DONE):\n')
    party_array = {}
    while party != 'DONE':
        if party in party_array.keys():
            party_array[party] += 1
        else:
            party_array[party] = 1
        party = input('')

    # Output formatted vote count
    print('\nVote counts:')
    output = '{0: <10} - {1}'
    for p in sorted(party_array.keys()):
        print(output.format(p, party_array[p]))


if __name__ == '__main__':
    main()