import time
def main():
    e=' '
    o='_'
    s='/'
    l='|'
    x="\\"
    b=')'

    print(e,o*4,o*4,o*3,o*4,e+o*5,o,e,o,o,e,o,o+e)
    print(e+s,o*3+s,o*3+l+o,o+s,o*3+l+l,e+o*3+l,l,l,l,x,l,l,l)
    print(l,l,e*2+x+o*3,x+l,l+x+o*3,x+l,l+o,e+l,l,l,l,e+x+l,l,l)
    print(l,l+o*3,o*3+b,l,l,o*3+b,l+e*2+o+l,l,l+o+l,l,l+x+e*2+l+o+l)
    print(e+x+o*4+l+o*4+s+o*3+l+o*4+s+l+o+l,e*2,x+o*3+s+l+o+l,x+o+'('+o+b)

main()
time.sleep(5)