import unittest
from main import check_cycle

class TestCheckCycle(unittest.TestCase):

    def test_graph_without_cycle(self):
        graph = [[], [], [], [], [], [], [], [], [], [], [], []]
        visited = [False] * 12
        parent = -1
        self.assertFalse(check_cycle(graph, 0, visited, parent))

    def test_graph_with_cycle(self):
        graph = [[1], [2, 3], [3], [4], [5], [3], [7, 8], [9], [10, 11], [11], [6], [1]]
        visited = [False] * 12
        parent = -1
        self.assertTrue(check_cycle(graph, 0, visited, parent))

    def test_graph_with_self_loop(self):
        graph = [[1], [2], [3], [4], [5], [5], [6], [7], [8], [9], [10], [11]]
        visited = [False] * 12
        parent = -1
        self.assertTrue(check_cycle(graph, 0, visited, parent))

if __name__ == "__main__":
    unittest.main()