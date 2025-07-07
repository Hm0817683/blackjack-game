import random
import os
from art import logo

print(logo)
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    """Calculates the score from a list of cards."""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    while sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(u_score, c_score):
    """Compares scores and declares the result."""
    if u_score == c_score:
        return "🤝 It's a draw."
    elif c_score == 0:
        return "😞 You lose! Opponent has Blackjack 🃏."
    elif u_score == 0:
        return "🎉 Win with a Blackjack! 🃏"
    elif u_score > 21:
        return "💥 You went over 21. You lose! 😢"
    elif c_score > 21:
        return "🔥 Opponent went over 21. You win! 🥳"
    elif u_score > c_score:
        return "🏆 You win! 😎"
    else:
        return "🙁 You lose. Better luck next time!"


# Main game loop
while True:
    clear_screen()
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"\nYour cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while calculate_score(computer_cards) < 17:
        computer_cards.append(deal_card())

    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    print(f"\nYour final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

    decision = input("\nDo you want to restart the game? Type 'y' or 'n': ").lower()
    if decision == 'y':
        print(logo)
    if decision != 'y':
        print("Thanks for playing!")
        break
