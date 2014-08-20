def toPigLatin(s):

    s=s.split(" ")

    new=""

    k=0

    for i in s:

        temp=i[0]

        t=1

        if(i[0] in {'a','e','i','o','u'}):

            new+=i+"way"

        else:

            

            while((t<=len(i)-1) and (i[t] not in {'a','e','i','o','u'})):

                temp+=i[t]

                t+=1

            if(t<=len(i)-1):

                new+=i[t:len(i)]+"a"+temp+"ay"

            else:

                new+="a"+temp+"ay"

        if(k!=len(s)-1):

            new+=" "

        k+=1

    return new




def toEnglish(s):

    s=s.split(" ")

    new=""

    k=0

    for i in s:

        t=len(i)-3

        temp=""

        c=0

        for j in i:

            if(j=='w'):

                new+=i[0:len(i)-3]

                c+=1

        if(c==0):

            while(i[t+1-1] not in {'a','e','i','o','u'}):

                temp+=i[t]

                t-=1

            new+=temp[::-1]+i[0:t]

        if(k!=len(s)-1):

            new+=" "

        k+=1

    return new       