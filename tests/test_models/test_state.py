import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Test the State class"""

    def setUp(self):
        """Set up test cases"""
        self.state = State()

    def test_attributes(self):
        """Test that State has the correct attributes"""
        self.assertTrue(hasattr(self.state, "name"))
        self.assertEqual(self.state.name, "")


if __name__ == "__main__":
    unittest.main()
