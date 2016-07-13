import unittest
import zoolandia

class TestHabitat(unittest.TestCase):

  def test_name_empty_string_default(self):
    habitat = zoolandia.Habitat()
    self.assertEqual(habitat.name, "")

  def test_members_set_default(self):
    habitat = zoolandia.Habitat()
    self.assertIsInstance(habitat.members, set)

  def test_add_member(self):
    aquarium = zoolandia.Aquarium("freshwater")
    bob = zoolandia.Betta("orange", "Bob")
    james = zoolandia.Betta("blue", "James")

    aquarium.add_member(bob)
    self.assertIn(bob, aquarium.members)

    aquarium.add_member(james)
    self.assertIn(bob, aquarium.members)
    self.assertIn(james, aquarium.members)

  def test_remove_members(self):
    aquarium = zoolandia.Aquarium("freshwater")
    james = zoolandia.Betta("blue", "James")
    aquarium.add_member(james)
    aquarium.remove_member(james)
    self.assertNotIn(james, aquarium.members)


if __name__ == '__main__':
    unittest.main()

