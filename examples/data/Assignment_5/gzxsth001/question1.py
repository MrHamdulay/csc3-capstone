""" To Write a program to simulate a simple BBS with one stored message and 2 fixed files
Sthabiso Andile Gazu
gzxsth001"""

hey="""Welcome to UCT BBS
MENU
(E)nter a message
(V)iew message
(L)ist files
(D)isplay file
e(X)it"""
y='no message yet'
while True:
      print(hey)
      x=input('Enter your selection:\n').lower()
      if x=='v' or x=="V":
            print('The message is:' ,y)
      elif x=='E' or x=='e':
            y=input('Enter the message:\n')   
      elif x=='l' or x=='L':
            print('List of files: 42.txt, 1015.txt ')
      
      elif x=='d' or x=='D':
            x=input('Enter the filename:\n')      
            if x=='42.txt':
                  print('The meaning of life is blah blah blah ...')
                        
                     
            elif x=='1015.txt':
                  print('Computer Science class notes ... simplified')
                  print('Do all work')
                  print('Pass course')
                  print('Be happy')
            else:
                  print('File not found')
                                              
            
      
      elif x=='x':
            print('Goodbye!')
            break
     