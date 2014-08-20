"""Sithembiso Mashinini 
2014/04/25
Shows the results of a list of votes """


def main():
    print('Independent Electoral Commission')
    print('--------------------------------')
    
    user_input=input('Enter the names of parties (terminated by DONE):\n')
    list_parties=[]
    while user_input!='DONE':#sentinal
        list_parties.append(user_input)
        user_input=input()
    x=sorted(list_parties)#this was not necessary
    d={}
    print ()
    print('Vote counts:')
    for i in x:
        d[i]=x.count(i)#adding to my dictionary 
        sorted(d)
        
    z=(sorted(d.keys()))# this sorts the keys of the dictionar so everything is in order  
    for i in z:
        
        print(i,' '*(10-len(i))+'-',d[i])
main()


            