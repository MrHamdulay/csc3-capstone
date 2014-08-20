def toPigLatin(s):
   list = s.split(" ")
   for i in range(len(list)):
      if list[i][0] in ('a','e','i','o','u'):
         list[i] = list[i] + 'way'
      else:
         list[i]+= "a"
         while list[i][0] not in ('a','e','i','o','u'):
            list[i] = list[i][1::]+list[i][0]
         list[i] += "ay"
   s= list
   s=str(s)
   sentence=s.replace(",","")
   sentence=sentence.replace("[","")
   sentence=sentence.replace("]","")
   sentence=sentence.replace("'","")
   return sentence
   

def toEnglish(s):
   list = s.split(" ")
   for i in range(len(list)):
      if list[i][len(list[i])-3::1] == "way":
         list[i] = list[i][0:len(list[i])-3:1]
      else:
         if list[i][len(list[i])-2::] == "ay":
            list[i] =  list[i][:len(list[i])-2:1]
            while list[i][-1] != "a":
               list[i] = list[i][-1] + list[i][:len(list[i])-1:1]
            list[i] = list[i][:len(list[i])-1:1]
   s= list
   s=str(s)
   sentence=s.replace(",","")
   sentence=sentence.replace("[","")
   sentence=sentence.replace("]","")
   sentence=sentence.replace("'","")
   return sentence

def main ():
   toEnglish("overway")

if __name__ == "__main__":
   main ()
