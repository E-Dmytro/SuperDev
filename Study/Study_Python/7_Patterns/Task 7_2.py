"""A separate class for Item"""

class Goods:

    """Constructor function  wth price and discount"""

    def __init__(self,price,discount_strategy = None):

        """take price and discount strategy"""

        self.price = price
        self.discount_strategy = discount_strategy

    def price_after_discount(self):
        discount = self.discount_strategy(self) if self.discount_strategy else 0

        return self.price - discount

    def __str__(self):

        return f'Price: {self.price}, price after discount: {self.price_after_discount()}'
    def on_sale_discount(order):
        """function dedicated to On Sale Discount"""
        return order.price * 0.5
    def twenty_percent_discount(order):
        """function dedicated to 20% discount"""
        return order.price * 0.20

