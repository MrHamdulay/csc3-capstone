#KRTDAK001

def vector():
    alist = []
    blist = []
    clist = []
    d = 0
    e = 0
    f = 0
    a = input("Enter vector A:\n")
    b = input("Enter vector B:\n")
    alist = a.split(" ")
    blist = b.split(" ")
    i = 0
    while i < len(alist):
        alist[i] = eval(alist[i])
        blist[i] = eval(blist[i])
        clist.append(alist[i] + blist[i])
        d = d + alist[i]*blist[i]
        e = e + alist[i]**2
        f = f + blist[i]**2
        i += 1
    e = (e)**0.5
    f = (f)**0.5
    print("A+B =", clist)
    print("A.B =", d)
    print("|A| =", round(e, 2))
    print("|B| =", round(f, 2))
vector()