#glnrus002
#question 3
def toPigLatin (s):# to return the Pig Latin string for a given English string
   vowels="aeiouAEIOU"
   consonents="qQwWrRtTyYpPsSdDfFgGhHjJkKlLzZxXcCvVbBnNmM" 
   new_string=""
   l=len(s.split(" "))
   word=s.split(" ")[::]
   for i in range (l):
      if (word[i])[0] in vowels:
         new_string=new_string+word[i]+"way "
      elif ((word[i])[0]) in consonents and (word[i][1]) in consonents:##
         wo=word[i]
         first_two_letters=wo[0]+wo[1]
         wo=wo[2::]+"a"+first_two_letters+"ay "
         new_string=new_string+wo
      else:
         wo=word[i]
         first_two_letters=wo[0]
         wo=wo[1::]+"a"+first_two_letters+"ay "
         new_string=new_string+wo
   new_string=new_string[:-1:]      
   return new_string
        
def toEnglish (s):# to return the English string for a given Pig Latin string
   vowels="aeiouAEIOU"
   consonents="qQwWrRtTyYpPsSdDfFgGhHjJkKlLzZxXcCvVbBnNmM" 
   new_string=""
   l=len(s.split(" "))
   word=s.split(" ")[::] 
   for i in range (l):
      word_work=word[i]
      word_length=len(word_work)
      q=word_work[(word_length-3)::]  
      if  q=="way":
         new_string=new_string+word_work.replace("way","")+" "
      if q!="way":
         q=word_work[(word_length-2)::] # first q was the last three letters, which might have not been a w, so remove that from q  
         we=word_work[0:(word_length-2)]  #removes 'ay' from word   
         last_two_letters=we[-2::]# determines what last two letters in word are so that it c an be used to test where the additional 'a' might be
         if q=="ay"and last_two_letters[0] in consonents and last_two_letters[1] in consonents : 
            we=word_work[0:(word_length-2)]#removes last two letters from word
            back2=we[-2]+we[-1]
            word_with_front=back2+we[:-3:]
            new_string=new_string+word_with_front+" "
         else:
            we=word_work[0:(word_length-1)]#removes back a
            letter=we[-2]#gets first letter
            we=letter+we[0:-3]
            new_string=new_string+we+" "            
   return new_string[:-1:]#take last letters bring them to front, drop a
