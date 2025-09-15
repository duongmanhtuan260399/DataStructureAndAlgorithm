import unittest

# Allow importing namespace packages from project root
import sys
import os

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from Week6_Tree.DSABinarySearchTree import DSABinarySearchTree
from Week5_LinkedList.DSALinkedList import DSALinkedList


class TestDSABinarySearchTree(unittest.TestCase):
    def setUp(self):
        self.bst = DSABinarySearchTree()
        # Class uses init() instead of __init__
        if hasattr(self.bst, "init"):
            self.bst.init()

    def test_empty_tree_behaviour(self):
        self.assertEqual(self.bst.height(), 0)
        self.assertEqual(self.bst.balance(), 100)
        self.assertEqual(self.bst.inorder(), [])
        self.assertEqual(self.bst.preorder(), [])
        self.assertEqual(self.bst.postorder(), [])

        with self.assertRaises(ValueError):
            self.bst.find(10)
        with self.assertRaises(ValueError):
            self.bst.delete(10)
        with self.assertRaises(ValueError):
            self.bst.min()
        with self.assertRaises(ValueError):
            self.bst.max()

        # Linked list return option should yield empty DSALinkedList
        inorder_ll = self.bst.inorder(return_linked_list=True)
        self.assertIsInstance(inorder_ll, DSALinkedList)
        self.assertEqual(inorder_ll.getCount(), 0)

    def test_insert_and_find(self):
        items = [(5, "A"), (3, "B"), (7, "C"), (2, "D"), (4, "E"), (6, "F"), (8, "G")]
        for k, v in items:
            self.bst.insert(k, v)

        for k, v in items:
            self.assertEqual(self.bst.find(k), v)

        # duplicate key updates value
        self.bst.insert(7, "C2")
        self.assertEqual(self.bst.find(7), "C2")

    def test_traversals(self):
        # Build known tree
        for k, v in [(5, "A"), (3, "B"), (7, "C"), (2, "D"), (4, "E"), (6, "F"), (8, "G")]:
            self.bst.insert(k, v)

        self.assertEqual(self.bst.inorder(), [(2, "D"), (3, "B"), (4, "E"), (5, "A"), (6, "F"), (7, "C"), (8, "G")])
        self.assertEqual(self.bst.preorder(), [(5, "A"), (3, "B"), (2, "D"), (4, "E"), (7, "C"), (6, "F"), (8, "G")])
        self.assertEqual(self.bst.postorder(), [(2, "D"), (4, "E"), (3, "B"), (6, "F"), (8, "G"), (7, "C"), (5, "A")])

        # Linked list variant
        ll = self.bst.preorder(return_linked_list=True)
        self.assertIsInstance(ll, DSALinkedList)
        self.assertEqual(ll.getCount(), 7)

    def test_min_max_height_balance(self):
        # empty tree already tested
        # single node
        self.bst.insert(10, "X")
        self.assertEqual(self.bst.min(), 10)
        self.assertEqual(self.bst.max(), 10)
        self.assertEqual(self.bst.height(), 1)
        self.assertEqual(self.bst.balance(), 100)

        # skewed insertions to the right
        self.bst.insert(20, "Y")
        self.bst.insert(30, "Z")
        self.assertEqual(self.bst.min(), 10)
        self.assertEqual(self.bst.max(), 30)
        self.assertGreaterEqual(self.bst.height(), 3)
        self.assertLess(self.bst.balance(), 100)

    def test_delete_leaf(self):
        for k in [5, 3, 7]:
            self.bst.insert(k, k)
        # 3 and 7 are leaves
        val = self.bst.delete(3)
        self.assertEqual(val, 3)
        with self.assertRaises(ValueError):
            self.bst.find(3)
        self.assertEqual(self.bst.inorder(), [(5, 5), (7, 7)])

    def test_delete_node_with_one_child(self):
        # Create: 5 -> left 3 -> left 2
        for k in [5, 3, 2]:
            self.bst.insert(k, k)
        # delete 3 (one child: 2)
        val = self.bst.delete(3)
        self.assertEqual(val, 3)
        self.assertEqual(self.bst.inorder(), [(2, 2), (5, 5)])

        # Right-child case: 5 -> right 7 -> right 9
        self.setUp()
        for k in [5, 7, 9]:
            self.bst.insert(k, k)
        val = self.bst.delete(7)
        self.assertEqual(val, 7)
        self.assertEqual(self.bst.inorder(), [(5, 5), (9, 9)])

    def test_delete_node_with_two_children(self):
        # Build full:        5
        #                  /   \
        #                 3     7
        #                / \   / \
        #               2  4  6   8
        for k in [5, 3, 7, 2, 4, 6, 8]:
            self.bst.insert(k, k)

        # Delete 5 (root) which has two children; should replace with inorder successor (6)
        val = self.bst.delete(5)
        self.assertEqual(val, 5)
        self.assertEqual(self.bst.inorder(), [(2, 2), (3, 3), (4, 4), (6, 6), (7, 7), (8, 8)])
        # Ensure 6 is now the root key by preorder head
        self.assertEqual(self.bst.preorder()[0][0], 6)

    def test_delete_missing_raises(self):
        for k in [10, 5, 15]:
            self.bst.insert(k, k)
        with self.assertRaises(ValueError):
            self.bst.delete(999)


if __name__ == '__main__':
    unittest.main()


