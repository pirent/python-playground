"""This module contains a code example related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division

from chapter18 import Card, Hand, Deck

from collections import defaultdict

class Hist(dict):
  def __init__(self, seq=[]):
    for x in seq:
      self.count(x)

  def count(self, x, f=1):
    self[x] = self.get(x, 0) + f
    if self[x] == 0:
      del self[x]

class PokerHand(Hand):
  """Represents a poker hand."""

  all_labels = ["straight_flush", "four_of_a_kind", "full_house", "flush", "straight", "three_of_a_kind", "two_pairs", "one_pair"]
  
  def make_histogram(self):
    """compute the histogram for suit and rank"""
    self.suits = Hist()
    self.ranks = Hist()

    for card in self.cards:
      self.suits.count(card.suit)
      self.ranks.count(card.rank)

    self.sets = list(self.ranks.values())
    self.sets.sort(reverse=True)

  def check_set(self, *t):
    """Check whether self.sets contains sets that are as big as the requirement ti
    """
    for need, have in zip(t, self.sets):
      if need > have:
        return False
    return True
 
  def has_one_pair(self):
    return self.check_set(2)

  def has_two_pairs(self):
    return self.check_set(2, 2)

  def has_three_of_a_kind(self):
    return self.check_set(3)

  def has_four_of_a_kind(self):
    return self.check_set(4)

  def has_full_house(self):
    return self.check_set(3, 2)

  def has_flush(self):
    for val in self.suits.values():
      if val >= 5:
        return True
    return False
    
  def has_straight(self):
    ranks = self.ranks.copy()
    ranks[14] = self.ranks.get(1, 0)

    return self.in_a_row(ranks, 5)

  def print_cards_seq(self, seq):
    res = []
    for card in seq:
      res.add(str(card))
    print(", ".join(res))

  def in_a_row(self, ranks, n=5):
    count = 0
    for i in range(1, 15):
      if ranks.get(i, 0):
        count += 1
        if count == n:
          return True
      else:
        count = 0
    return False

  def has_straight_flush(self):
    sub_hands = defaultdict(PokerHand)
    for c in self.cards:
      sub_hands[c.suit].add_card(c)

    for hand in sub_hands.values():
      if len(hand.cards) < 5:
        continue
      hand.make_histogram()
      if hand.has_straight():
        return True
    return False

  def classify(self):
    self.make_histogram()
    self.my_labels = set()
    for label in PokerHand.all_labels:
      f = getattr(self, "has_" + label)
      if f():
        self.my_labels.add(label)

if __name__ == '__main__':
  ## make a deck
  #deck = Deck()
  #deck.shuffle()

  ## deal the cards and classify the hands
  #for i in range(7):
  #  hand = PokerHand()
  #  deck.move_cards(hand, 7)
  #  hand.sort()
  #  print(hand)
  #  print(hand.has_flush())
  #  print('')

  print(">>> SMOKE TEST <<<")
  two_of_clubs = Card(0, 2)
  three_of_clubs = Card(0, 3)
  four_of_clubs = Card(0, 4)
  five_of_clubs = Card(0, 5)
  six_of_clubs = Card(0, 6)
  
  three_of_hearts = Card(2, 3)
  three_of_diamonds = Card(1, 3)
  three_of_spades = Card(3, 3)
  four_of_spades = Card(3, 4)

  hand1 = PokerHand()
  hand1.add_card(two_of_clubs)
  hand1.add_card(three_of_clubs)
  hand1.add_card(four_of_clubs)
  hand1.add_card(five_of_clubs)
  hand1.add_card(six_of_clubs)
  hand1.add_card(three_of_hearts)
  hand1.add_card(four_of_spades)

  hand1.classify()

  print("Hand One has flush? >>", "flush" in hand1.my_labels)
  print("Hand One has straight? >>", "straight" in hand1.my_labels)
  print("Hand One has one pair? >>", "one_pair" in hand1.my_labels)
  print("Hand One has two pairs? >>", "two_pair" in hand1.my_labels)
  print("Hand One has straight flush? >>", "straight_flush" in hand1.my_labels)

  hand2 = PokerHand()
  hand2.add_card(three_of_clubs)
  hand2.add_card(three_of_hearts)
  hand2.add_card(three_of_diamonds)
  hand2.add_card(four_of_clubs)
  hand2.add_card(four_of_spades)
  hand2.add_card(three_of_spades)

  hand2.classify()
  print("Hand Two has three of a kind? >>", "three_of_a_kind" in hand2.my_labels)
  print("Hand Two has full house? >>", "full_house" in hand2.my_labels) 
  
  
  print("Hand Two has four of a kind? >>", "four_of_a_kind" in hand2.my_labels)
  
