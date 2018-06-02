"""This module contains a code example related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division

from chapter18 import Card, Hand, Deck

class PokerHand(Hand):
  """Represents a poker hand."""

  def suit_hist(self, collection):
    """Builds a histogram of the suits that appear in the hand.

    Stores the result in attribute suits.
    """
    self.suits = {}
    for card in collection:
      self.suits[card.suit] = self.suits.get(card.suit, 0) + 1

  def has_flush(self, collection=None):
    """Returns True if the hand has a flush, False otherwise.
      
    Note that this works correctly for hands with more than 5 cards.
    """
    if not collection:
      collection = self.cards
    self.suit_hist(collection)
    for val in self.suits.values():
      if val >= 5:
        return True
    return False

  def rank_hist(self):
    self.ranks = {}
    for card in self.cards:
      self.ranks[card.rank] = self.ranks.get(card.rank, 0) + 1

  def count_same_rank(self, no_cards_in_same_rank=2):
    """Return the number of pairs/three of a kind in hands"""
    counter = 0
    self.rank_hist()
    #print(">> DEBUG: histogram of rank is", self.ranks)
    for val in self.ranks.values():
      if val == no_cards_in_same_rank:
        counter+=1
    return counter

  def has_one_pair(self):
    return self.count_same_rank() == 1

  def has_two_pairs(self):
    return self.count_same_rank() == 2

  def has_three_of_a_kind(self):
    return self.count_same_rank(3) == 1

  def has_four_of_a_kind(self):
    return self.count_same_rank(4) == 1

  def collect_sequence(self):
    self.sort(False)
    res = []
    for i in range(len(self.cards) - 1):
      current_card = self.cards[i]
      next_card = self.cards[i + 1]
      diff = next_card.rank - current_card.rank
      if diff == 1 or diff == 0:
        res.append(self.cards[i])
        if i == (len(self.cards) - 2):
          res.append(self.cards[i + 1])
        self.print_card_list(res)
    return res

  def print_card_list(self, collection):
    print("DEBUG, card list is now:", end = " ")
    for card in collection:
      print(str(card), end=', ')
    print()

  def has_straight(self):
    tmp = self.collect_sequence()
    print(">> DEBUG - before set")
    self.print_card_list(tmp)
    tmp = set(tmp)
    print(">> DEBUG - after set:")
    self.print_card_list(tmp)
    return len(tmp) >= 5
      
  def has_full_house(self):
    return self.has_three_of_a_kind and self.has_one_pair()
    
  def has_straight_flush(self):
    tmp = self.collect_sequence()
    if not self.has_straight():
      return False
   
    is_flush = False
    tmp_suit = None
    for card in tmp:
      if not tmp_suit:
        tmp_suit = card.suit
      else:
        if tmp_suit != card.suit:
          return False
    return True

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

  print("Hand One has flush? >>", hand1.has_flush())
  print("Hand One has straight? >>", hand1.has_straight())
  print("Hand One has one pair? >>", hand1.has_one_pair())
  print("Hand One has two pairs? >>", hand1.has_two_pairs())
  print("Hand One has straight flush? >>", hand1.has_straight_flush())

  hand2 = PokerHand()
  hand2.add_card(three_of_clubs)
  hand2.add_card(three_of_hearts)
  hand2.add_card(three_of_diamonds)
  hand2.add_card(four_of_clubs)
  hand2.add_card(four_of_spades)

  print("Hand Two has three of a kind? >>", hand2.has_three_of_a_kind())
  print("Hand Two has full house? >>", hand2.has_full_house()) 
  
  hand2.add_card(three_of_spades)
  
  print("Hand Two has four of kinds? >>", hand2.has_four_of_a_kind())
  
