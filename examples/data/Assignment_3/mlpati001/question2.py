
def main():
    A=eval(input("Enter the height of the triangle:\n"))
    B=A
    for i in range(0,A):
        B-=1
        print(" "*B+(1+2*i)*"*")

main()