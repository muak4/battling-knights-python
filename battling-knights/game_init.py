from enum import Enum


class KStatus(Enum):
    LIVE = 1
    DEAD = 0
    DROWNED = -1


class Knight:
    def __init__(self, name, symbol, position, k_status, item, a_score, d_score):
        self.name = name
        self.symbol = symbol
        self.position = position
        self.k_status = k_status
        self.item = item
        self.a_score = a_score
        self.d_score = d_score


class Item:
    def __init__(self, name, symbol, position, p_value, holder, a_stat, d_stat):
        self.name = name
        self.symbol = symbol
        self.position = position
        self.p_value = p_value
        self.holder = holder
        self.a_stat = a_stat
        self.d_stat = d_stat


items = []
knights = []


def app_init():
    red_knight = Knight("Red", 'R', [0, 0], KStatus.LIVE, None, 1, 1)
    blue_knight = Knight("Blue", 'B', [7, 0], KStatus.LIVE, None, 1, 1)
    green_knight = Knight("Green", 'G', [7, 7], KStatus.LIVE, None, 1, 1)
    yellow_knight = Knight("Yellow", 'Y', [0, 7], KStatus.LIVE, None, 1, 1)

    axe = Item("Axe", 'A', [2, 2], 4, None, 2, 0)
    dagger = Item("Dagger", 'D', [2, 5], 2, None, 1, 0)
    magic_staff = Item("Magic Staff", 'M', [5, 2], 3, None, 1, 1)
    helmet = Item("Helmet", 'H', [5, 5], 1, None, 0, 1)

    knights.append(red_knight)
    knights.append(blue_knight)
    knights.append(green_knight)
    knights.append(yellow_knight)

    items.append(axe)
    items.append(dagger)
    items.append(helmet)
    items.append(magic_staff)
