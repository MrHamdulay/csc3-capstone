#A program to determine whether a year is a leap year or not.
#ATISANG MOLAPO
#STUDENT NUMER:MLPATI001
def main():
        yr = eval(input('Enter a year:\n'))
         
        if yr%400==0:
                print(yr, "is a leap year.")
        elif yr%100==0:
                print(yr, "is not a leap year.")
        elif yr%4==0:
                print(yr, "is a leap year.")
         
        else:
                print(yr, "is not a leap year.")
             
    
         

main()