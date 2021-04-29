# -*- coding: utf-8 -*-
"""Poo_v1.ipynb

Automatically generated by Colaboratory.

"""

# Abstract class konkretna implementacja przez subclass i sama klasa abstracyjna nie moze miec instancji
from abc import ABC, abstractmethod

class GraphicShape(ABC):

  def __init__(self):
    pass

  @abstractmethod
  def calcArea(self):
    pass


class Circle(GraphicShape):
  def __init__(self, radius):
    self.radius = radius
    
  def calcArea(self):
    return 3.14 * (self.radius ** 2)


class Square(GraphicShape):
  def __init__(self, side):
    self.side = side

  def calcArea(self):
    return self.side * self.side

#g = GraphicShape()

c = Circle(10)
print(c.calcArea())
