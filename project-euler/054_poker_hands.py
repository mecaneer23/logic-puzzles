#!/usr/bin/env python3

# https://projecteuler.net/problem=54

from collections import Counter


class Card:
    """Representation of a playing card"""

    suits = "HDSC"
    values = "23456789TJQKA"

    def __init__(self, card_str: str) -> None:
        if (
            len(card_str) != 2
            or card_str[0] not in Card.values
            or card_str[1] not in Card.suits
        ):
            raise ValueError(f"Invalid card: {card_str}")
        self._value, self._suit = card_str

    def get_value(self) -> str:
        """Getter for value"""
        return self._value

    def get_suit(self) -> str:
        """Getter for suit"""
        return self._suit


class Hand:
    """5 cards in a Poker hand"""

    def __init__(self, cards: list[str]) -> None:
        if len(cards) != 5:
            raise ValueError(f"Wrong amount of cards in hand: {len(cards)}")
        self._cards = [Card(card) for card in cards]
        self._suits = [card.get_suit() for card in self._cards]
        self._values = [card.get_value() for card in self._cards]
        self._values_counter = Counter(self._values).values()
        table = {
            "T": 10,
            "J": 11,
            "Q": 12,
            "K": 13,
            "A": 14,
        }
        self._sortable_values: list[int] = []
        for value in self._values:
            if value.isdigit():
                self._sortable_values.append(int(value))
                continue
            self._sortable_values.append(table[value])

    def is_flush(self) -> bool:
        """Whether all of the cards in the hand are of the same suit"""
        return set(Counter(self._suits).values()) == {5}

    def is_royal_flush(self) -> bool:
        """Whether the cards form a royal flush"""
        if not self.is_flush():
            return False
        for value in "TJQKA":
            if value not in self._values:
                return False
        return True

    def is_straight_flush(self) -> bool:
        """Whether the cards are all consecutive and the same suit"""
        return self.is_straight() and self.is_flush()

    def is_four_of_a_kind(self) -> bool:
        """Whether the hand contains >= four cards of the same value"""
        return max(self._values_counter) <= 4

    def is_full_house(self) -> bool:
        """Whether the hand is comprised of 3 of a kind and a pair"""
        return set(self._values_counter) == {3, 2}

    def is_straight(self) -> bool:
        """Whether all cards are consecutive"""
        return sorted(self._sortable_values) == list(
            range(min(self._sortable_values), max(self._sortable_values) + 1)
        )

    def is_three_of_a_kind(self) -> bool:
        """Whether the hand contains >= three cards of the same value"""
        return max(self._values_counter) <= 3

    def is_two_pairs(self) -> bool:
        """Whether the hand contains two pairs"""
        return set(self._values_counter) in [{2, 1}, {3, 2}]

    def is_one_pair(self) -> bool:
        """Whether the hand contains one pair"""
        return 2 in set(self._values_counter)

    def get_high_card_value(self) -> int:
        """Return the value of the highest card"""
        return max(self._sortable_values)

    # def get_max_ranking(self) -> int:
    #     """
    #     Return a number 1-1000 which determines the
    #     likelyhood of a hand to win
    #     """
    #     if self.is_royal_flush():
    #         return 1000
    #     if self.is_straight_flush():
    #         return 900
    #     if self.is_four_of_a_kind():
    #         return 800
    #     if self.is_full_house():
    #         return 700
    #     if self.is_flush():
    #         return 600
    #     if self.is_straight():
    #         return 500
    #     if self.is_three_of_a_kind():
    #         return 400
    #     if self.is_two_pairs():
    #         return 300
    #     if self.is_one_pair():
    #         return 200
    #     return 1


# def will_first_hand_win(first_hand: Hand, second_hand: Hand) -> bool:
#     """Return whether the first hand will win over the second hand"""
#     h1 = first_hand.get_max_ranking()
#     h2 = second_hand.get_max_ranking()
#     if h1 == h2 == 1:
#         return first_hand.get_high_card_value() > second_hand.get_high_card_value()
#     if h1 == h2:
#         print(h1)
#         raise ValueError("Equal hands")
#     return h1 > h2

# def compare_hands_from_file(filename: str) -> int:
#     """Return the amount of hands player 1 wins over player 2"""
#     with open(filename, "r", encoding="utf-8") as file:
        
