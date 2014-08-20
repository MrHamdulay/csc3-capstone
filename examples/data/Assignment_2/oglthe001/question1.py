s=eval(input("Enter a year:""\n"))
if s/400==s//400 or s/4==s//4 and not s/100==s//100:
    print(s,"is a leap year.")
else:
    print(s,"is not a leap year.")