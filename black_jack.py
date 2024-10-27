"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.  See below for values.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    if card in ["J", "Q", "K"]:
        return 10
    elif card == "A":
        return 1
    else:
        return int(card)


def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt in hand.  See below for values.
    :return: str or tuple - resulting Tuple contains both cards if they are of equal value.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    value_cardone = value_of_card(card_one)
    value_cardtwo = value_of_card(card_two)
    
    if value_cardone > value_cardtwo:
        return card_one
    elif value_cardtwo > value_cardone:
        return card_two
    else:
        return card_one, card_two
    


def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for the ace card.

    :param card_one, card_two: str - cards dealt.
    :return: int - either 1 or 11 value of the Ace, depending on other card.
    """
    # Determine the value of the non-Ace card
    if card_one == 'A':
        other_card_value = value_of_card(card_two)
    elif card_two == 'A':
        other_card_value = value_of_card(card_one)
    else:
        return 1  # Edge case; this function should only be called if there's an Ace

    # Return 1 if adding 11 would exceed 21, otherwise return 11
    return 1 if other_card_value + 11 > 21 else 11
    
print(value_of_ace('2', 'A'))

def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: bool - is the hand is a blackjack (two cards worth 21).

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
    if card_one == "A" and value_of_card(card_two) == 10:
        return True       
    elif card_two == "A" and value_of_card(card_one) == 10:
        return True
    else:
        return False
print(is_blackjack('10', '9'))

def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards dealt.
    :return: bool - can the hand be split into two pairs? (i.e. cards are of the same value).
    """

    return value_of_card(card_one) == value_of_card(card_two)

print(can_split_pairs('Q', 'K'))

def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """
    total_value = value_of_card(card_one) + value_of_card(card_two)
    if total_value in [9, 10, 11]:
        return True
    else:
        return False
print(can_double_down('10', '2'))
