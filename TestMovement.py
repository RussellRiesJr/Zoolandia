import unittest
import zoolandia

class TestWalking(unittest.TestCase):

  def test_legs_zero_default(self):
    walking = zoolandia.Walking()
    self.assertEqual(walking.legs, 0)

  def test_walk_speed_zero_default(self):
    walking = zoolandia.Walking()
    self.assertEqual(walking.walk_speed, 0)


class TestFlying(unittest.TestCase):

  def test_wings_zero_default(self):
    flying = zoolandia.Flying()
    self.assertEqual(flying.wings, 0)

  def test_wing_span_zero_default(self):
    flying = zoolandia.Flying()
    self.assertEqual(flying.wing_span, 0)

  def test_air_speed_zero_default(self):
    flying = zoolandia.Flying()
    self.assertEqual(flying.air_speed, 0)


class TestSwimming(unittest.TestCase):

  def test_appendages(self):
    swimming = zoolandia.Swimming()
    self.assertFalse(swimming.fins, False)
    self.assertFalse(swimming.flippers, False)
    self.assertFalse(swimming.web_feet, False)

  def test_swim_speed_zero_default(self):
    swimming = zoolandia.Swimming()
    self.assertEqual(swimming.swim_speed, 0)


if __name__ == '__main__':
    unittest.main()
