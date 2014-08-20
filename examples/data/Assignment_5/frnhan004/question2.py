"""Question 3 - Assignment 5
FRNHAN004
16 April 2014"""

m_d = {1: 0, 0.25: 0, 0.10: 0, 0.05: 0, 0.01: 0}
#possible ammounts used
m_l = [1, 0.25, 0.10, 0.05, 0.01]


#user input
cost = eval(input("Enter the cost (in cents):\n"))
if cost>0:
    paid = eval(input("Deposit a coin or note (in cents):\n"))
    npaid=[paid]
    #loop until the ammount paid is greater or equal to the cost
    while sum(npaid)<cost:
        a = eval(input("Deposit a coin or note (in cents):\n"))
        npaid.append(a)
        #once the ammount paid is equal to the cost c
    else:
        change = sum(npaid) - cost
        cent=change/100
        if change != 0:   
            print("Your change is:")
        for i in m_l:
            while cent >= i:
                m_d[i] += 1
                cent -= i -0.00000001 #when subtracted 8 from 8.85 the decimals didnt round up to .85
        if m_d[1]!=0:
            print(m_d[1],"x $1")
        if m_d[0.25]!=0:
            print(m_d[0.25],"x 25c")
        if m_d[0.10]!=0:
            print(m_d[0.10],"x 10c")
        if m_d[0.05]!=0:
            print(m_d[0.05],"x 5c")
        if m_d[0.01]!=0:
            print(m_d[0.01],"x 1c")
else:
    pass