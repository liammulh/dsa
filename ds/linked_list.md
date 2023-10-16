# Linked list

In languages like C, arrays have a fixed length. If you aren't sure how
many elements you wish to store in an array, you could implement a
dynamically re-sizeable array. When your fixed-size array runs out of
space, you create a new, larger array and copy the values from the
old array to the new array. Alternatively, you could opt for a linked
list. A linked list is a list data structure that relies on links rather
than a contiguous block of memory to order the list.

To understand how the links in a linked list work, we need to understand
that a linked list is made up of nodes. A node is a simple data
structure that has at least two fields. One field is a data field. The
other field is a pointer to the next node in the linked list. Sometimes
a node can have pointers to other nodes as well. These pointers are the
aforementioned links. In a language like C, these pointers are literally
C pointers to nodes.

In a language like Python where lists don't have a fixed size, a linked
list is contrived, but the implementation of a linked list is roughly
the same for all C-like languages.