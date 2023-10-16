"""Test our linked list implementations."""

# Ignore these Pylint rules.
# pylint: disable=redefined-outer-name
#     ^ Pytest fixtures cause this error.

# Third-party dependencies.
import pytest

# In-house code.
from ds.linked_list import Node

# Constants.
NODE_DATA = 10


@pytest.fixture
def node():
    """Return an initialized linked list node for testing."""
    return Node(NODE_DATA)


def test_initializes_node(node):
    """Ensure we can initialize a linked list node."""
    assert node.data == NODE_DATA
    assert node.next is None
    assert node.prev is None
