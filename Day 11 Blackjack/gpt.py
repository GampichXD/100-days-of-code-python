import random

def clear_screen():
    # Clear the console screen
    print("\n" * 50)

def print_logo():
    # Print a logo or simple welcome message
    print("=" * 30)
    print("     WELCOME TO BLACKJACK     ")
    print("=" * 30)

def ask_to_play():
    while True:
        ask_to_play = input("Do you want to play Blackjack with me? (y/n): ").lower()
        if ask_to_play in ['y', 'n']:
            return ask_to_play == 'y'
        print("Invalid input. Please enter 'y' or 'n'.")

def calculate_score(cards):
    score = sum(cards)
    if 11 in cards and score > 21:
        # Convert Ace (11) to 1 if score exceeds 21
        score -= 10
    return score

def draw_card():
    # Draw a random card
    return random.choice([11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10])

def computer_strategy(computer_cards):
    while calculate_score(computer_cards) < 17:
        computer_cards.append(draw_card())
    return computer_cards

def display_status(player_cards, computer_cards, reveal_computer=False):
    print(f"Your cards: {player_cards}, current score: {calculate_score(player_cards)}")
    if reveal_computer:
        print(f"Computer's cards: {computer_cards}, final score: {calculate_score(computer_cards)}")
    else:
        print(f"Computer's first card: {computer_cards[0]}")

def determine_winner(player_score, computer_score):
    if player_score > 21:
        return "You went over 21. You lose!"
    elif computer_score > 21:
        return "Computer went over 21. You win!"
    elif player_score == computer_score:
        return "It's a draw!"
    elif player_score == 21:
        return "Blackjack! You win!"
    elif computer_score == 21:
        return "Computer got Blackjack! You lose!"
    elif player_score > computer_score:
        return "You win!"
    else:
        return "You lose!"

def blackjack():
    clear_screen()
    print_logo()

    # Initial card distribution
    player_cards = [draw_card(), draw_card()]
    computer_cards = [draw_card(), draw_card()]

    game_over = False

    while not game_over:
        display_status(player_cards, computer_cards)

        if calculate_score(player_cards) == 21:
            game_over = True
            continue

        action = input("Type 'y' to draw another card, 'n' to pass: ").lower()
        if action == 'y':
            player_cards.append(draw_card())
            if calculate_score(player_cards) > 21:
                game_over = True
        elif action == 'n':
            game_over = True

    # Computer's turn
    computer_cards = computer_strategy(computer_cards)

    # Final scores and result
    clear_screen()
    print_logo()
    display_status(player_cards, computer_cards, reveal_computer=True)

    player_score = calculate_score(player_cards)
    computer_score = calculate_score(computer_cards)
    result = determine_winner(player_score, computer_score)
    print(result)

def main():
    while True:
        if ask_to_play():
            blackjack()
        else:
            print("Thanks for visiting! Goodbye!")
            break

if __name__ == "__main__":
    main()