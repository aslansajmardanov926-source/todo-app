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


class CompleteDeleteTests(unittest.TestCase):
    def test_complete_marks_done(self):
        todo = TodoList()
        todo.add_task("A")
        self.assertTrue(todo.complete_task(1).done)

    def test_delete_removes_task(self):
        todo = TodoList()
        todo.add_task("A")
        todo.delete_task(1)
        self.assertEqual(todo.list_tasks(), [])

    def test_unknown_id_raises(self):
        with self.assertRaises(LookupError):
            TodoList().complete_task(99)


if __name__ == "__main__":
    unittest.main()
