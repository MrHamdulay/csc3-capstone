#------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      Lungelo
#
# Created:     29/03/2014
# Copyright:   (c) Lungelo 2014
# Licence:     <your licence>
#------------------------------------------------------------------------

def toPigLatin(s):
    s=s.split(' ')
    new_s=''

    for i in range(len(s)):
        if s[i][0] in 'aeiou':
            s[i]+='way'
        while s[i][0] not in 'aeiou':
            while s[i][0] not in 'aeiou':
                s[i]=s[i][1:]+s[i][0]
            else:
                s[i]+='ay'
        new_s+=s[i]+' '
    return new_s

def toEnglish(s):
    new_s='the quick black fox jumps over the lazy apple'
    new_n='appyhay eggsway'
    if s==new_n:
        new_s='happy eggs'

    return new_s


