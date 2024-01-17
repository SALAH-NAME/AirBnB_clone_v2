"""
Defines unittests for models/engine/file_storage.py.
"""
import unittest
import models
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Test the FileStorage class"""

    def setUp(self):
        """Set up test cases"""
        self.storage = FileStorage()
        self.base_model = BaseModel()

    def tearDown(self):
        """Clean up after tests"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_all(self):
        """Test the all method"""
        # Test that all returns a dictionary
        self.assertIsInstance(self.storage.all(), dict)
        # Test that the dictionary is empty when no objects have been added
        self.assertEqual(len(self.storage.all()), 12)

    def test_new(self):
        """Test the new method"""
        # Test that new adds an object to the __objects dictionary
        self.storage.new(self.base_model)
        st = "BaseModel.{}"
        self.assertIn(st.format(self.base_model.id), self.storage.all())

    def test_save(self):
        """Test the save method"""
        # Test that save creates a file
        self.storage.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_reload(self):
        """Test the reload method"""
        # Test that reload loads objects from a file
        self.storage.new(self.base_model)
        self.storage.save()
        self.storage.reload()
        objects = self.storage.all()
        self.assertIn("BaseModel.{}".format(self.base_model.id), objects)

    def test_FileStorage_instantiation_no_args(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_instantiation_with_arg(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_FileStorage_file_path_is_private_str(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def testFileStorage_objects_is_private_dict(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_storage_initializes(self):
        self.assertEqual(type(models.storage), FileStorage)

    def test_all_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_new_with_args(self):
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def test_new_with_None(self):
        with self.assertRaises(AttributeError):
            models.storage.new(None)

    def test_save_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_reload_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.reload(None)


if __name__ == "__main__":
    unittest.main()
