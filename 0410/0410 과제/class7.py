import random

def dice_game() :
    human = random.randint(1,6)
    print("인간: 주사위값=", human )
    ai = random.randint(1,6)
    print("컴퓨터: 주사위값=", ai )

    if human > ai :
        print("인간승리") 
    else:
        print("컴퓨터승리")  

def main() : 
    while True:
        dice_game()    
        user = input("중단할까요? Y/N")
        if user == "Y" or user == "y":
            break;

main()