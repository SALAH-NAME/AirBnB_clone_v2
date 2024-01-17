import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Test the Review class"""

    def setUp(self):
        """Set up test cases"""
        self.review = Review()

    def test_attributes(self):
        """Test that Review has the correct attributes"""
        self.assertTrue(hasattr(self.review, "place_id"))
        self.assertTrue(hasattr(self.review, "user_id"))
        self.assertTrue(hasattr(self.review, "text"))
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")


if __name__ == "__main__":
    unittest.main()
