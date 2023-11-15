from unittest import TestCase
from module_counter.classes import Order


class OrderTestCase(TestCase):
    def test_order_id_is_increment(self):
        initial_counter = Order.counter
        order_1 = Order([])
        order_2 = Order([])

        self.assertEqual(order_1.order_id, f"order-{initial_counter}")
        self.assertEqual(order_2.order_id, f"order-{initial_counter}")