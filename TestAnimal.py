import unittest
import zoolandia

class TestAnimal(unittest.TestCase):

  @classmethod
  def setUpClass(self):
    pass

  def test_animal_creation(self):
    bob = zoolandia.Betta("orange", "Bob")
    self.assertEqual(bob.species.color, "orange")
    self.assertEqual(bob.name, "Bob")
    self.assertIsInstance(bob, zoolandia.Animal)
    self.assertIsInstance(bob.species, zoolandia.Species)
    self.assertIsInstance(bob.species, zoolandia.BettaTrifasciata)


class TestSpecies(unittest.TestCase):

  def test_common_name_empty_string_default(self):
    species = zoolandia.Species()
    self.assertEqual(species.common_name, "")

  def test_georegion_empty_string_default(self):
    species = zoolandia.Species()
    self.assertEqual(species.geo_region, "")

if __name__ == '__main__':
    unittest.main()

