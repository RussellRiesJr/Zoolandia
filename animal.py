from species import *

class Animal :

  def __init__(self, name, species):
    self.species = species
    self.name = name

class Betta(Animal):
  def __init__(self, color, name):
    Animal.__init__(self, name, BettaTrifasciata(color))
