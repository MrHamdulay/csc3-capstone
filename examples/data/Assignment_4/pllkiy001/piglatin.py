def toPigLatin(s):

    split=s.split(" ")

    new=""

    k=0

    for i in split:

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

        if(k!=len(split)-1):

            new+=" "

        k+=1

    return new