"""Provide implementations of the linked list data structure."""

# Ignore these Pylint rules.
# pylint: disable=too-few-public-methods
#     ^ This is educational code, not production code; don't care.

# Built-in libraries.
from typing import Any


class Node:
    """Define a node for a linked list.

    This node data structure can be used in a singly linked list or a
    doubly linked list.
    """

    def __init__(self, data: Any) -> None:
        """Initialize a node with the given data.

        Args:
             data: Data we want to store in a node, e.g. a number or a
                character.
        """
        self.data = data
        self.next = None
        self.prev = None  # Always None for a singly linked list.
