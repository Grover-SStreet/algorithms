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
        # WRITE YOUR CODE HERE

        raise NotImplementedError

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
        if key == self.__root.key:
            return self.__root.key
        elif key < self.__root.key:
            left_side = self.__root
            while left_side is not None:
                if key > left_side.key:
                    if left_side.right.key > key and left_side.right.left is None:
                        return left_side.key
                    else:
                        left_side = left_side.right
                elif key < left_side.key:
                    left_side = left_side.left
                elif key == left_side.key:
                    return left_side.key
                if left_side.right is None and left_side.left is None:
                    if left_side.key > key:
                        return None
                    else:
                        return left_side.key
        elif key > self.__root.key:
            right_side = self.__root
            while right_side is not None:
                if key > right_side.key:
                    if right_side.right.key > key and right_side.right.left is None:
                        return right_side.key
                    else:
                        right_side = right_side.right
                elif key < right_side.key:
                    right_side = right_side.left
                elif key == right_side.key:
                    return right_side.key
                if right_side.right is None and right_side.left is None:
                    if key < right_side.key:
                        return self.__root.key
                    else:
                        return right_side.key

    def ceiling(self, key: int):
        if key == self.__root.key:
            return self.__root.key
        elif key > self.__root.key:
            right_side = self.__root
            while right_side is not None:
                if key < right_side.key:
                    if right_side.right.key < key and right_side.right.left is None:
                        return left_side.key
                    else:
                        left_side = left_side.right
                elif key > left_side.key:
                    left_side = left_side.left
                elif key == left_side.key:
                    return left_side.key
                if left_side.right is None and left_side.left is None:
                    if left_side.key < key:
                        return None
                    else:
                        return left_side.key

        raise NotImplementedError

        # elif key > self.__root.key:
        #     right_side = self.__root
        #     while right_side is not None:
        #         if key > right_side.key:
        #             if right_side.right.key > key and right_side.right.left is None:
        #                 return right_side.key
        #             else:
        #                 right_side = right_side.right
        #         elif key < right_side.key:
        #             right_side = right_side.left
        #         elif key == right_side.key:
        #             return right_side.key
        #         if right_side.right is None and right_side.left is None:
        #             if key < right_side.key:
        #                 return self.__root.key
        #             else:
        #                 return right_side.key

    def rank(self, key: int) -> int:
        # WRITE YOUR CODE HERE

        raise NotImplementedError

    def delete(self, key: int) -> None:
        # WRITE YOUR CODE HERE

        raise NotImplementedError

    def avlBalance(self) -> None:
        # WRITE YOUR CODE HERE

        raise NotImplementedError


# assert(tc_1.ceiling(9)==10)
# assert(tc_1.ceiling(4)==4)
# assert(tc_1.ceiling(5)==6)
# assert(tc_1.ceiling(2)==3)

# test case 4
# tc_4 = BST(**data['testcase_4'])
# assert(tc_4.ceiling(31)==35)
# assert(tc_4.ceiling(41)==45)
# assert(tc_4.ceiling(25)==25)
# assert(tc_4.ceiling(51)==None)