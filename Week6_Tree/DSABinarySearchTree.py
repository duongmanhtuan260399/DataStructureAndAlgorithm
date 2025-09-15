from Week5_LinkedList.DSALinkedList import DSALinkedList
class DSABinarySearchTree():
    def init (self, keey_type_tring=False):
        self._root = None # start with an empty tree
        self._compare_as_string = bool(keey_type_tring)

    class DSATreeNode():
        def init (self, inKey, inValue):
            self._key = inKey
            self._value = inValue
            self._left = None
            self._right = None
        def __str__(self):
            return "Key: " + str(self._key) + ", Value: "+ str(self._value)

    def _findRec(self, key, cur: DSATreeNode):
        value = None
        if cur is None:  # Base case: not found
            raise ValueError("Key " + str(key) + " not found")
        keyN = self._normalize_key(key)
        curKeyN = self._normalize_key(cur._key)
        if keyN == curKeyN:
            value = cur._value
        elif keyN < curKeyN:  # Go left (recursive)
            value = self._findRec(key, cur._left)
        else:  # Go right(recursive)
            value = self._findRec(key, cur._right)
        return value

    def find(self, key):
        return self._findRec(key, self._root)

    def _createNode(self, key, value):
        node = self.DSATreeNode()
        node._key = key
        node._value = value
        node._left = None
        node._right = None
        return node

    def _insertRec(self, cur: DSATreeNode, key, value):
        updatedSubtreeRoot = cur
        if cur is None:
            updatedSubtreeRoot = self._createNode(key, value)
        else:
            keyN = self._normalize_key(key)
            curKeyN = self._normalize_key(cur._key)
            if keyN == curKeyN:
                cur._value = value
                updatedSubtreeRoot = cur
            elif keyN < curKeyN:
                cur._left = self._insertRec(cur._left, key, value)
                updatedSubtreeRoot = cur
            else:
                cur._right = self._insertRec(cur._right, key, value)
                updatedSubtreeRoot = cur
        return updatedSubtreeRoot

    def insert(self, key, value):
        self._root = self._insertRec(self._root, key, value)
        return None


    def delete(self, key):
        self._root, deletedValue = self._deleteRec(self._root, key)
        return deletedValue

    def _normalize_key(self, key):
        if self._compare_as_string:
            return str(key)
        try:
            return int(key)
        except Exception:
            raise ValueError("Key cannot be converted to integer for comparison: " + str(key))

    def _deleteRec(self, cur: DSATreeNode, key):
        newSubtreeRoot = cur
        deletedValue = None

        if cur is None:
            raise ValueError("Key " + str(key) + " not found")
        keyN = self._normalize_key(key)
        curKeyN = self._normalize_key(cur._key)
        if keyN < curKeyN:
            cur._left, deletedValue = self._deleteRec(cur._left, key)
            newSubtreeRoot = cur
        elif keyN > curKeyN:
            cur._right, deletedValue = self._deleteRec(cur._right, key)
            newSubtreeRoot = cur
        else:
            # Node to delete found
            deletedValue = cur._value
            if cur._left is None and cur._right is None:
                newSubtreeRoot = None
            elif cur._left is None:
                newSubtreeRoot = cur._right
            elif cur._right is None:
                newSubtreeRoot = cur._left
            else:
                # Two children: replace with inorder successor (min in right subtree)
                successor = self._findMin(cur._right)
                cur._key = successor._key
                cur._value = successor._value
                # Delete successor node from right subtree
                cur._right, _ = self._deleteRec(cur._right, successor._key)
                newSubtreeRoot = cur

        return newSubtreeRoot, deletedValue

    def _findMin(self, cur: DSATreeNode):
        node = cur
        while node is not None and node._left is not None:
            node = node._left
        return node

    def _findMax(self, cur: DSATreeNode):
        node = cur
        while node is not None and node._right is not None:
            node = node._right
        return node

    def _heightOf(self, cur: DSATreeNode):
        h = 0
        if cur is not None:
            leftH = self._heightOf(cur._left)
            rightH = self._heightOf(cur._right)
            h = 1 + (leftH if leftH > rightH else rightH)
        return h

    def min(self):
        if self._root is None:
            raise ValueError("Tree is empty")
        node = self._findMin(self._root)
        return node._key

    def max(self):
        if self._root is None:
            raise ValueError("Tree is empty")
        node = self._findMax(self._root)
        return node._key

    def height(self):
        return self._heightOf(self._root)

    def balance(self):
        if self._root is None:
            return 100
        leftH = self._heightOf(self._root._left)
        rightH = self._heightOf(self._root._right)
        denom = leftH + rightH
        score = 100
        if denom > 0:
            diff = leftH - rightH if leftH > rightH else rightH - leftH
            score = int(round((1 - (diff / denom)) * 100))
        return score

    def _inorderNodes(self, node: DSATreeNode, ll: DSALinkedList):
        if node is not None:
            self._inorderNodes(node._left, ll)
            ll.insertLast(node)
            self._inorderNodes(node._right, ll)

    def inorder(self):
        ll = DSALinkedList()
        self._inorderNodes(self._root, ll)
        return ll

    def _preorderNodes(self, node: DSATreeNode, ll: DSALinkedList):
        if node is not None:
            ll.insertLast(node)
            self._preorderNodes(node._left, ll)
            self._preorderNodes(node._right, ll)

    def preorder(self):
        ll = DSALinkedList()
        self._preorderNodes(self._root, ll)
        return ll

    def _postorderNodes(self, node: DSATreeNode, ll: DSALinkedList):
        if node is not None:
            self._postorderNodes(node._left, ll)
            self._postorderNodes(node._right, ll)
            ll.insertLast(node)

    def postorder(self):
        ll = DSALinkedList()
        self._postorderNodes(self._root, ll)
        return ll