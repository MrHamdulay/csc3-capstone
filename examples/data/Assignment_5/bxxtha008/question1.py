""" program to simulate a simple BBS
Thabiso Beau
15 April 2014"""
a=''
lys='42.txt'
lys_2='1015.txt'
message=("no message yet") 
while a!="X" and a!='x':
      print("Welcome to UCT BBS")
      print("MENU")
      print('(E)nter a message')
      print('(V)iew message')
      print('(L)ist files')
      print('(D)isplay file')
      print('e(X)it')
      a=input('Enter your selection: \n')
      if a=="E" or a=="e":
            message= input('Enter the message: \n')
      if a=="V" or a=="v":
            print('The message is:', message)
      if a=="l" or a=="L":
            print('List of files: ', lys,',',' ', lys_2, sep='')
      if a=="d" or a=="D":
            filename=input('Enter the filename: \n')
            if filename==lys_2:
                  print('Computer Science class notes ... simplified', 'Do all work', 'Pass course', 'Be happy', sep='\n')
            elif filename==lys:
                  print("The meaning of life is blah blah blah ...")
            elif filename!=lys or filename!=lys_2:
                  print('File not found')
            else:     
                  print(lys, ',', lys_2)
if a=="x" or a=="X":
      print("Goodbye!") 
                            