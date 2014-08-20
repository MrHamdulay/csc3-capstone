def maker():
    print("Enter strings (end with DONE):")
    line=[]
    ip=input()
    a=len(ip)
    while ip!="DONE":
        line.append(ip)
        ip=input()
        if a<len(ip):
            a=len(ip)
    b=str(a)
    output="{pl:>a}"
    output=output.replace('a',b)
    print()
    print("Right-aligned list:")
    for line in line:
        print(output.format(pl=line))
    
maker()