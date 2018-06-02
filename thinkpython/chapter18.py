import random
from operator import itemgetter, attrgetter

class Card:
  """Represents a standard playing card"""

  suit_names = ["Clubs", "Diamonds", "Hearts", "Spades"]
  rank_names = [None, "Aces", '2', '3', '4', '5', '6', '7', '8', '9', '10', "Jack", "Queen", "King"]

  def __init__(self, suit=0, rank=2):
    self.suit = suit
    self.rank = rank

  def __str__(self):
    return "{:s} of {:s}".format(Card.rank_names[self.rank], Card.suit_names[self.suit])

  def __lt__(self, other):
    # check the suit
    t1 = self.suit, self.rank
    t2 = other.suit, other.rank
    return t1 < t2
 
  def __eq__(self, other):
    """Check whether self or other have the same rank and suit
    return boolean
    """
    return self.suit == other.suit and self.rank == other.rank

  def __hash__(self):
    return hash(self.rank)

class Deck:
  """Represents a deck of cards"""

  def __init__(self):
    self.cards = []
    for suit in range(4):
      for rank in range(1, 14):
        card = Card(suit, rank)
        self.cards.append(card)

  def __str__(self):
    res = []
    for card in self.cards:
      res.append(str(card))
    return ", ".join(res)

  def pop_card(self):
    return self.cards.pop()

  def add_card(self, card):
    return self.cards.append(card)

  def shuffle(self):
    random.shuffle(self.cards)

  def sort(self, by_suit = True):
    if by_suit:
      self.cards.sort(key=attrgetter('suit', 'rank'))
    else:
      self.cards.sort(key=attrgetter('rank', 'suit'))

  def move_cards(self, hand, num):
    for i in range(num):
      hand.add_card(self.pop_card())
  
  def deal_hands(self, no_hands, no_cards_per_hand):
    hands = []
    for i in range(no_hands):
      hand = Hand("Hand " + str(i))
      hands.append(hand)
      self.move_cards(hand, no_cards_per_hand)
    return hands
  
class Hand(Deck):
  """Represents a hand of playing cards"""

  def __init__(self, label=''):
    self.cards = []
    self.label = label 

if __name__ == "__main__":
  deck = Deck()
  deck.shuffle()
  player_hands = deck.deal_hands(4, 12)
  for player in player_hands:
    print("Player {} has:".format(player.label))
    player.sort(False)
    print(player)
