def get_integer(variable):
   letter = input ("Enter" + " " + variable + ":\n")
   while not letter.isdigit ():
      letter = input ("Enter" + " " + variable + ":\n")
   letter = eval (letter)
   return letter

def calc_factorial (variable):
   variablefactorial = 1
   for i in range (1, variable+1):
      variablefactorial *= i
   return variablefactorial