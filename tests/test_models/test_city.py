import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Test the City class"""

    def setUp(self):
        """Set up test cases"""
        self.city = City()

    def test_attributes(self):
        """Test that City has the correct attributes"""
        self.assertTrue(hasattr(self.city, "state_id"))
        self.assertTrue(hasattr(self.city, "name"))
        self.assertEqual(self.city.state_id, "")
        self.assertEqual(self.city.name, "")


if __name__ == "__main__":
    unittest.main()
