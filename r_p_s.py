import random

emojis = {'r': '🪨', 'p': '📄', 's': '✂️'}
games = ('r', 'p', 's')

while True:
    ask = input("Do you want to play? (y/n): ").lower()
    if ask == "y":
        print("Great! Let's start.")
        player = input("rock, paper, or scissor? (r/p/s): ").lower()
        if player not in games:
            print("No, you can't play with that, try again")
            continue
        bot = random.choice(games)

        print(f"You chose {emojis[player]}")
        print(f"Bot chose {emojis[bot]}")

        if player == bot:
            print("Tie")
        elif (
            (player == 'r' and bot == 's') or
            (player == 's' and bot == 'p') or
            (player == 'p' and bot == 'r')):
            print("You win!")
        else:
            print("You lose")

        is_continue = input("Do you want to play again? (y/n): ").lower()
        if is_continue == "y":
            continue
        elif is_continue == "n":
            print("Okay, Maybe next time")
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
    elif ask == "n":
        print("Okay, Maybe next time")
        break
