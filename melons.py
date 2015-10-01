"""This file should have our melon-type classes in it."""

class AbstractMelonOrder(object):
    species = None
    color = None
    imported = False
    shape = None
    seasons = []
    base_price = 5

    def __init__(self):
        raise NotImplementedError("Melon order must be of a specific type")

    def get_base_price(self):
        """Return the base price of all melons"""

        if 'mel' == 'grumpy':
            return 100
        elif 'mel' == 'happy':
            return 1
        else:
            return 5






class WatermelonOrder(AbstractMelonOrder):
    species = "Watermelon"
    color = "green"
    imported = False
    shape = 'natural'
    seasons = ['Fall', 'Summer']

    def __init__(self):
        pass

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        if qty >= 3:
            total = (qty * self.get_base_price()) * 0.75
        else:
            total = qty * self.get_base_price()

        return total



class CantaloupeOrder(AbstractMelonOrder):
    species = "Cantaloupe"
    color = "tan"
    imported = False
    shape = 'natural'
    seasons = ['Spring', 'Summer']

    def __init__(self):
        pass

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        if qty >= 5:
            total = (qty * self.get_base_price()) * 0.5
        else:
            total = qty * self.get_base_price()

        return total


class CasabaOrder(AbstractMelonOrder):
    species = "Casaba"
    color = "green"
    imported = True
    shape = 'natural'
    seasons = ['Fall', 'Summer', 'Spring', 'Winter']

    def __init__(self):
        pass

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        price_each = (self.get_base_price() + 1) * 1.5

        return qty * price_each


class SharlynOrder(AbstractMelonOrder):
    species = "Sharlyn"
    color = "tan"
    imported = True
    shape = 'natural'
    seasons = ['Summer']

    def __init__(self):
        pass

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        price_each = self.get_base_price() * 1.5

        return qty * price_each 


class SantaClausOrder(AbstractMelonOrder):
    species = "Santa Claus"
    color = "green"
    imported = True
    shape = 'natural'
    seasons = ['Winter', 'Spring']

    def __init__(self):
        pass

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        price_each = self.get_base_price() * 1.5

        return qty * price_each 



class ChristmasOrder(AbstractMelonOrder):
    species = "Christmas"
    color = "green"
    imported = False
    shape = 'natural'
    seasons = ['Winter']

    def __init__(self):
        pass

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        return qty * self.get_base_price()


class HornedmelonOrder(AbstractMelonOrder):
    species = "Horned Melon"
    color = "yellow"
    imported = True
    shape = 'natural'
    seasons = ['Summer']

    def __init__(self):
        pass

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        price_each = self.get_base_price() * 1.5

        return qty * price_each 


class XiguaOrder(AbstractMelonOrder):
    species = "Xigua"
    color = "black"
    imported = True
    shape = 'square'
    seasons = ['Summer']

    def __init__(self):
        pass

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        price_each = self.get_base_price() * 3

        return qty * price_each


class OgenOrder(AbstractMelonOrder):
    species = "Ogen"
    color = "tan"
    imported = False
    shape = 'natural'
    seasons = ['Spring', 'Summer']

    def __init__(self):
        pass

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        price_each = self.get_base_price() + 1

        return qty * price_each