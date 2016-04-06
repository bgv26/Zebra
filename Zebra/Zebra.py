from itertools import permutations


class Number:
    One, Two, Three, Four, Five = range(5)
    _values = 'One, Two, Three, Four, Five'.split(', ')

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return Number._values[self.value]


class Color:
    Red, Green, Blue, Ivory, Yellow = range(5)
    _values = 'Red, Green, Blue, Ivory, Yellow'.split(', ')

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return Color._values[self.value]


class Drink:
    Milk, Coffee, Water, OrangeJuice, Tea = range(5)
    _values = 'Milk, Coffee, Water, Orange Juice, Tea'.split(', ')

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return Drink._values[self.value]


class Smoke:
    Parliament, LuckyStrike, Kools, OldGold, Chesterfield = range(5)
    _values = 'Parliament, Lucky Strike, Kools, Old Gold, Chesterfield'.split(', ')

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return Smoke._values[self.value]


class Pet:
    Dog, Fox, Zebra, Horse, Snails = range(5)
    _values = 'Dog, Fox, Zebra, Horse, Snails'.split(', ')

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return Pet._values[self.value]


class Nation:
    Englishman, Spaniard, Ukrainian, Norwegian, Japanese = range(5)
    _values = 'Englishman, Spaniard, Ukrainian, Norwegian, Japanese'.split(', ')

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return Nation._values[self.value]


def cond_one(perms):
    res = []
    for number in perms:
        # The Norwegian lives in the first house.
        if number[Nation.Norwegian] == Number.One:
            res.append(number)

    return res


def cond_two(perms):
    res = []
    for color in perms:
        # The Englishman lives in the red house.
        if color[Nation.Englishman] == Color.Red:
            res.append(color)

    return res


def cond_three(perms):
    res = []
    for drink in perms:
        # The Ukrainian drinks tea.
        if drink[Nation.Ukrainian] == Drink.Tea:
            res.append(drink)

    return res


def cond_four(perms):
    res = []
    for smoke in perms:
        # The Japanese smokes Parliaments.
        if smoke[Nation.Japanese] == Smoke.Parliament:
            res.append(smoke)

    return res


def cond_five(perms):
    res = []
    for pet in perms:
        # The Spaniard owns the dog.
        if pet[Nation.Spaniard] == Pet.Dog:
            res.append(pet)

    return res


def is_possible(number, color, drink, smoke, pet):
    # # The Norwegian lives in the first house.
    # if number and number[Nation.Norwegian] != Number.One:
    #     return False
    # # The Englishman lives in the red house.
    # if color and color[Nation.Englishman] != Color.Red:
    #     return False
    # # The Ukrainian drinks tea.
    # if drink and drink[Nation.Ukrainian] != Drink.Tea:
    #     return False
    # # The Japanese smokes Parliaments.
    # if smoke and smoke[Nation.Japanese] != Smoke.Parliament:
    #     return False
    # # The Spaniard owns the dog.
    # if pet and pet[Nation.Spaniard] != Pet.Dog:
    #     return False

    # if not number or not color or not drink or not smoke or not pet:
    #     return True

    for i in xrange(5):
        # Coffee is drunk in the green house.
        if color[i] == Color.Green and drink[i] != Drink.Coffee:
            return False
        # The Old Gold smoker owns snails.
        if smoke[i] == Smoke.OldGold and pet[i] != Pet.Snails:
            return False
        # Kools are smoked in the yellow house.
        if color[i] == Color.Yellow and smoke[i] != Smoke.Kools:
            return False
        # Milk is drunk in the middle house.
        if number[i] == Number.Three and drink[i] != Drink.Milk:
            return False
        # The Lucky Strike smoker drinks orange juice.
        if smoke[i] == Smoke.LuckyStrike and drink[i] != Drink.OrangeJuice:
            return False
        # The Norwegian lives next to the blue house.
        if color[i] == Color.Blue and number[i] != Number.Two:
            return False

        for j in xrange(5):
            # The green house is immediately to the right of the ivory house.
            if (color[i] == Color.Green and
                        color[j] == Color.Ivory and
                            number[j] - number[i] != 1):
                return False

            diff = abs(number[i] - number[j])
            # The man who smokes Chesterfields lives in the house next to the man with the fox.
            if smoke[i] == Smoke.Chesterfield and pet[j] == Pet.Fox and diff != 1:
                return False
                # Kools are smoked in the house next to the house where the horse is kept.
            if pet[i] == Pet.Horse and smoke[j] == Smoke.Kools and diff != 1:
                return False

    return True


def show_row(t, data):
    print "%6s: %18s%18s%18s%18s%18s" % (
        t.__name__, t(data[0]),
        t(data[1]), t(data[2]),
        t(data[3]), t(data[4]))


def main():
    perms = list(permutations(range(5)))

    perms_one = cond_one(perms)
    perms_two = cond_two(perms)
    perms_three = cond_three(perms)
    perms_four = cond_four(perms)
    perms_five = cond_five(perms)

    # print len(perms_one)

    count = 0

    for number in perms_one:
        # if is_possible(number, None, None, None, None):
            for color in perms_two:
                # if is_possible(number, color, None, None, None):
                    for drink in perms_three:
                        # if is_possible(number, color, drink, None, None):
                            for smoke in perms_four:
                                # if is_possible(number, color, drink, smoke, None):
                                    for pet in perms_five:
                                        count += 1
                                        if is_possible(number, color, drink, smoke, pet):
                                            print "Found a solution:"
                                            show_row(Nation, range(5))
                                            show_row(Number, number)
                                            show_row(Color, color)
                                            show_row(Drink, drink)
                                            show_row(Smoke, smoke)
                                            show_row(Pet, pet)
                                            print

    print count #39813120
                #7962624

main()
