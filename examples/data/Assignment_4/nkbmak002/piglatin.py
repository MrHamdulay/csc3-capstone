

def toPigLatin(b):

     k = b.split()
     message=''
     for chr in k:
          
          a =  chr[0]

          if a in "aeiou" or a in "AEIOU":
               message+= chr+"way"+' '
          else:
               track = ""
               for b in chr:
                    if not b in "aeiou" and not b in "AEIOU":
                         track+=b
                    else:
                         break
               message+= chr[len(track):]+"a"+track+"ay"+' '
     return message


def toEnglish(b):
     k = b.split()
     message=''
     for chr in k:
          
          a =  chr[len(chr)-3:len(chr)]

          if a == "way":
               message+= chr[:len(chr)-3]+" "
          else:
               chr = chr[:len(chr)-2]
               track = ""
               for b in chr[::-1]:
                    if not b is 'a':
                         track+=b
                    else:
                         break
                    chr=chr[:len(chr)-1]
               message+= track[::-1]+chr[:len(chr)-1]+" "
     return message
             
     