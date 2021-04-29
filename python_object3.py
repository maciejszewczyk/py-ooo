# -*- coding: utf-8 -*-
"""Python_Object3.ipynb

Automatically generated by Colaboratory.
"""

class Book:
  def __init__(self, title):
    self.title = title
   
class Newspaper:
  def __init__(self, name):
    self.name = name


b1 = Book("The Book title 1")
b2 = Book("The Book title 2")

n1 = Newspaper("The Newspaper 1")
n2 = Newspaper("The Newspaper 2")

print(isinstance(b1, Book))
print(isinstance(n1, Newspaper))
print(isinstance(n1, Book))
print(isinstance(b1, object))