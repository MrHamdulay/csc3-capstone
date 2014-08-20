# program to check validity of time entered by user
# nomsa gamedze
# 26 february 2014

hours = eval(input('\n'"Enter the hours: "))

minutes = eval(input('\n'"Enter the minutes: "))

seconds = eval(input('\n'"Enter the seconds: "))


def main():
                if not 0<=hours<=23:
                                print('\n'"Your time is invalid.")
                if not 0<=minutes<=59:
                                print('\n'"Your time is invalid.")
                
                if not 0<=seconds<=59:
                                print('\n'"Your time is invalid.")
                elif 0<=hours<=23 and 0<=minutes<=59 and 0<=seconds<=59:
                                print('\n'"Your time is valid.")

main()