def _parent(i):
    """
    Return the index of the parent of the element at index i.
    Converted from 1-based indexing.
    """
    return int((i - 1) // 2)

def _left(i):
    """
    Returns the index of the left child of the element at index i.
    Converted from 1-based indexing.
    """
    return 2 * i + 1

def _right(i):
    """
    Returns the index of the right child of the element at index i.
    Converted from 1-based indexing.
    """
    return 2 * i + 2

def _heap_increase_key(A, i, key):
    """
    "Bubble" a key up the heap.
    """
    pass

def _max_heapify(A, i):
    """
    Element is in the list but not yet part of the heap. This
    adds i into the heap.
    """
    pass

def max_heap_insert(A, key):
    """
    Inserts an element into the heap. This method
    should append a None value to the list to make
    room for the new key and call _heap_increase_key.
    """
    pass

def heap_extract_max(A):
    """
    Removes the maximum value from the heap and returns it.
    The list size should be reduced by 1.
    """
    pass

def build_max_heap(A):
    """
    Takes a list A of unordered elements and reorders the elements
    to construct a max binary heap.
    """
    pass

def heapsort(A):
    """
    Sorts a list of elements by converting the list into a heap
    and then extracting each element from biggest to smallest.
    Note that this is done in place.
    """
    pass







