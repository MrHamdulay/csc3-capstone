'''NWTDOU001
question2.py
25 april 2014'''

import math

# gets input in form "x y z ..." and converts it to array of number values
def input_vector(str):
    vec = input(str)
    vec = vec.split(' ')
    for i in range(3):
        vec[i] = eval(vec[i])
    return vec

# returns sum of each element of 2 vectors multiplied together
def dot_mult_vectors(vec1,vec2):
    total = 0
    for i in range(3):
        total += vec1[i] * vec2[i]
    return round(total,2)
        

# adds each element of vec1 and vec2 together and return results in a new vector
def add_vectors(vec1,vec2):
    vec = []
    for i in range(3):
        vec.append(vec1[i]+vec2[i])
    return vec

# calculates the normal of a vector, assuming it is 3d
def normal(vec):
    return round(
        math.sqrt(vec[0]**2 + vec[1]**2 + vec[2]**2), 2
    )


vec_a = input_vector('Enter vector A:\n')
vec_b = input_vector('Enter vector B:\n')

print('A+B =',add_vectors(vec_a,vec_b))
print('A.B =',dot_mult_vectors(vec_a,vec_b))
print('|A| =','%.2f' % normal(vec_a))
print('|B| =','%.2f' % normal(vec_b))