def q1():
    print("Enter strings (end with DONE):")
    a = []
    j=0
    longname=''
    sub = 0
    while j != 'DONE':
        j = input('')
        if j != 'DONE':    
            a.append(j)
        
    for i in a:
        if len(i) > len(longname):
            longname = i
    
    x = str(len(longname))
    print("\nRight-aligned list:")
    for i in a:
        g = "{0: >"+x+"}"
        print(g.format(i))
q1()