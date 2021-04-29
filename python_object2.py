# -*- coding: utf-8 -*-
"""Python_Object2.ipynb

Automatically generated by Colaboratory.

"""

class Book:
  def __init__(self, title, author, pages, price): # musza byc ustawione
    self.title = title
    self.author = author
    self.pages = pages
    self.price = price
    self.__secret = "this is an unavailable attribute"

  def getprice(self):
    if hasattr(self, "_discount"): #jezeli jest ustawiony atrybut _discount
      return self.price - (self.price * self._discount)
    else:
      return self.price

  def setdiscount(self, amount): # atrybut ustawiony i nie musi byc w init
    self._discount = amount

b1 = Book('Problem 3 cial', 'cixin liu', '333', 39.99)
b2 = Book('wspomnienie o przeszlosci', 'cixin liu', '444', 60.00)

print(b2.getprice())
b2.setdiscount(0.25)
print(b2.getprice())

#name mangling
#print(b2.__secret)
#vs.
print(b2._Book__secret)