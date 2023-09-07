import numpy as np

class PokerEnvironment:
    def __init__(self, num_players):
        self.num_players = num_players
        self.deck = self.generate_deck()
        self.players = [self.initialize_player() for _ in range(num_players)]
        self.community_cards = []
        self.current_player = 0
        self.pot = 0
        self.small_blind = 10
        self.big_blind = 20
        self.current_bet = 0
        self.current_round = 'pre-flop'

    def generate_deck(self):
        # Create a standard deck of 52 cards
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        deck = [{'rank': rank, 'suit': suit} for rank in ranks for suit in suits]
        return deck

    def initialize_player(self):
        # Initialize a player with starting chips and an empty hand
        return {
            'chips': 1000,
            'hand': [],
            'bet': 0,
            'folded': False
        }

    def deal_hole_cards(self):
        # Deal two hole cards to each player
        for _ in range(2):
            for player in self.players:
                card = self.deck.pop()
                player['hand'].append(card)

    def start_betting_round(self):
        self.current_bet = 0
        self.current_round = 'pre-flop' if len(self.community_cards) == 0 else 'flop' if len(self.community_cards) == 3 else 'turn' if len(self.community_cards) == 4 else 'river'

    def next_player(self):
        self.current_player = (self.current_player + 1) % self.num_players

    def collect_bets(self):
        for player in self.players:
            if not player['folded']:
                player['chips'] -= player['bet']
                self.pot += player['bet']
                player['bet'] = 0

    def deal_community_cards(self):
        if self.current_round == 'flop':
            self.community_cards.extend(self.deck.pop() for _ in range(3))
        elif self.current_round in ('turn', 'river'):
            self.community_cards.append(self.deck.pop())

    def rank_hand(self, player_hand):
        # Evaluate and rank the player's hand.
        ranks = '23456789TJQKA'
        rank_counts = {rank: 0 for rank in ranks}
        suit_counts = {}

        for card in player_hand:
            rank_counts[card['rank']] += 1
            if card['suit'] in suit_counts:
                suit_counts[card['suit']] += 1
            else:
                suit_counts[card['suit']] = 1

        is_flush = any(count >= 5 for count in suit_counts.values())
        is_straight = False

        for i in range(len(ranks) - 4):
            if all(rank_counts[ranks[j]] >= 1 for j in range(i, i + 5)):
                is_straight = True
                break

        if is_flush and is_straight:
            return 9  # Straight flush
        elif any(count == 4 for count in rank_counts.values()):
            return 8  # Four of a kind
        elif all(count == 3 or count == 2 for count in rank_counts.values()):
            return 7  # Full house
        elif is_flush:
            return 6  # Flush
        elif is_straight:
            return 5  # Straight
        elif any(count == 3 for count in rank_counts.values()):
            return 4  # Three of a kind
        elif sum(1 for count in rank_counts.values() if count == 2) == 2:
            return 3  # Two pair
        elif any(count == 2 for count in rank_counts.values()):
            return 2  # One pair
        else:
            return 1  # High card

    def determine_winner(self):
        winners = []
        best_hand_rank = -1

        for player in self.players:
            if not player['folded']:
                player_hand = self.evaluate_hand(player)
                hand_rank = self.rank_hand(player_hand)

                if hand_rank > best_hand_rank:
                    best_hand_rank = hand_rank
                    winners = [player]
                elif hand_rank == best_hand_rank:
                    winners.append(player)

        # Distribute the pot to the winning player(s).
        if len(winners) == 1:
            winner = winners[0]
            winner['chips'] += self.pot
            print(f"Player {winners[0]} wins the pot of {self.pot} chips with a {self.get_hand_name(best_hand_rank)}.")
        else:
            # Handle a split pot by equally distributing chips among winners.
            split_pot = self.pot // len(winners)
            for winner in winners:
                winner['chips'] += split_pot
                print(f"Player {winner} wins {split_pot} chips with a {self.get_hand_name(best_hand_rank)}.")

        # Reset the game state.
        self.reset_game()

    def get_hand_name(self, rank):
        hand_names = {
            1: "High Card",
            2: "One Pair",
            3: "Two Pair",
            4: "Three of a Kind",
            5: "Straight",
            6: "Flush",
            7: "Full House",
            8: "Four of a Kind",
            9: "Straight Flush",
        }
        return hand_names.get(rank, "Unknown")

    def play_game(self):
        self.deal_hole_cards()
        for _ in range(4):  # Four betting rounds: pre-flop, flop, turn, river
            self.start_betting_round()
            while not all(player['bet'] == self.current_bet or player['folded'] for player in self.players):
                current_player = self.players[self.current_player]
                if not current_player['folded']:
                    # Implement AI agent's decision-making logic here.
                    # You can use your trained AI agents to decide actions.
                    # For simplicity, assume random actions for now.
                    action = np.random.choice(['fold', 'call', 'raise'])
                    if action == 'fold':
                        current_player['folded'] = True
                    elif action == 'call':
                        current_player['bet'] = self.current_bet
                    else:
                        raise_amount = np.random.randint(10, 101)  # Random raise amount between 10 and 100
                        current_player['bet'] = self.current_bet + raise_amount
                        self.current_bet = current_player['bet']
                self.next_player()
            self.collect_bets()
            if self.current_round != 'river':
                self.deal_community_cards()

        self.determine_winner()
        # Distribute the pot to the winning player(s) and reset the game state.

if __name__ == "__main__":
    num_players = 2
    poker_env = PokerEnvironment(num_players)
    poker_env.play_game()
