import pytest
from CC.trees.intersection import BinaryTree, tree_intersection


def test_tree_intersection():
    # the first binary tree
    tree1 = BinaryTree()
    tree1.add(150)
    tree1.add(100)
    tree1.add(250)
    tree1.add(75)
    tree1.add(160)
    tree1.add(200)
    tree1.add(350)
    tree1.add(125)
    tree1.add(175)
    tree1.add(300)
    tree1.add(500)

    # the second binary tree
    tree2 = BinaryTree()
    tree2.add(42)
    tree2.add(100)
    tree2.add(600)
    tree2.add(15)
    tree2.add(160)
    tree2.add(200)
    tree2.add(350)
    tree2.add(125)
    tree2.add(175)
    tree2.add(4)
    tree2.add(500)

    result = tree_intersection(tree1, tree2)

    # the Output
    assert result == {100, 160, 125, 175, 200, 350, 500}


def test_tree_intersection_empty_trees():
    # empty binary trees
    tree1 = BinaryTree()
    tree2 = BinaryTree()

    result = tree_intersection(tree1, tree2)

    assert result == set()


def test_tree_intersection_no_intersection():
    # the first binary tree
    tree1 = BinaryTree()
    tree1.add(1)
    tree1.add(2)
    tree1.add(3)

    # the second binary tree
    tree2 = BinaryTree()
    tree2.add(4)
    tree2.add(5)
    tree2.add(6)

    result = tree_intersection(tree1, tree2)

    assert result == set()
