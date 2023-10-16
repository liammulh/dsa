# dsa

This repo contains my notes about common data structures and algorithms.
It also contains implementations of them. The implementations are
written in Python.

I make extensive references to the third edition of *Introduction to
Algorithms* by Cormen, Leiserson, Rivest, and Stein as "CLRS" throughout
this repo. I pilfer some definitions from Richard Hammack's *Book of
Proof*. I also refer to the official 3.12.0 Python documentation.

## Definitions

CLRS opens its chapter on data structures as follows:

> Sets are fundamental to computer science as they are to mathematics.
> Whereas mathematical sets are unchanging, the sets manipulated by
> algorithms can grow, shrink, or otherwise change over time. We call
> such sets dynamic.

We can use this definition as a jumping-off point for some other
definitions:

- **set**: A collection of things. The things in the collection are
  called **elements** of the set. (This is a naive definition of a set,
  and it leads to contradictions, but for our purposes, it will do.)
- **infinite set**: A set with infinitely many elements.
- **finite set**: A set that does not have infinitely many elements.
- **dynamic set**: A set that grow, shrink, or otherwise change over
  time.
- **algorithm**: A set of instructions for performing operations on a
  finite dynamic set.
- **computer**: A thing (e.g. a person or a machine) that can do
  arithmetic and logical operations.
- **modern computer**: A machine that can be programmed to perform
  arithmetic and logical operations.
- **program**: A set of instructions for a modern computer, typically
  written in a language intelligible to humans (a **programming
  language**), and then translated (interpreted or compiled) into a
  language that can be understood by a modern computer (machine code).
- **algorithm implementation**: A program for a modern computer
  containing an algorithm's instructions.
- **data structure**: A representation of a finite dynamic set on a
  modern computer.

## Primitive types

According to Python's language reference documentation, everything in
Python is an object. In most programming languages, an object is a thing
that has attributes (metadata) and methods (functions).

> Objects are Python’s abstraction for data. All data in a Python
> program is represented by objects or by relations between objects.
> [...] Every object has an identity, a type and a value. An object’s
> identity never changes once it has been created; you may think of it
> as the object’s address in memory. The `is` operator compares the
> identity of two objects; the `id()` function returns an integer
> representing its identity. For CPython, `id(x)` is the memory address
> where `x` is stored.

The most "atomic" (i.e. basic) types in Python are:

- numbers
    - integers (`int`): The mathematical set of integers. Range subject
      to virtual memory.
        - booleans (`bool`): Subclass of integers. `False` behaves
          similarly to 0 and `True` behaves similarly to 1.
    - floating point numbers (`float`): Machine-level double precision
      floating point numbers. Usually implemented using `double` in C.
    - complex (`complex`): Numbers with a real and imaginary part.
    - (etc.) Python also has `fraction.Fraction` and `decimal.Decimal`.
- sequences
    - immutable sequences
        - strings (`str`): An immutable sequence of Unicode code points.
          (A Unicode code point is a numeric value associated with an
          abstract character. Character encoding forms, such as UTF-8
          and UTF-16, determine how a Unicode code point should be
          encoded as a sequence of bytes. In UTF-8, if the code point is
          less than 128, it’s represented by the corresponding byte
          value, but if the code point is greater than or equal to 128,
          it’s turned into a sequence of two, three, or four bytes,
          where each byte of the sequence is between 128 and 255.)
        - tuples (`tuple`)
        - ranges (`range`)
        - bytes (`bytes`)
    - mutable sequences
        - lists (`list`)
        - byte arrays (`bytearray`)
        - (etc.) Python also has `collections` and `array` modules.
- sets
    - sets (`set`)
    - frozen sets (`frozenset`)
- mappings
    - dictionaries (`dict`)
    - (etc.) Python also has `collections` and `array` modules.

## Data structures

CLRS lists common operations on a dynamic set. Some of these operations
simply query the set whereas others modify the set.

- `search(S, e)`: Return an element *e* if it exists in the set.
  Otherwise, return a value indicating *e* isn't in the set.
- `insert(S, e)`: Add element *e* to *S*.
- `delete(S, e)`: Remove element *e* from *S*.
- `minimum(S)`: Return the smallest element in *S*.
- `maximum(S)`: Return the largest element in *S*.
- `successor(S, e)`: Return the element in *S* that comes after *e*.
- `predecessor(S, e)`: Return the element in *S* that comes before
  **e**.

The common data structures we care about are:

- array
- linked list
- hash table
- stack
- queue
- tree
- graph
