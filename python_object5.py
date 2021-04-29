# -*- coding: utf-8 -*-
"""Python_Object5.ipynb

Automatically generated by Colaboratory.

"""

class Publication: #base class for Book i 
  def __init__(self, title, price):
    self.title = title
    self.price = price


class Periodical(Publication): #base class for Magazine & Newspaper
  def __init__(self, title, price, publisher, period):
    super().__init__(title, price)
    self.publisher = publisher
    self.period = period


class Book(Publication):
  def __init__(self, title, author, pages, price):
    super().__init__(title, price)
    self.author = author
    self.pages = pages


class Magazine(Periodical):
  def __init__(self, title, publisher, price, period):
    super().__init__(title, publisher, price, period)


class Newspaper(Periodical):
  def __init__(self, title, publisher, price, period):
    super().__init__(title, publisher, price, period)


b1 = Book("Problem 3 cial", "Cixin Liu", 444, 49.99)
m1 = Magazine("Polityka", "Dzienniekarze", 5.00, "weekly")

print(b1.title)
print(m1.period)
