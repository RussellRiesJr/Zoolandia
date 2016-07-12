import unittest
import zoolandia

class TestAnimal(unittest.TestCase):

  @classmethod
  def setUpClass(self):
    pass

  def test_name_empty_string_default(self):
    a_animal = zoolandia.Animal()
    self.assertEqual(a_animal.name, "")

  def test_species_none_default(self):
    a_animal = zoolandia.Animal()
    self.assertEqual(a_animal.species, None)

class TestSpecies(unittest.TestCase):

  def test_common_name_empty_string_default(self):
    species = zoolandia.Species()
    self.assertEqual(species.common_name, "")

  def test_georegion_empty_string_default(self):
    species = zoolandia.Species()
    self.assertEqual(species.geo_region, "")

class TestHabitat(unittest.TestCase):

  def test_name_empty_string_default(self):
    habitat = zoolandia.Habitat()
    self.assertEqual(habitat.name, "")

  def test_members_set_default(self):
    habitat = zoolandia.Habitat()
    self.assertIsInstance(habitat.members, set)


if __name__ == '__main__':
    unittest.main()
