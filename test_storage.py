import tempfile
import unittest
from pathlib import Path

from storage import load_tasks, save_tasks


class StorageTests(unittest.TestCase):
    def test_roundtrip(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "tasks.json"
            data = [{"id": 1, "title": "Купить молоко", "done": False}]
            save_tasks(path, data)
            self.assertEqual(load_tasks(path), data)

    def test_missing_file_gives_empty_list(self):
        self.assertEqual(load_tasks("no-such-file.json"), [])


if __name__ == "__main__":
    unittest.main()
