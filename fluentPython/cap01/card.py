from collections import namedtuple
from random import choice


Card = namedtuple('Card', ['rank', 'suit'])



class FrenchCard():
    ranks = [str(i) for i in range(2, 11)] + list('AJQK')
    suits = 'spades diamonds clubs hearts'.split()

    
    def __init__(self):
        self._cards = [ Card(rank, suit) for rank in self.ranks for suit in self.suits]


    def __len__(self):
        return len(self._cards)


    def __getitem__(self, pos):
        return self._cards[pos]




if __name__ == '__main__':
    
    fc = FrenchCard()

    print(len(fc))
    print(choice(fc))
    print(choice(fc))
    print(choice(fc))
