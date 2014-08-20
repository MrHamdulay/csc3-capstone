#to calculate if a given year is a leap year

def main():
    
    ans=eval(input("Enter a year:\n"))

    if (ans/400.0==ans//400):
        print(ans, "is a leap year.")
        
    elif (ans/4.0==ans//4 and not ans/100.0==ans//100):
            print(ans, "is a leap year.")
        
    else:
        print(ans, "is not a leap year.")
        
main()