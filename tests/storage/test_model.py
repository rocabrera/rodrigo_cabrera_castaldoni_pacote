import unittest
from unittest.mock import MagicMock, patch
from src.rodrigo_ml_communication.storage import InMemoryModelStorage, FileSystemModelStorage


class TestModelStorage(unittest.TestCase):
	def setUp(self):
		mock = MagicMock()
		mock.open.__enter__.return_value = True
		self.model_path = mock
		self.model = 'dummy_model'

	def test_in_memory_model_storage(self):
		storage = InMemoryModelStorage()

		self.assertTrue(storage.add(self.model_path, self.model))

		retrieved_model = storage.get(self.model_path)
		self.assertEqual(retrieved_model, self.model)

		self.assertTrue(storage.delete(self.model_path))

		retrieved_model = storage.get(self.model_path)
		self.assertIsNone(retrieved_model)

if __name__ == '__main__':
	unittest.main()
