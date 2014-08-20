#danson masuka
#program to calcualte vectors
#23 april 14

import math
vecA = input ("Enter vector A:\n")
vecB = input ("Enter vector B:\n")

def addition():
    addA = []
    addA = (vecA.split())
    addB = []
    addB = (vecB.split())
    addoutput = [(eval(addA[0]))+(eval(addB[0])),(eval(addA[1]))+(eval(addB[1])),(eval(addA[2]))+(eval(addB[2]))]
    print ("A+B =",addoutput)
def dotproduct():
    dotA = []
    dotA = (vecA.split())
    dotB = []
    dotB = (vecB.split())
    dotoutput = (eval(dotA[0]))*(eval(dotB[0]))+(eval(dotA[1]))*(eval(dotB[1]))+(eval(dotA[2]))*(eval(dotB[2]))
    print ("A.B =",dotoutput)
    
def norm():
    normA = []
    normA = (vecA.split())
    normB = []
    normB = (vecB.split())
    normAoutput = math.sqrt((eval(normA[0]))**2+(eval(normA[1]))**2+(eval(normA[2]))**2)
    normBoutput = math.sqrt((eval(normB[0]))**2+(eval(normB[1]))**2+(eval(normB[2]))**2)
    print ("|A| = {0:.2f}".format(normAoutput))
    print ("|B| = {0:.2f}".format(normBoutput))
addition()
dotproduct()
norm()