import math

pi = 2*(2/math.sqrt(2))*(2/math.sqrt(2 + math.sqrt(2)))*(2/math.sqrt(2 +math.sqrt(2 + math.sqrt(2))))*(2/math.sqrt(2 +math.sqrt(2 + math.sqrt(2+ math.sqrt(2)))))*(2/math.sqrt(2 +math.sqrt(2 + math.sqrt(2+ math.sqrt(2 + math.sqrt(2))))))*(2/math.sqrt(2 +math.sqrt(2 + math.sqrt(2+ math.sqrt(2 + math.sqrt(2 + math.sqrt(2)))))))*(2/math.sqrt(2 +math.sqrt(2 + math.sqrt(2+ math.sqrt(2 + math.sqrt(2 + math.sqrt(2 + math.sqrt(2))))))))*(2/math.sqrt(2 +math.sqrt(2 + math.sqrt(2+ math.sqrt(2 + math.sqrt(2 + math.sqrt(2 + math.sqrt(2+ math.sqrt(2)))))))))


#print(pi) test
pi2 =round(2*(2/math.sqrt(2))*(2/math.sqrt(2 + math.sqrt(2)))*(2/math.sqrt(2 +math.sqrt(2 + math.sqrt(2))))*(2/math.sqrt(2 +math.sqrt(2 + math.sqrt(2+ math.sqrt(2)))))*(2/math.sqrt(2 +math.sqrt(2 + math.sqrt(2+ math.sqrt(2 + math.sqrt(2))))))*(2/math.sqrt(2 +math.sqrt(2 + math.sqrt(2+ math.sqrt(2 + math.sqrt(2 + math.sqrt(2)))))))*(2/math.sqrt(2 +math.sqrt(2 + math.sqrt(2+ math.sqrt(2 + math.sqrt(2 + math.sqrt(2 + math.sqrt(2)))))))),3)#pi rounded off

print("Approximation of pi:",pi2)
rad = eval(input("Enter the radius:\n"))
area = round(pi*rad**2,3)
print("Area:", area)