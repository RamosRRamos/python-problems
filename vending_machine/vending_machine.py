#!/bin/python3

import os


class VendingMachine:
    """
        A class that represents a vending machine. It has methods to check
        if there is enough money and items to buy, and a buy method that
        subtracts the requested items from the machine's available items
        and prints out the remaining number of items. It also raises a
        ValueError if there are not enough items or not enough money.

        :param num_items_input: An integer representing the initial number
        of items in the machine.
        :param item_price: A float representing the price of each
        item in the machine.
        """

    def __init__(self, num_items_input, item_price):
        """

        :param num_items_input:
        :param item_price:

        """
        self.num_items = num_items_input
        self.item_price = item_price

    def has_money(self, req_items, money):
        """
        This is a method called has_money that belongs to a class,
        as indicated by the presence of the self parameter.
         It takes two arguments: req_items
         (an integer representing the number of items requested)
         and money (a float representing the amount of money available).
         The method calculates the required amount of money by multiplying
         the item price (presumably an instance variable of the class)
         by the number of requested items, and then checks if the available
         money is greater than or equal to this amount.
         If it is, the method returns True, indicating that the transaction
         can proceed. Otherwise, it returns False, indicating that the
         transaction should be cancelled due to insufficient funds.

         :param req_items: An integer representing the number of items requested.
        :param money: A float representing the amount of money available.
        :return: True if there is enough money, False otherwise.

        """
        input_solicitation = self.item_price * req_items
        if money >= input_solicitation:
            return True
        else:
            return False

    def has_items(self, req_items):
        """This is a method called has_items which takes one argument req_items.
        It checks if the num_items attribute of self (which is presumably
        an instance of some class) is greater than or equal to req_items.
        If it is, the method returns True, and False otherwise."""
        if self.num_items >= req_items:
            return True
        else:
            return False

    def buy(self, req_items, money):
        """
        This is a method called "buy" that belongs to a class.
        It takes two parameters, "req_items" and "money".
        The method first checks if there is enough money inserted by calling
        another method "has_money". If there is enough money, it then checks
        if there are enough items left in the machine by calling another method
        "has_items". If there are enough items, it subtracts the requested
        items and prints out the remaining number of items. If there are not
        enough items, it raises a ValueError with the message "Not enough items
        in the machine". If there is not enough money, it raises a ValueError
        with the message "Not enough coins".

        :param req_items: An integer representing the number of items requested.
        :param money: A float representing the amount of money inserted.
        :return:
        """
        if self.has_money(req_items, money):
            if self.has_items(req_items):
                self.num_items = self.num_items - req_items
                print(self.num_items)
            else:
                raise ValueError('Not enough items in the machine')
        else:
            raise ValueError('Not enough coins')


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    num_items, item_coins = map(int, input().split())
    machine = VendingMachine(num_items, item_coins)

    n = int(input())
    for _ in range(n):
        num_items, num_coins = map(int, input().split())
        try:
            change = machine.buy(num_items, num_coins)
            fptr.write(str(change) + "\n")
        except ValueError as e:
            fptr.write(str(e) + "\n")

    fptr.close()
