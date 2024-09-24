import random

def get_computer_choice():
    """Randomly select rock, paper, or scissors for the computer."""
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    """Determine the winner of the game."""
    if user_choice == computer_choice:
        return 'tie'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return 'user'
    else:
        return 'computer'

def main():
    print("Welcome to Rock-Paper-Scissors!")
    user_score = 0
    computer_score = 0

    while True:
        user_choice = input("Choose rock, paper, or scissors (or 'exit' to quit): ").lower()
        
        if user_choice == 'exit':
            print("Thanks for playing! Final Score - You: {} | Computer: {}".format(user_score, computer_score))
            break
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please try again.")
            continue

        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        winner = determine_winner(user_choice, computer_choice)

        if winner == 'user':
            print("You win!")
            user_score += 1
        elif winner == 'computer':
            print("You lose!")
            computer_score += 1
        else:
            print("It's a tie!")

        print(f"Score - You: {user_score} | Computer: {computer_score}")

        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing! Final Score - You: {} | Computer: {}".format(user_score, computer_score))
            break

if __name__ == "__main__":
    main()
