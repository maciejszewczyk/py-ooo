# -*- coding: utf-8 -*-
"""composition.ipynb

"""

class Book:
  def __init__(self, title, price, author=None):
    self.title = title
    self.price = price

    self.author = author
    self.chapters = []
    
  def addchapter(self, chapter):
    self.chapters.append(chapter)

  def getbookpagecount(self):
    result = 0
    for ch in self.chapters:
      result += ch.pagecount
    return result


class Author:
  def __init__(self, fname, lname):
    self.fname = fname
    self.lname = lname

  def __str__(self):
    return f"{self.fname} {self.lname}"


class Chapter:
  def __init__(self, name, pagecount):
    self.name = name
    self.pagecount = pagecount

auth = Author("Lew", "Tolstoy")

b1 = Book("War and pEace", 55.0, auth)

b1.addchapter(Chapter("First",200))
b1.addchapter(Chapter("Second",300))
b1.addchapter(Chapter("Third",500))

print(b1.author)

print(b1.getbookpagecount())
