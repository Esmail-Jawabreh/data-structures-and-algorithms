import pytest
from CC.trees.binaryTree import *
from CC.trees.binarySearchTree import *
from CC.trees.maximumValue import *


@pytest.fixture
def empty_tree():
    return BinarySearchTree()


@pytest.fixture
def tree_with_root():
    tree = BinarySearchTree()
    tree.add(10)
    return tree


@pytest.fixture
def sample_tree():
    tree = BinarySearchTree()
    tree.add(10)
    tree.add(5)
    tree.add(15)
    tree.add(2)
    tree.add(7)
    tree.add(12)
    tree.add(20)
    return tree


## CC-15
def test_instantiate_empty_tree(empty_tree):
    assert empty_tree.root is None


def test_instantiate_tree_with_root(tree_with_root):
    assert tree_with_root.root.value == 10
    assert tree_with_root.root.left is None
    assert tree_with_root.root.right is None


def test_add_child_nodes(sample_tree):
    assert sample_tree.root.value == 10
    assert sample_tree.root.left.value == 5
    assert sample_tree.root.right.value == 15


def test_preorder_traversal(sample_tree):
    expected_result = [10, 5, 2, 7, 15, 12, 20]
    assert sample_tree.preorder_traversal(sample_tree.root) == expected_result


def test_inorder_traversal(sample_tree):
    expected_result = [2, 5, 7, 10, 12, 15, 20]
    assert sample_tree.inorder_traversal(sample_tree.root) == expected_result


def test_postorder_traversal(sample_tree):
    expected_result = [2, 7, 5, 12, 20, 15, 10]
    assert sample_tree.postorder_traversal(sample_tree.root) == expected_result


def test_contains_existing_value(sample_tree):
    assert sample_tree.contains(10) is True
    assert sample_tree.contains(5) is True
    assert sample_tree.contains(20) is True


def test_contains_non_existing_value(sample_tree):
    assert sample_tree.contains(3) is False
    assert sample_tree.contains(100) is False
    assert sample_tree.contains(8) is False


## CC-16
def test_find_maximum_value():
    # Test case 1: Empty tree
    tree = BinaryTree()
    with pytest.raises(Exception):
        tree.find_maximum_value()

    # Test case 2: Tree with a single node
    tree = BinaryTree()
    tree.root = Node(5)
    assert tree.find_maximum_value() == 5

    # Test case 3: Tree with multiple nodes
    tree = BinaryTree()
    tree.root = Node(5)
    tree.root.left = Node(3)
    tree.root.right = Node(8)
    tree.root.left.left = Node(9)
    tree.root.left.right = Node(4)
    tree.root.right.left = Node(2)
    tree.root.right.right = Node(7)
    assert tree.find_maximum_value() == 9

    # Test case 4: Tree with negative values
    tree = BinaryTree()
    tree.root = Node(-2)
    tree.root.left = Node(-5)
    tree.root.right = Node(-1)
    assert tree.find_maximum_value() == -1
