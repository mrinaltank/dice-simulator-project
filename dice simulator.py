import random

def roll_dice():
    # Generate a random number between 1 and 6 (inclusive) to simulate a dice roll
    return random.randint(1, 6)

def main():
    print("Welcome to the Dice Simulator!")
    while True:
        input("Press Enter to roll the dice...")
        dice_result = roll_dice()
        print(f"You rolled: {dice_result}")
        
        play_again = input("Do you want to roll again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thank you for playing!")
            break

if __name__ == "__main__":
    main()
