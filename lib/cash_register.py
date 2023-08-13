#!/usr/bin/env python3

class CashRegister:
  
  def __init__(self, discount = 0, total = 0, items = None, last_transaction = [0, 0]):
    self.discount = discount
    self.total = total
    if items == None:
      items = []
    self.items = items
    self.last_transaction = last_transaction

  @property
  def discount(self):
    return self._discount

  @discount.setter
  def discount(self, discount):
    self._discount = discount

  @property
  def total(self):
    return self._total

  @total.setter
  def total(self, total):
    self._total = total

  @property
  def items(self):
    return self._items

  @items.setter
  def items(self, items):
    self._items = items

  @property
  def last_transaction(self):
    return self._last_transaction

  @last_transaction.setter
  def last_transaction(self, last_transaction):
    self._last_transaction = last_transaction

  def add_item(self, item, price, quantity = 1):
    self.total += price * quantity
    for x in range(quantity):
      self.items.append(item)
    self.last_transaction = [price, quantity]

  def apply_discount(self):
    if self.discount == 0:
      print('There is no discount to apply.')
      return
    self.total = self.total - (self.total * self.discount / 100)
    print(f"After the discount, the total comes to ${int(self.total)}.")

  def void_last_transaction(self):
    self.total -= self.last_transaction[0] * self.last_transaction[1]
    for x in range(self.last_transaction[1]):
      self.items.pop()