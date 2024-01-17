import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test the Amenity class"""

    def setUp(self):
        """Set up test cases"""
        self.amenity = Amenity()

    def test_attributes(self):
        """Test that Amenity has the correct attributes"""
        self.assertTrue(hasattr(self.amenity, "name"))
        self.assertEqual(self.amenity.name, "")


if __name__ == "__main__":
    unittest.main()
