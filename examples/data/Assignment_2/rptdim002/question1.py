#leap year program
#RPTDIM002
def main():
    year=eval(input("Enter a year:\n"))
    if year/(4)==year//(4):
        print(year,"is a leap year.")
    else:
        print(year,"is not a leap year.")
main()        
              