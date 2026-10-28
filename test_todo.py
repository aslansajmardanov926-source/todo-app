import unittest

from todo import TodoList


class AddListTests(unittest.TestCase):
    def test_add_task_assigns_incremental_ids(self):
        todo = TodoList()
        first = todo.add_task("Купить молоко")
        second = todo.add_task("Сделать ПР №9")
        self.assertEqual((first.id, second.id), (1, 2))

    def test_add_empty_title_raises(self):
        with self.assertRaises(ValueError):
            TodoList().add_task("   ")

    def test_list_only_open(self):
        todo = TodoList()
        todo.add_task("A")
        todo.add_task("B").done = True
        self.assertEqual([t.title for t in todo.list_tasks(only_open=True)], ["A"])


if __name__ == "__main__":
    unittest.main()
