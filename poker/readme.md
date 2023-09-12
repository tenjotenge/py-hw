/blackjack/readme.md

action space:
- bet (must do to start round)
- hit (pulls another card to players hand)
- stand (self explanatory)
- split (If the first two cards are a pair, the players are allowed to split those, thus creating two hands rather than the normal one per seat. To fund the split, the player has to place a second bet, of equal value to the first.)
- double down (After receiving the first two cards, players can double their bet while hitting. When doubling down, player receives one extra card only and cannot hit again. Most casinos allow cards to be split again if the second card makes another pair - but some have limits on the number of times a player can split.)
- insurance (Insurance is a side bet, which is offered to the players when the dealer’s up card is an ace. It insures the player against the dealer having a ‘blackjack’ and gives them a chance to break even on the hand, if the dealer’s cards total 21.
Insurance is offered before the dealer checks their face-down card.)
- surrender (If a player believes they will be unable to beat dealer’s hand, they can choose to ‘surrender’. In this strategy, players fold the hand, and risk loosing only half of the bet, rather than the whole amount.
A player can only forfeit their hand before receiving extra cards.)
- bet behind [will not be inlcuded in agents actual action space, but for real players it is a possible action in certain casinos] (Busy, live casinos sometimes offer an option to take side bets, otherwise known as ‘bet behind’. This is where a limitless number of people take a bet behind the main seven seated players, wagering that they will win the hand.)
