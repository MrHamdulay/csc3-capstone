import ndom
def main():
    y=input("Choose a test:\n")
    if y=='d':
        ndom.ndom_to_decimal(f)
    elif y=='n':
        ndom.decimal_to_ndom(f)
    elif y=='a':
        ndom.nom_add(f,b)
    elif y=='m':
        ndom.nom_multiply(f,b)
    else:
        print()
main()