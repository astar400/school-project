#%%
from colorama import Fore,Style
print('THIS IS A HOUSE. THERE IS PRIZE HIDDEN IN ONE OF THE ROOMS.')
print('ALL YOU GOTTA DO IS GUESS THE ROOM IN WHICH THE PRIZE IS HIDDEN.')
print('YOU HAVE 3 CHANCES TO GUESS THE ROOM BEFORE YOU LOSE. WATCH OUT FOR THE CHANCEMETER AND GOOD LUCK!')
print('____________________________________________________________')
print('                              |                            |')
print('                              |                            |')
print('                              |                            |')
print('    KITCHEN                   |                            |')
print('                              |                            |')
print('                              |         LIVING             |')
print('______________________________|          ROOM              |')
print('                              |                            |')
print('                              |                            |')
print('                              |                            |')
print('                              |                            |')
print('                              |                            |')
print('                              |                            |')
print('     BEDROOM                  |                            |')
print('                              |                            |')
print('                              |______________--------______|')
print('                              |          |     DOOR')
print('                              |          |      ** ')
print('                              |          | you are here')
print('                              | STORE    |')
print('______________________________| ROOM     |')
print('                              |          |')
print('                              |          |')
print('                              |          |')
print('   WASHROOM                   |          |')
print('                              |          |')
print('                              |          |')
print('                              |          |')
print('______________________________|__________|')
print('CHANCES LEFT:3')
print('    ')
print('     ')
print('     ')
chances=3
gamewin=False
p=['KITCHEN','STORE ROOM','LIVING ROOM','WASHROOM','BEDROOM']
import random
l=random.choice(p)

k=input('ENTER YOUR GUESS:')
m=k.upper()
while gamewin==False:
    if m==l:
        print(Fore.GREEN+ 'SPECTACULAR GUESSING SKILLS!! ACHIEVEMENT UNLOCKED "GUESS LEVEL = 100"')
        print(Style.RESET_ALL)
        gamewin=True
        break
    elif m==l and chances>=0:
        print(Fore.GREEN+'SPECTACULAR GUESSING SKILLS! ACHIEVEMENT UNLOCKED "GUESS LEVEL = 100"')
        print(Style.RESET_ALL)
        gamewin=True
    elif m!=l:
        chances=chances-1
        if chances==0 and  gamewin==False:
            print(Fore.RED+'OOPS SORRY, YOU LOST!')
            print(Style.RESET_ALL)
            gamewin=True
            break
        else:
            pass
        if m=='WASHROOM':
            print('____________________________________________________________')
            print('                              |                            |')
            print('                              |                            |')
            print('                              |                            |')
            print('    KITCHEN                   |                            |')
            print('                              |                            |')
            print('                              |         LIVING             |')
            print('______________________________|          ROOM              |')
            print('                              |                            |')
            print('                              |                            |')
            print('                              |                            |')
            print('                              |                            |')
            print('                              |                            |')
            print('                              |                            |')
            print('     BEDROOM                  |                            |')
            print('                              |                            |')
            print('                              |______________--------______|')
            print('                              |          |     DOOR')
            print('                              |          |')
            print('                              |          |')
            print('                              | STORE    |')
            print('______________________________| ROOM     |')
            print('                              |          |')
            print('                              |          |')
            print('                              |          |')
            print('   WASHROOM                   |          |')
            print('      **                      |          |')
            print('  you are here                |          |')
            print('                              |          |')
            print('______________________________|__________|')
            print('CHANCES LEFT:',chances)
        elif m=='LIVING ROOM':
            print('____________________________________________________________')
            print('                              |                            |')
            print('                              |                            |')
            print('                              |                            |')
            print('    KITCHEN                   |                            |')
            print('                              |                            |')
            print('                              |         LIVING             |')
            print('______________________________|          ROOM              |')
            print('                              |           **               |')
            print('                              |       you are here         |')
            print('                              |                            |')
            print('                              |                            |')
            print('                              |                            |')
            print('                              |                            |')
            print('     BEDROOM                  |                            |')
            print('                              |                            |')
            print('                              |______________--------______|')
            print('                              |          |     DOOR')
            print('                              |          |')
            print('                              |          |')
            print('                              | STORE    |')
            print('______________________________| ROOM     |')
            print('                              |          |')
            print('                              |          |')
            print('                              |          |')
            print('   WASHROOM                   |          |')
            print('                              |          |')
            print('                              |          |')
            print('                              |          |')
            print('______________________________|__________|')
            print('CHANCES LEFT:',chances)
        elif m=='BEDROOM':
            print('____________________________________________________________')
            print('                              |                            |')
            print('                              |                            |')
            print('                              |                            |')
            print('    KITCHEN                   |                            |')
            print('                              |                            |')
            print('                              |         LIVING             |')
            print('______________________________|          ROOM              |')
            print('                              |                            |')
            print('                              |                            |')
            print('                              |                            |')
            print('                              |                            |')
            print('                              |                            |')
            print('                              |                            |')
            print('     BEDROOM                  |                            |')
            print('       **                     |                            |')
            print('   you are here               |______________--------______|')
            print('                              |          |     DOOR')
            print('                              |          |')
            print('                              |          |')
            print('                              | STORE    |')
            print('______________________________| ROOM     |')
            print('                              |          |')
            print('                              |          |')
            print('                              |          |')
            print('   WASHROOM                   |          |')
            print('                              |          |')
            print('                              |          |')
            print('                              |          |')
            print('______________________________|__________|')
            print('CHANCES LEFT:',chances)
        elif m=='KITCHEN':
            print('____________________________________________________________')
            print('                              |                            |')
            print('                              |                            |')
            print('                              |                            |')
            print('    KITCHEN                   |                            |')
            print('    **                        |                            |')
            print('      YOU ARE HERE            |         LIVING             |')
            print('______________________________|          ROOM              |')
            print('                              |                            |')
            print('                              |                            |')
            print('                              |                            |')
            print('                              |                            |')
            print('                              |                            |')
            print('                              |                            |')
            print('     BEDROOM                  |                            |')
            print('                              |                            |')
            print('                              |______________--------______|')
            print('                              |          |     DOOR')
            print('                              |          |')
            print('                              |          |')
            print('                              | STORE    |')
            print('______________________________| ROOM     |')
            print('                              |          |')
            print('                              |          |')
            print('                              |          |')
            print('   WASHROOM                   |          |')
            print('                              |          |')
            print('                              |          |')
            print('                              |          |')
            print('______________________________|__________|')
            print('CHANCES LEFT:',chances)
        elif m=='STORE ROOM':
            print('____________________________________________________________')
            print('                              |                            |')
            print('                              |                            |')
            print('                              |                            |')
            print('    KITCHEN                   |                            |')
            print('                              |                            |')
            print('                              |         LIVING             |')
            print('______________________________|          ROOM              |')
            print('                              |                            |')
            print('                              |                            |')
            print('                              |                            |')
            print('                              |                            |')
            print('                              |                            |')
            print('                              |                            |')
            print('     BEDROOM                  |                            |')
            print('                              |                            |')
            print('                              |______________--------______|')
            print('                              |          |     DOOR')
            print('                              |          |')
            print('                              |          |')
            print('                              | STORE    |')
            print('______________________________| ROOM     |')
            print('                              |  **      |')
            print('                              | you are  |')
            print('                              |  here    |')
            print('   WASHROOM                   |          |')
            print('                              |          |')
            print('                              |          |')
            print('                              |          |')
            print('______________________________|__________|')
            print('CHANCES LEFT:',chances)
        k=input(Fore.BLUE+'Wrong Guess Mate, Try Again:')
        print(Style.RESET_ALL)
        m=k.upper()
print(Fore.MAGENTA+l,'was the correct room MR.SHERLOCK')
print(Style.RESET_ALL)
input()