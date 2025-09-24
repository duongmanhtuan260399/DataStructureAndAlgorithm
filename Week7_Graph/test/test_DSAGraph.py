import unittest
from Week7_Graph.DSAGraph import DSAGraph


class TestDSAGraph(unittest.TestCase):

    def test_empty_graph(self):
        g = DSAGraph()
        self.assertEqual(g.getVertexCount(), 0)
        self.assertEqual(g.getEdgeCount(), 0)
        # getAdjacent on missing vertex should raise via peek
        with self.assertRaises(ValueError):
            g.getAdjacent("X")
        # BFS/DFS return empty traversal T
        self.assertTrue(g.breadthFirstSearch().is_empty())
        self.assertTrue(g.depthFirstSearch().is_empty())

    def test_add_vertex_and_duplicate(self):
        g = DSAGraph()
        g.addVertex("A")
        self.assertTrue(g.hasVertex("A"))
        self.assertEqual(g.getVertexCount(), 1)
        with self.assertRaises(ValueError):
            g.addVertex("A")

    def test_add_edge_auto_creates_vertices_and_idempotent(self):
        g = DSAGraph()
        g.addEdge("A", "B")
        self.assertTrue(g.hasVertex("A"))
        self.assertTrue(g.hasVertex("B"))
        self.assertTrue(g.isAdjacent("A", "B"))
        self.assertTrue(g.isAdjacent("B", "A"))  # undirected by default
        self.assertEqual(g.getVertexCount(), 2)
        self.assertEqual(g.getEdgeCount(), 1)
        # Idempotent
        g.addEdge("A", "B")
        self.assertEqual(g.getEdgeCount(), 1)

    def test_no_self_loops(self):
        g = DSAGraph()
        with self.assertRaises(ValueError):
            g.addEdge("A", "A")

    def test_get_vertex_and_adjacency(self):
        g = DSAGraph()
        g.addEdge("A", "B")
        a = g.getVertex("A")
        b = g.getVertex("B")
        self.assertEqual(a.getLabel(), "A")
        self.assertEqual(b.getLabel(), "B")
        self.assertEqual(sum(1 for _ in g.getAdjacent("A")), 1)
        self.assertEqual(sum(1 for _ in g.getAdjacent("B")), 1)

    def _drain_pair_queue(self, q):
        pairs = []
        while not q.is_empty():
            v = q.dequeue()
            w = q.dequeue()
            pairs.append((v.getLabel(), w.getLabel()))
        return pairs

    def test_bfs_single_vertex(self):
        g = DSAGraph()
        g.addVertex("A")
        pairs = self._drain_pair_queue(g.breadthFirstSearch())
        self.assertEqual(pairs, [])

    def test_bfs_line_graph(self):
        g = DSAGraph()
        g.addEdge("A", "B")
        g.addEdge("B", "C")
        pairs = self._drain_pair_queue(g.breadthFirstSearch())
        # Start at A, visit B then C
        self.assertIn(("A", "B"), pairs)
        self.assertIn(("B", "C"), pairs)
        self.assertEqual(len(pairs), 2)

    def test_bfs_cycle(self):
        g = DSAGraph()
        g.addEdge("A", "B")
        g.addEdge("B", "C")
        g.addEdge("C", "A")
        pairs = self._drain_pair_queue(g.breadthFirstSearch())
        # Two edges discovered from start A: (A,B) and (A,C) in some order
        labels = set(pairs)
        self.assertTrue(("A", "B") in labels or ("A", "C") in labels)
        # Only two discovery edges because the third creates a visited neighbor
        self.assertEqual(len(pairs), 2)

    def test_bfs_disconnected_graph_starts_first_component(self):
        g = DSAGraph()
        # Component 1
        g.addEdge("A", "B")
        # Component 2
        g.addEdge("X", "Y")
        pairs = self._drain_pair_queue(g.breadthFirstSearch())
        # Traversal should start from first inserted vertex (A), staying in its component
        self.assertTrue(all(v in {"A", "B"} and w in {"A", "B"} for v, w in pairs))

    def test_dfs_single_vertex(self):
        g = DSAGraph()
        g.addVertex("A")
        pairs = self._drain_pair_queue(g.depthFirstSearch())
        self.assertEqual(pairs, [])

    def test_dfs_line_graph(self):
        g = DSAGraph()
        g.addEdge("A", "B")
        g.addEdge("B", "C")
        pairs = self._drain_pair_queue(g.depthFirstSearch())
        self.assertIn(("A", "B"), pairs)
        self.assertIn(("B", "C"), pairs)
        self.assertEqual(len(pairs), 2)

    def test_dfs_cycle(self):
        g = DSAGraph()
        g.addEdge("A", "B")
        g.addEdge("B", "C")
        g.addEdge("C", "A")
        pairs = self._drain_pair_queue(g.depthFirstSearch())
        # DFS from A will discover two edges total
        self.assertEqual(len(pairs), 2)

    def test_remove_edge_and_vertex(self):
        g = DSAGraph()
        g.addEdge("A", "B")
        g.addEdge("B", "C")
        self.assertEqual(g.getEdgeCount(), 2)
        g.removeEdge("A", "B")
        self.assertFalse(g.isAdjacent("A", "B"))
        self.assertFalse(g.isAdjacent("B", "A"))
        self.assertEqual(g.getEdgeCount(), 1)
        g.removeVertex("B")
        self.assertFalse(g.hasVertex("B"))
        self.assertEqual(g.getVertexCount(), 2)

    def test_display_methods_do_not_crash(self):
        g = DSAGraph()
        g.displayAsList()
        g.displayAsMatrix()
        g.addEdge("A", "B")
        g.displayAsList()
        g.displayAsMatrix()


if __name__ == "__main__":
    unittest.main()


