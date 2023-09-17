import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Test the User class"""

    def setUp(self):
        """Set up test cases"""
        self.user = User()

    def test_attributes(self):
        """Test that User has the correct attributes"""
        self.assertTrue(hasattr(self.user, "email"))
        self.assertTrue(hasattr(self.user, "password"))
        self.assertTrue(hasattr(self.user, "first_name"))
        self.assertTrue(hasattr(self.user, "last_name"))

    def test_types(self):
        """Test that User attributes have the correct types"""
        self.assertIsInstance(self.user.email, str)
        self.assertIsInstance(self.user.password, str)
        self.assertIsInstance(self.user.first_name, str)
        self.assertIsInstance(self.user.last_name, str)

    def test_inheritance(self):
        """Test that User inherits from BaseModel"""
        self.assertIsInstance(self.user, BaseModel)


if __name__ == "__main__":
    unittest.main()
