import json

with open('content/data.json') as json_file:
    data = json.load(json_file)


class Node:
    def __init__(self, key: int = None, value: str = None, N: int = 0):
        self.key = key  # key
        self.value = value  # associated values
        self.left = None  # link to left subtree
        self.right = None  # link to right subtree
        self.N = N  # number of nodes in subtree rooted here


from typing import List


# class definition of binary search tree
# noinspection DuplicatedCode
class BST:
    def __init__(self, keys: List, vals: List):
        self.__root = None
        for (key, val) in zip(keys, vals):
            self.insert(key, val)

    # find the number of nodes in the tree
    def size(self) -> int:
        return self.__size(self.__root)

    # find the number of nodes in the subtree whose root is node
    def __size(self, node: Node) -> int:
        if node is None:
            return 0
        else:
            return node.N

    # insert a new pair of key and associated value to the tree
    def insert(self, key: int, val: str) -> None:
        self.__root = self.__insert(self.__root, key, val)

    def __insert(self, node: Node, key: int, val: str) -> Node:
        # if the node does not exist, add new node
        if node is None: return Node(key, val, 1)
        if key < node.key:
            node.left = self.__insert(node.left, key, val)
        elif key > node.key:
            node.right = self.__insert(node.right, key, val)
        else:
            node.val = val
        node.N = self.__size(node.left) + self.__size(node.right) + 1
        return node

    # print the tree horizontally
    def printTree(self) -> None:
        self.__printTree(self.__root)

    # recursively print the nodes from right to left
    def __printTree(self, node: Node, level: int = 0) -> None:
        if node is not None:
            self.__printTree(node.right, level + 1)
            print(' ' * 6 * level + '-> ' + str(node.key))
            self.__printTree(node.left, level + 1)

    # find the height of a node with given key
    def height(self, key: int) -> int:
        def internal_height(node):
            if node is None:
                return 0
            leftAns = internal_height(node.left)
            rightAns = internal_height(node.right)
            return max(leftAns, rightAns) + 1

        def internal_traverse(node):
            if node is None:
                return None
            if node.key == key:
                return node
            else:
                if key < node.key:
                    temp_one = internal_traverse(node.left)
                elif key > node.key:
                    temp_one = internal_traverse(node.right)
                else:
                    temp_one = None
                return temp_one

        node_found = internal_traverse(self.__root)
        left_height = internal_height(node_found.left)
        right_height = internal_height(node_found.right)

        return max(left_height, right_height)

    # get the value at a node with a given key
    def getValue(self, key: int) -> str:
        return self.__getValue(self.__root, key)

    def __getValue(self, node: Node, key: int) -> str:
        if node is None: return None
        if key < node.key:
            return self.__getValue(node.left, key)
        elif key > node.key:
            return self.__getValue(node.right, key)
        else:
            return node.value

    def min(self) -> int:
        left_side = self.__root
        while left_side.left is not None:
            left_side = left_side.left
        return left_side.key

    # return the maximum key of the tree
    def max(self) -> int:
        right_side = self.__root
        while right_side.right is not None:
            right_side = right_side.right
        return right_side.key

    def floor(self, key: int):
        if self.__root is None:
            return -1

        if self.__root.key == key:
            return self.__root.key
        elif self.__root.key > key:
            side = self.__root.left
        else:
            side = self.__root.right

        while True:
            if side.left is not None and side.right is not None:
                if side.key < key:
                    side = side.right
                elif side.key > key:
                    side = side.left
            elif side.right is not None:
                if side.key < key:
                    if side.right.key > key:
                        return side.key
                    else:
                        side = side.right
            elif side.left is not None:
                if side.key > key:
                    if side.left.key < key:
                        return side.key
                else:
                    side = side.left
            else:
                if key < side.key:
                    if self.__root.key < key:
                        return self.__root.key
                    else:
                        return None
                elif key == side.key:
                    return key
                else:
                    return side.key

    def ceiling(self, key: int):
        if self.__root is None:
            return -1

        if self.__root.key == key:
            return self.__root.key
        elif self.__root.key > key:
            side = self.__root.left
        else:
            side = self.__root.right

        while True:
            if side.left is not None and side.right is not None:
                if side.key < key:
                    side = side.right
                elif side.key > key:
                    if side.left.key < key < side.key:
                        return side.key
                    else:
                        side = side.left
            elif side.right is not None:
                if side.key > key:
                    if side.right.key > key:
                        return side.key
                    else:
                        side = side.right
                else:
                    side = side.right
            elif side.left is not None:
                if side.key > key:
                    if side.left.key < key:
                        return side.key
                else:
                    side = side.left

            else:
                if key > side.key:
                    if self.__root.key < key:
                        return None
                    else:
                        return self.__root.key
                elif key == side.key:
                    return key
                else:
                    return side.key

    def rank(self, key: int) -> int:
        def find_size(node):
            size = 1
            if node.left is not None and node.key < key:
                size += find_size(node.left)
            if node.right is not None and node.key < key:
                size += find_size(node.right)

            if node.key > key or node.key == key:
                size -= 1
            if node.key > key and node.left is not None:
                size += find_size(node.left)
            return size

        def find_internal_rank(node):
            count = 0
            if key == self.__root.key:
                if node is None:
                    return 0
                else:
                    return find_size(self.__root.left)
            if key > self.__root.key:
                count += 1
                if self.__root.left is not None:
                    count += find_size(self.__root.left)
                if self.__root.right is not None:
                    count += find_size(self.__root.right)
                return count
            if key < self.__root.key:
                if self.__root.left is not None:
                    count += find_size(self.__root.left)
                return count

        return find_internal_rank(self.__root)

    def delete(self, key: int) -> None:
        def min_node(node):
            left_side = node
            while node.left is not None:
                left_side = node.left
            return left_side

        def deleteNode(node, key):
            if node is None:
                return node
            if node.key > key:
                node.left = deleteNode(node.left, key)
            elif node.key < key:
                node.right = deleteNode(node.right, key)
            else:
                if node.left is None:
                    temp = node.right
                    return temp

                elif node.right is None:
                    temp = node.left
                    return temp

                temp_node = min_node(node.right)
                node.key = temp_node.key
                node.right = deleteNode(node.right, temp_node.key)
            return node

        self.__root = deleteNode(self.__root, key)

    def avlBalance(self) -> None:
        # WRITE YOUR CODE HERE

        raise NotImplementedError
