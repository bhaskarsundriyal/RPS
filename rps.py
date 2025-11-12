import random
import pyfiglet
from pyfiglet import FigletFont

yellow="\033[93m"
bold="\033[1m"
RESET="\033[0m"
megenta="\033[95m"
cyan="\033[96m"
green="\033[92m"
red="\033[91m"
purple="\033[94m"





CHOISE={ 
    "rock": '✊',
    "paper": '🤚',
    "scissor": '✌️'
}
WIN=0
LOSS=0
TIE=0

print(megenta + bold +"\n 💥 ☠️  💥 APPKA HARDIK ABHINANDAN HAI ROCK ✊ PAPER 🤚  SCISSOR ✌️  MAI 💥 ☠️  💥" + RESET)
print(cyan + "═════════════════════════════════════════════════════════════════════════════════" +RESET)

while True:
    print(cyan + bold +"\n🎯 scoreboard" + RESET)
    print(yellow +f" 🏆 Win {WIN}" + RESET , end=" ")
    print(green +f"  ☠️  loss {LOSS}" + RESET , end=" ")
    print(red +f" 😐 tie {TIE}" + RESET)
    print(cyan +"="* 81 + RESET)

    user_choice=input(cyan+bold+ "\n APNI PASAND CHUNAW KAREE (ROCK, PAPER, SCISOR) Or 'q' to quit:\n" + RESET).lower()
    if user_choice == 'q':
        print(yellow + bold +"\n DHANYWAAD AAPKA KHELNE KE LIYE  👋" + RESET)
        print(green + f" ANTIM SCOREBOARD:  🏆 Win {WIN}  ☠️ loss {LOSS}  😐 tie {TIE}" + RESET)
        print(megenta +" see you again!" + RESET)
        break

    if user_choice not in CHOISE:
        print( red + bold +"\n GALAT INPIT! KRIPYA ROCK, PAPER, SCISSOR ME SE CHUNE." + RESET)
        continue
    computer_choice = random.choice(list(CHOISE))
    
    print(purple + bold +f"\n COMPUTER KA CHUNAAV HAI: {computer_choice}" + RESET)
    print(yellow + bold +f"\n AAPKA CHUNAAV HAI: {user_choice}" + RESET)

    fig = pyfiglet.Figlet(font='3-d')




    if user_choice == computer_choice:
        TIE += 1
        print(cyan + bold +"\n YE TOH TIE HO GAYA! 😐" + RESET)
        print(cyan + fig.renderText("T I E") + RESET)

        
    elif (user_choice == 'rock' and computer_choice == 'scissor') or\
            (user_choice == 'paper' and computer_choice == 'rock') or\
            (user_choice == 'scissor' and computer_choice == 'paper'):
        
        WIN += 1
        print(green + bold +"\n AAP JEET GAYE! 🏆" + RESET)
        print(cyan + fig.renderText(" W I N") + RESET)
        
    else:
         LOSS += 1
         print(red + bold +"\n AAP HAAR GAYE! ☠️" + RESET)
         print(cyan + fig.renderText(" L O S S") + RESET)
    
       
    print(cyan + "══════════════════════════════════════════════" +RESET)

    

    


    

    















