from datetime import datetime
from module_counter.exceptions_counter import MealTooBigError, InvalidItemId
from module_counter.functions_counter import calories_counter, prices_counter

class Order:
    """
    This class represents an order.

    Arguments:
        items (list): A list of item ids.
        date (datetime): The date and time of the order.

    Class attributes:
        order_counter (int): A counter for the number of orders.

    Attributes:
        order_id (str): A unique identifier for the order.
        order_accepted (bool): Whether or not the order was accepted.
        order_refused_reason (str): The reason the order was refused.
        date (datetime): The date and time of the order.
        items (list): A list of item ids.

    Properties:
        calories (int): The total calories for the order.
        price (int): The total price for the order.
    """
    order_counter = 0

    def __init__(self, items, date=None):
        Order.order_counter += 1
        self.order_id = f"order-{Order.order_counter}"
        if date is None:
            self.date = datetime.now()
        else:
            self.date = date
        self.items = items
        self._calories = None
        self._price = None

        try:
            self._calories = calories_counter(self.items)
            self._price = prices_counter(self.items)
            self.order_accepted = True
            self.order_refused_reason = None
        except (InvalidItemId, MealTooBigError) as e:
            self.order_accepted = False
            self.order_refused_reason = str(e)
            self._calories = 0
            self._price = 0
        else:
            self.order_accepted = True
            self.order_refused_reason = None

    @property
    def calories(self):
        if self._calories is None:
            self._calories = calories_counter(self.items)
        return self._calories

    @property
    def price(self):
        if self._price is None:
            self._price = prices_counter(self.items)
        return self._price
        