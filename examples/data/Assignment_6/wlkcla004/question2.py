"""question 2
clare walker
19 april 2014"""

import math
#create empty array
vecs=[]
for i in range(2):
    vecs.append(['0'] *3)
#get vec A values   
vecs[0][0], vecs[0][1], vecs[0][2] = input("Enter vector A:\n").split(' ')
#get vec B values
vecs[1][0], vecs[1][1], vecs[1][2] = input("Enter vector B:\n").split(' ')

#addtion function
def addition(x):
    ans=[]
    for i in range(3):
        ans.append(eval(x[0][i])+eval(x[1][i]))
    return ans
                    
#dot production function
def dotP():
    ans=0
    for i in range(3):
        ans+=(eval(vecs[0][i])*eval(vecs[1][i]))
    return ans
#norm function
def norm(n):
    ans=0
    for i in range(3):
        ans+=(eval(vecs[n][i])**2)
    return math.sqrt(ans)

#core function to print desired output
def main():
    print("A+B =", addition(vecs))
    print("A.B =", dotP())
    print("|A| = {0:<.2f}".format(norm(0)))
    print("|B| = {0:<.2f}".format(norm(1)))
    
main()    
