#Ndom Calculator
#Geoff Murphy
#MRPGEO001
#3 April 2014

                     #DECIMAL TO NDOM
#-------------------------------------------------------------------------------

def decimal_to_ndom(a): #d
    Ndom_Number = ""    #The new Ndom number
    answer = a          #That which will be divided
    while answer >= 6:  #Since 6 in base-10 = 6 in base-6
        remainder = answer%6
        answer = answer//6
        
        New_Ndom_Number = str(remainder)
        Ndom_Number = New_Ndom_Number + Ndom_Number #Add remainder to left of Ndom number
        
    Ndom_Number = str(answer) + Ndom_Number
    answer = Ndom_Number
    return answer
    #print(eval(Ndom_Number))
    
#-------------------------------------------------------------------------------

                      #NDOM TO DECIMAL
#-------------------------------------------------------------------------------
def ndom_to_decimal(a): #n
    a_new = str(a)
    Length = len(a_new) #Length of the number

    working_number = a_new[::-1] #Number to be used backwards because (6^3,6^2,6^1,6^0)
    place = 1 #The place of the digit
    Decimal = 0 #Final Number

    for characters in str(working_number):
        if place == 1: #6^0 will be used
            Decimal += (eval(characters) * 1) #1 = 6^0, Add answer to Decimal/Final Number. The sum == the original Ndom number
            place += 1
            if (Length + 1) == place: #Resumes function until length == places, i.e. all digits taken into account
                return Decimal
                break
            continue
        elif place == 2: #6^1 will be used
            Decimal += (eval(characters) * 6)
            place += 1
            if (Length + 1) == place:
                return Decimal
                break        
            continue
        elif place == 3: #6^2 will be used
            Decimal += (eval(characters) * 36)
            place += 1
            if (Length + 1) == place:
                return Decimal
                break        
            continue

#-------------------------------------------------------------------------------
                     #NDOM ADDITION
#-------------------------------------------------------------------------------
def ndom_add(a,b): #a
    A = ndom_to_decimal(a)
    B = ndom_to_decimal(b)
    New = A + B
    answer = decimal_to_ndom(New)
    return answer
    
#-------------------------------------------------------------------------------
def ndom_multiply(a,b): #a
    A = ndom_to_decimal(a)
    B = ndom_to_decimal(b)
    New = A * B
    answer = decimal_to_ndom(New)
    return answer


    
        
        
        
        
    


