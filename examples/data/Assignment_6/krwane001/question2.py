import math

v = input("Enter vector A:\n")
split = v.split()
split = list(map(int,split))

v_1 = input("Enter vector B:\n")
split1 = v_1.split()
split1 = list(map(int,split1))

a = split[0]+split1[0]
b = split[1]+split1[1]
c = split[2]+split1[2]

a1 = split1[0]*split1[0]
b1 = split1[1]*split1[1]
c1 = split1[2]*split1[2]

a_1 = split[0]*split1[0]
b_1 = split[1]*split1[1]
c_1 = split[2]*split1[2]

a2 = split[0]*split[0]
b2 = split[1]*split[1]
c2 = split[2]*split[2]

new = a,b,c
new1 = a1+b1+c1
new2 = math.sqrt(a2+b2+c2)
new3 = math.sqrt(a1+b1+c1)
new4 = a_1+b_1+c_1

print("A+B =",list(new))
print("A.B =",new4)
if new2 == 0:
    print("|A| = 0.00")
else:
    print("|A| =",round(new2,2))
if new3 == 0:
    print("|B| = 0.00")
else:
    print("|B| =",round(new3,2))
          