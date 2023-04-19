import unittest

from vending_machine.vending_machine import VendingMachine


class VendingMachineTest(unittest.TestCase):
    """
        The first test (test_has_money) checks whether the has_money method returns the correct boolean value when
        given a certain amount of money and required items.
        The second test (test_has_items) checks whether the has_items method returns the correct boolean value
        when given a required number of items.
        The third test (test_buy) tests the buy method for three cases: buying with not enough items,
        buying with not enough money, and buying successfully. After the successful buy,
        it checks whether the num_items attribute was updated correctly.

    """

    def test_has_money(self):
        vm = VendingMachine(10, 1.50)
        self.assertTrue(vm.has_money(3, 5))
        self.assertFalse(vm.has_money(4, 5))

    def test_has_items(self):
        vm = VendingMachine(10, 1.50)
        self.assertTrue(vm.has_items(3))
        self.assertFalse(vm.has_items(11))

    def test_buy(self):
        vm = VendingMachine(10, 1.50)
        # Test buying with not enough items
        with self.assertRaises(ValueError):
            vm.buy(11, 20)
        # Test buying with not enough coins
        with self.assertRaises(ValueError):
            vm.buy(3, 3)
        # Test successful buy
        vm.buy(2, 3.50)
        self.assertEqual(vm.num_items, 8)


if __name__ == '__main__':
    unittest.main()
