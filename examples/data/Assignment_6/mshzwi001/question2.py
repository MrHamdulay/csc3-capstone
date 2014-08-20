#a programe to do basic vector calculations in 3 dimensions: addition, dot product and normalization.
# mashau zwivhuya
# 21 april 2014
import math

def main():
    #getting inputs and conveting to lists
    list1=input("Enter vector A:\n")
    list1=list1.split(" ")
    list1=[eval(list1[0]),eval(list1[1]),eval(list1[2])]
    list2=input("Enter vector B:\n")
    list2=list2.split(" ")
    list2=[eval(list2[0]),eval(list2[1]),eval(list2[2])]
    #vector addition
    vector_addition_0=list1[0]+list2[0]
    vector_addition_1=list1[1]+list2[1]
    vector_addition_2=list1[2]+list2[2]
    add=[vector_addition_0,vector_addition_1,vector_addition_2]
    print("A+B =",add)
    #the dot product
    vector_mult_0=list1[0]*list2[0]
    vector_mult_1=list1[1]*list2[1]
    vector_mult_2=list1[2]*list2[2]
    ans=(vector_mult_0+vector_mult_1+vector_mult_2)
    print("A.B =",ans)
    #hypotenuse_A
    hyp=math.sqrt((list1[0])**2+(list1[1])**2+(list1[2])**2)
    print("|A| =","%1.2f " % hyp)
    #hypotenuse_B
    hypo=math.sqrt((list2[0])**2+(list2[1])**2+(list2[2])**2)
    print("|B| =","%1.2f " % hypo)
    
main()    