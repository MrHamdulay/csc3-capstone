#personalised spam message
#Dacod Magagula

def main():
   
    f=input('Enter first name:\n')
    l=input('Enter last name:\n')
    s=eval(input('Enter sum of money in USD:\n'))
    c=input('Enter country name:\n')
    tp=0.3*s
    print('')

    print("Dearest",f)
    print('It is with a heavy heart that I inform you of the death of my father,')
    print("General Fayk ",l,", your long lost relative from Mapsfostol.",sep='')
    print("My father left the sum of ",s,"USD for us, your distant cousins.",sep="")
    print('Unfortunately, we cannot access the money as it is in a bank in ',c,'.',sep="")
    print('I desperately need your assistance to access this money.')
    print("I will even pay you generously, 30% of the amount - ",tp,"USD,",sep="")
    print('for your help.  Please get in touch with me at this email address asap.')
    print('Yours sincerely')
    print('Frank',l)  
main()