#-------------------------------------------------------------------------------
# Name:        Vending Machine
# Purpose:     Return change in the form of coins only
#
# Author:      Taylor
#
# Created:     13/04/2014
# Copyright:   (c) Taylor 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    cost = eval(input("Enter the cost (in cents):\n"))
    deposit = eval(input("Deposit a coin or note (in cents):\n"))

    while True:

        if deposit < cost:
            deposit = eval(input("Deposit a coin or note (in cents):\n")) + deposit
            continue
        else:
            change = deposit - cost



            if change >= 100:
                #change is equal to 100 cents
                #done


                if change == 100:
                    dollars = change//100
                    result = print("Your change is:\n{0} x $1".format(dollars))
                    break
                #change is greater than 100 cents
                else:
                    dollars = change//100
                    cents = change % 100
                    #done
                    if not cents:
                        result = print("Your change is:\n{0} x $1".format(dollars))
                        break
                    elif 5>cents>=1:
                        result = print("Your change is:\n{0} x $1\n{1} x 1c".format(dollars, cents))
                        break
                    #done


                    elif 10 > cents >= 5:
                        dimes = cents//5
                        cents = cents % 5
                        if cents:
                            result = print("Your change is:\n{0} x $1\n{1} x 5c\n{2} x 1c".format(dollars, dimes, cents))
                            break
                        elif not cents:
                            result = print("Your change is:\n{0} x $1\n{1} x 5c".format(dollars, dimes))
                            break
                    elif 25 > cents >= 10:
                        if cents == 10:
                            result = print("Your change is:\n{0} x $1\n1 x 10c".format(dollars))
                            break
                        else:
                            nikels = cents//10
                            cents = cents%10

                            if cents:

                                if cents < 5:
                                    result = print("Your change is:\n{0} x $1:\n{1} x 10c:\n{2} x 1c".format(dollars, nikels, cents))
                                    break
                                elif cents >= 5:
                                    if cents == 5:
                                        result = print("Your change is:\n{0} x $1:\n{1} x 10c:\n1 x 5c".format(dollars, nikels))
                                        break
                                    else:
                                        dimes = cents//5
                                        cents = cents%5
                                        result = print("Your change is:\n{0} x $1:\n{1} x 10c:\n{2} x 5c\n{3} x 1c".format(dollars, nikels, dimes, cents))
                                        break
                            else:
                                result = print("Your change is:\n{0} x $1\n{1} x 10c".format(dollars, nikels))
                                break


                    elif 100 > cents >= 25:
                        if cents%25 == 0:
                            quarters = cents//25
                            result = print("Your change is:\n{0} x $1\n{1} x 25c".format(dollars, quarters))
                            break
                        else:
                            quarters = cents//25
                            cents = cents%25



                            if 5 > cents > 1:
                                result = print("Your change is:\n{0} x $1\n{1} x 25c\n{2} x 1c".format(dollars, quarters, cents))
                                break
                            #done


                            elif 10 > cents >= 5:
                                dimes = cents//5
                                cents = cents % 5
                                if cents:
                                    result = print("Your change is:\n{0} x $1\n{1} x 25c\n{2} x 5c\n{3} x 1c".format(dollars, quarters, dimes, cents))
                                    break
                                elif not cents:
                                    result = print("Your change is:\n{0} x $1\n{1} x 25c\n{2} x 5c".format(dollars, quarters, dimes))
                                break
                            elif 25 > cents >= 10:
                                if cents == 10:
                                    result = print("Your change is:\n{0} x $1\n{1} x 25c\n1 x 10c".format(dollars, quarters, nikels))
                                    break
                                else:
                                    nikels = cents//10
                                    cents = cents%10

                                    if cents:

                                        if cents < 5:
                                            result = print("Your change is:\n{0} x $1\n{1} x 25c\n{2} x 10c\n{3} x 1c".format(dollars, quarters, nikels, cents))
                                            break
                                        elif cents >= 5:
                                            if cents == 5:
                                                result = print("Your change is:\n{0} x $1\n{1} x 25c\n{2} x 10c\n1 x 5c".format(dollars, quarters, nikels))
                                                break
                                            else:
                                                dimes = cents//5
                                                cents = cents%5
                                                result = print("Your change is:\n{0} x $1\n{1} x 25c\n{2} x 10c\n{3} x 5c\n{4} x 1c".format(dollars , quarters, nikels, dimes, cents))
                                                break
                                    else:
                                        result = print("Your change is:\n{0} x $1\n{1} x 25c\n{2} x 10c".format(dollars, quarters, nikels))
                                        break




            else:
                 cents = change
                 if 5 > cents > 1:
                    cents = cents
                    break
                 elif 10 > cents >= 5:
                    dollars = 0
                    cents = cents/5
                    single_cents = cents % 5
                    break
                 elif 25 > cents >= 10:
                    dollars = 0
                    cents = cents/10
                    single_cents = cents % 10
                 elif 100 > cents >= 25:
                    dollars = 0
                    cents = cents/25
                    single_cents = cents % 25
                    break

    return(result)

if __name__ == '__main__':
    main()
