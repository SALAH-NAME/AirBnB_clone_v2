import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Unit tests for the BaseModel class."""

    def setUp(self):
        """Set up test cases."""
        self.model = BaseModel()

    def test_init(self):
        """Test initialization of BaseModel instance."""
        self.assertIsInstance(self.model, BaseModel)
        self.assertIsInstance(self.model.id, str)
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_init_kwargs(self):
        """Test initialization of BaseModel instance with kwargs."""
        d = {
            "id": "1234-5678-9101",
            "created_at": "2023-04-05T16:25:03.500000",
            "updated_at": "2023-04-05T16:25:03.500000"
        }
        model = BaseModel(**d)
        self.assertEqual(model.id, d["id"])
        self.assertEqual(model.created_at.isoformat(), d["created_at"])
        self.assertEqual(model.updated_at.isoformat(), d["updated_at"])

    def test_str(self):
        """Test string representation of BaseModel instance."""
        expected = "[BaseModel] ({}) {}".format(self.model.id,
                                                self.model.__dict__)
        self.assertEqual(str(self.model), expected)

    def test_save(self):
        """Test save method of BaseModel instance."""
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(old_updated_at, self.model.updated_at)

    def test_to_dict(self):
        """Test to_dict method of BaseModel instance."""
        d = self.model.to_dict()
        self.assertIsInstance(d, dict)
        self.assertEqual(d["__class__"], "BaseModel")
        self.assertEqual(d["id"], self.model.id)
        self.assertEqual(d["created_at"], self.model.created_at.isoformat())
        self.assertEqual(d["updated_at"], self.model.updated_at.isoformat())


if __name__ == "__main__":
    unittest.main()
