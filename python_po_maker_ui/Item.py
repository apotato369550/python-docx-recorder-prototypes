class Item:
    def __init__(self, quantity, article, unit, unit_price):
        self.quantity = quantity
        self.article = article
        self.unit = unit
        self.unit_price = unit_price
        self.amount = quantity * unit_price
        pass