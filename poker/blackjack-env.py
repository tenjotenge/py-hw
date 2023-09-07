import random

class BlackjackEnvironment:
    def __init__(self, num_players):
        self.num_players = num_players
        self.deck = self.generate_deck()
        self.players = [self.initialize_player() for _ in range(num_players)]

    def generate_deck(self):
        # Create a standard deck of 52 cards
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        deck = [{'rank': rank, 'suit': suit} for rank in ranks for suit in suits]
        random.shuffle(deck)
        return deck

    def initialize_player(self):
        # Initialize a player with an empty hand
        return {'hand': []}

    def deal_card(self, player):
        card = self.deck.pop()
        player['hand'].append(card)

    def calculate_hand_value(self, hand):
        # Calculate the value of a player's hand in Blackjack
        value = 0
        num_aces = 0

        for card in hand:
            rank = card['rank']
            if rank == 'A':
                value += 11
                num_aces += 1
            elif rank in ['K', 'Q', 'J']:
                value += 10
            else:
                value += int(rank)

        # Adjust for aces
        while num_aces > 0 and value > 21:
            value -= 10
            num_aces -= 1

        return value

    def play_game(self):
        # Deal two initial cards to each player
        for _ in range(2):
            for player in self.players:
                self.deal_card(player)

        # Players take turns to play
        for player in self.players:
            while self.calculate_hand_value(player['hand']) < 16:
                self.deal_card(player)

    def display_hands(self):
        for i, player in enumerate(self.players):
            hand_value = self.calculate_hand_value(player['hand'])
            print(f"Player {i + 1} Hand: {', '.join([f'{card['rank']} of {card['suit']}' for card in player['hand']])} (Value: {hand_value})")


if __name__ == "__main__":
    num_players = 2
    blackjack_env = BlackjackEnvironment(num_players)
    blackjack_env.play_game()
    blackjack_env.display_hands()
