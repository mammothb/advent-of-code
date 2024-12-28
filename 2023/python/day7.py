import collections
from dataclasses import dataclass, field
from enum import IntEnum, auto

from aoc_helper.io import IoOutputType, read_data


class HandType(IntEnum):
    HIGH_CARD = auto()
    PAIR = auto()
    TWO_PAIR = auto()
    THREE_OF_A_KIND = auto()
    FULL_HOUSE = auto()
    FOUR_OF_A_KIND = auto()
    FIVE_OF_A_KIND = auto()


CARD_TO_VALUE = {card: value for value, card in enumerate("23456789TJQKA")}
CARD_TO_VALUE2 = {card: value for value, card in enumerate("J23456789TQKA")}


@dataclass
class Hand:
    cards: str
    bid: int
    use_joker: bool = False
    type: HandType = field(init=False)
    value_map: dict[str, int] = field(init=False)

    def __post_init__(self):
        counter = collections.Counter(self.cards)
        if self.use_joker and len(counter) > 1 and "J" in counter:
            num_joker = counter["J"]
            counts = sorted([v for k, v in counter.items() if k != "J"], reverse=True)
            counts[0] += num_joker
        else:
            counts = sorted(list(counter.values()), reverse=True)

        if counts[0] == 5:
            self.type = HandType.FIVE_OF_A_KIND
        elif counts[0] == 4:
            self.type = HandType.FOUR_OF_A_KIND
        elif counts[0] == 3 and counts[1] == 2:
            self.type = HandType.FULL_HOUSE
        elif counts[0] == 3:
            self.type = HandType.THREE_OF_A_KIND
        elif counts[0] == 2 and counts[1] == 2:
            self.type = HandType.TWO_PAIR
        elif counts[0] == 2:
            self.type = HandType.PAIR
        else:
            self.type = HandType.HIGH_CARD

        self.value_map = CARD_TO_VALUE2 if self.use_joker else CARD_TO_VALUE

    def __lt__(self, other: "Hand") -> bool:
        if self.type != other.type:
            return self.type < other.type
        n = min(len(self.cards), len(other.cards))
        for i in range(n):
            if self.value_map[self.cards[i]] == self.value_map[other.cards[i]]:
                continue
            return self.value_map[self.cards[i]] < self.value_map[other.cards[i]]
        return False


def main():
    data = read_data("day7.txt", IoOutputType.LINE)
    hands: list[Hand] = []
    for line in data:
        cards, bid = line.rstrip().split()
        hands.append(Hand(cards, int(bid)))
    hands = sorted(hands)
    print(sum(rank * hand.bid for rank, hand in enumerate(hands, 1)))

    hands2: list[Hand] = []
    for line in data:
        cards, bid = line.rstrip().split()
        hands2.append(Hand(cards, int(bid), use_joker=True))
    hands2 = sorted(hands2)
    print(sum(rank * hand.bid for rank, hand in enumerate(hands2, 1)))


if __name__ == "__main__":
    main()
