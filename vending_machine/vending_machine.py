#!/bin/python3

import os


class VendingMachine:

    def __init__(self, num_items_input, item_price):
        self.num_items = num_items_input
        self.item_price = item_price

    def has_money(self, req_items, money):
        input_solicitation = self.item_price * req_items
        if money >= input_solicitation:
            return True
        else:
            return False

    def has_items(self, req_items):
        if self.num_items >= req_items:
            return True
        else:
            return False

    def buy(self, req_items, money):
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
