import random

choices = ["rock", "paper", "scissors"]

print("🎮 Rock, Paper, Scissors!")
print("Type 'quit' to exit.")

while True:
    player = input("\nChoose rock, paper, or scissors: ").lower()

    if player == "quit":
        print("Thanks for playing! 👋")
        break;

    if player not in choices:
        print("❌ Invalid choice. Try again!")
        continue

    computer = random.choice(choices)

    print("You chose:", player)
    print("Computer chose:", computer)

    if player == computer:
        print("🤝 It's a tie!")

    elif (
        (player == "rock" and computer == "scissors") or
        (player == "paper" and computer == "rock") or
        (player == "scissors" and computer == "paper")
    ):
        print("🎉 You win!")

    else:
        print("😢 Computer wins!")
