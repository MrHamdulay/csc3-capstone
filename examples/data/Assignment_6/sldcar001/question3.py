def vote():
    print("Independent Electoral Commission")
    print("--------------------------------")
    print("Enter the names of parties (terminated by DONE):")
    print()
    line=[]
    voters=[]
    ip=input()
    while ip!="DONE":
        line.append(ip)
        a=line.count(ip)
        if a==1:
            voters.append(ip)
            
        ip=input()
        if ip=="DONE":
            break
    voters.sort()
    print("Vote counts:")
    output="{0:10} - {1}"
    for voter in voters:
        print(output.format(voter,line.count(voter)))
               
vote()