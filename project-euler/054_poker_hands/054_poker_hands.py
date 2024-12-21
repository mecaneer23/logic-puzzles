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

    def __str__(self) -> str:
        return self.get_value() + self.get_suit()


class Hand:
    """5 cards in a Poker hand"""

    table = {
        "T": 10,
        "J": 11,
        "Q": 12,
        "K": 13,
        "A": 14,
    }

    @staticmethod
    def to_int(card_value: str) -> int:
        """Convert a card_value string to an integer"""
        if card_value.isdigit():
            return int(card_value)
        return Hand.table[card_value]

    def __init__(self, cards: list[str]) -> None:
        if len(cards) != 5:
            raise ValueError(f"Wrong amount of cards in hand: {len(cards)}")
        self._cards = [Card(card) for card in cards]
        self._suits = [card.get_suit() for card in self._cards]
        self._values = [card.get_value() for card in self._cards]
        self._values_counter = Counter(self._values).values()
        self._sortable_values: list[int] = []
        for value in self._values:
            if value.isdigit():
                self._sortable_values.append(int(value))
                continue
            self._sortable_values.append(self.table[value])
        self._highest_in_counter = Hand.to_int(
            Counter(self._values).most_common()[0][0]
        )

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

    def get_four_of_a_kind(self) -> int:
        """
        Whether the hand contains >= four cards of the same value
        (return that value or 0)
        """
        if max(Counter(self._values).values()) >= 4:
            return self._highest_in_counter
        return 0

    def get_full_house(self) -> int:
        """
        Whether the hand is comprised of 3 of a kind and a pair
        (return the value of the 3 of a kind or 0)
        """
        if set(self._values_counter) == {3, 2}:
            return self._highest_in_counter
        return 0

    def is_straight(self) -> bool:
        """Whether all cards are consecutive"""
        return sorted(self._sortable_values) == list(
            range(min(self._sortable_values), max(self._sortable_values) + 1)
        )

    def get_three_of_a_kind(self) -> int:
        """
        Whether the hand contains >= three cards of the same value
        (return the value of the 3 of a kind or 0)
        """
        if max(self._values_counter) >= 3:
            return self._highest_in_counter
        return 0

    def get_two_pairs(self) -> int:
        """
        Whether the hand contains two pairs
        (return the sum of the values of the
        two pairs or 0)
        """
        most_common = Counter(self._values).most_common()
        counts = list(self._values_counter)
        if 2 not in counts:
            return 0
        counts.remove(2)
        if 2 in counts:
            return Hand.to_int(most_common[0][0]) + Hand.to_int(most_common[1][0])
        return 0

    def get_one_pair(self) -> int:
        """
        Whether the hand contains one pair
        (return the value of the pair or 0)
        """
        if 2 in self._values_counter:
            return self._highest_in_counter
        return 0

    def get_high_card_value(self) -> int:
        """Return the value of the highest card"""
        return max(self._sortable_values)

    def get_max_ranking(self) -> int:
        """
        Return a number 1-1000 which determines the
        likelyhood of a hand to win
        """
        if self.is_royal_flush():
            return 1000
        if self.is_straight_flush():
            return 900
        if self.get_four_of_a_kind() > 0:
            return 800 + self.get_four_of_a_kind()
        if self.get_full_house() > 0:
            return 700 + self.get_full_house()
        if self.is_flush():
            return 600
        if self.is_straight():
            return 500
        if self.get_three_of_a_kind() > 0:
            return 400 + self.get_three_of_a_kind()
        if self.get_two_pairs() > 0:
            return 300 + self.get_two_pairs()
        if self.get_one_pair() > 0:
            return 200 + self.get_one_pair()
        return 1

    def __str__(self) -> str:
        return " ".join(map(str, self._cards))


def will_first_hand_win(first_hand: Hand, second_hand: Hand) -> bool:
    """Return whether the first hand will win over the second hand"""
    h1 = first_hand.get_max_ranking()
    h2 = second_hand.get_max_ranking()
    if h1 == h2:
        return first_hand.get_high_card_value() > second_hand.get_high_card_value()
    return h1 > h2


def compare_hands_from_file(filename: str) -> int:
    """Return the amount of hands player 1 wins over player 2"""
    first_hand_wins = 0
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            cards = line.strip().split()
            if will_first_hand_win(Hand(cards[0:5]), Hand(cards[5:10])):
                first_hand_wins += 1
    return first_hand_wins


print(compare_hands_from_file("0054_poker.txt"))
