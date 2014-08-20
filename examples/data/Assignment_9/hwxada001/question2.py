inp = input("Enter the input filename:\n")
outp = input("Enter the output filename:\n")
n = eval(input("Enter the line width:\n"))
fin = open(inp)
fout = open(outp, "w")
s = fin.read()
def rewrite(n, s):
    w = s.split()
    l = []
    ln = ''
    for i in w:
        if len(i) + len(ln)>n:
            l.append(ln)
            ln = ''
        ln = ln + i + ' '
        if i is w[-1]:
            l.append(ln)
    return '\n'.join(l)
p = s.split("\n\n")
for j in p:
    print (rewrite(n, j),"\n")
    fout.write(rewrite(n, j))
    fout.write("\n\n")
fout.close()
fin.close()