def revdup(word):
    if len(word)<=1:
        return word
    elif  word[0]==word[1] :
        return revdup(word[1:])
    else:
        return word[0]+revdup(word[1:])
    

def compare(temp_original_string,nodupli):
    duplicates=len(temp_original_string)-len(nodupli)
    print('Number of pairs:',duplicates)
  
def rev(inputstring): 
    if len(inputstring)==0:
        return ''
    output=inputstring[-1]+rev(inputstring[:-1])
    return output 


info=input('Enter a message:\n')
if info==rev(info):
    print('Number of pairs:',len(info)//2)
else:
    
    x=revdup(info)
    compare(info,x)
