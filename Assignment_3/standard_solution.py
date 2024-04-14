import random
from enum import Enum
from typing import Any

class Choice(Enum):
    """
    Enum representing the possible choices in the game.
    """
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

    def __lt__(self, other: Any) -> bool:
        """
        Overload the less than operator to determine the winner.

        Args:
            other (Any): The other choice to compare against.

        Returns:
            bool: True if self is less than other, False otherwise.
        """
        if self.value == other.value:
            return False
        return (self.value - other.value) % 3 == 2

    def __gt__(self, other: Any) -> bool:
        """
        Overload the greater than operator to determine the winner.

        Args:
            other (Any): The other choice to compare against.

        Returns:
            bool: True if self is greater than other, False otherwise.
        """
        if self.value == other.value:
            return False
        return (other.value - self.value) % 3 == 2

def get_computer_choice() -> Choice:
    """
    Get a random choice for the computer.

    Returns:
        Choice: A random choice from the Choice enum.
    """
    return random.choice(list(Choice))

def get_winner(player_choice: Choice, computer_choice: Choice) -> str:
    """
    Determine the winner of the game.

    Args:
        player_choice (Choice): The player's choice.
        computer_choice (Choice): The computer's choice.

    Returns:
        str: "Player" if the player wins, "Computer" if the computer wins, or "Draw" if it's a draw.
    """
    if computer_choice > player_choice:
        return "Computer"
    elif player_choice > computer_choice:
        return "Player"
    return "Draw"

def play_game() -> None:
    """
    Play the Rock-Paper-Scissors game.
    """
    player_wins = 0
    computer_wins = 0
    draws = 0

    while True:
        # Get the computer's choice
        computer_choice = get_computer_choice()

        # Get the player's choice
        player_choice_str = input("Enter your choice (Rock, Paper, Scissors): ").capitalize()
        try:
            player_choice = Choice[player_choice_str]
        except KeyError:
            print("Invalid choice. Please try again.")
            continue

        # Display the computer's choice
        print(f"Computer's choice: {computer_choice.name}")

        # Determine the winner
        winner = get_winner(player_choice, computer_choice)
        if winner == "Draw":
            print("It's a draw!")
            draws += 1
        elif winner == "Player":
            print("You win!")
            player_wins += 1
        else:
            print("Computer wins!")
            computer_wins += 1

        # Ask if the player wants to play again
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != "y":
            break

    # Display the final scores
    print(f"Player wins: {player_wins}")
    print(f"Computer wins: {computer_wins}")
    print(f"Draws: {draws}")

# Start the game
if __name__ == "__main__":
    play_game()
