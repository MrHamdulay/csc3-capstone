def get_integer(character):
   character1 = input("Enter "+character+":\n")
   while not character1.isdigit ():
      character1 = input ("Enter "+character+":\n")
   character1 = eval (character1)
   return character1
def calc_factorial(integer):
   integerfactorial = 1
   for i in range (1, integer+1):
      integerfactorial *= i 
   return integerfactorial
