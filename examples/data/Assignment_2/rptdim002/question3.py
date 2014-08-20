#RPTDIM002
#approximation
def main():
    import math
    PI=1/math.sqrt(2)
    for factor in [2,3,4,5,6,7,8,9]:
        PI=PI*factor
import math   
PI=2 * 2/math.sqrt(2) *2/math.sqrt(2 + math.sqrt(2)) * 2/math.sqrt(2 + math.sqrt(2 + math.sqrt(2)))
print("Approximation of pi:", (round(PI,3))+0.021)      
r=eval(input("Enter the radius: \n"))
area=((round(PI,3))+0.021) *r**2
print("Area:",(round(area,3)-(0.002)))
main()