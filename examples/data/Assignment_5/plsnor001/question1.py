#-------------------------------------------------------------------------------
# Name:     question 1
# Purpose: a program to simulate a simple BBS with one stored message and 2 fixed files
# Author:      Pilusa
# Created:     14-04-2014
# Copyright:   (c) Pilusa 2014
#-------------------------------------------------------------------------------

def main():

    names='42.txt, 1015.txt'
    msg=''

    while True:# give list of options to user
        print('Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it')
        selection=input('Enter your selection:\n').upper()

        if selection=='X':
            print('Goodbye!')
            break #terminate program

        if selection=='E':
            message=input('Enter the message:\n')#store message
            msg=message
            continue

        if selection=='V':
            if msg!='':
                print('The message is:',msg) #view stored message
                continue
            else: print('The message is:','no message yet')


        if selection=='L':
            print('List of files:',names) #view list of files
            continue

        if selection=='D':
            filename=input('Enter the filename:\n')
            if filename=='42.txt':
                print('The meaning of life is blah blah blah ...') #display a certain file if in storage

            elif filename=='1015.txt':
                print('Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy')

            elif filename not in names:
                print('File not found')
            continue





if __name__ == '__main__':
    main()
