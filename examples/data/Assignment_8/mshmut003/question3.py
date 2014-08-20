# Encryption by use recursion
# Mutali Mashamba
# [day] May 2014

msg = input('Enter a message:\n')

def encryption(sequence):
  if sequence == '' :
    return ''
  
  # if theres 'z', we start from 'a' again
  elif sequence[0] == 'z' :
    return 'a' + encryption(sequence[1:])
  
  # is it lower case or is it not??
  elif sequence[0].islower():
    new_seq = ord(sequence[0]) +1
    return chr(new_seq) + encryption(sequence[1:])
  
  # Encrypts only lower case characters, Upper case is returned as is
  else :
    return sequence[0] + encryption(sequence[1:])
  
print('Encrypted message:\n', encryption(msg), sep='')
    
  
  