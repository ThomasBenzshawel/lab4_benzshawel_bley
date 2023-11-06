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
    if key < A[i]:
        print("Error, new key is smaller than current key")
    else:
        A[i] = key
        while i > 0 and A[_parent(i)] < A[i]:
            temp = A[i]
            A[i] = A[_parent(i)]
            A[_parent(i)] = temp
            i = _parent(i)

def _max_heapify(A, i, heap_size):
    """
    Element is in the list but not yet part of the heap. This
    adds i into the heap.
    """
    l = _left(i)
    r = _right(i)

    if l < heap_size and A[l] > A[i]:
        largest = l
    else:
        largest = i

    if r < heap_size and A[r] > A[largest]:
        largest = r
    if largest is not i:
        temp = A[i]
        A[i] = A[largest]
        A[largest] = temp
        _max_heapify(A, largest, heap_size)

def max_heap_insert(A, key):
    """
    Inserts an element into the heap. This method
    should append a None value to the list to make
    room for the new key and call _heap_increase_key.
    """
    # A.heap_size = A.heap_size + 1
    A.append(-99999999)
    _heap_increase_key(A, len(A) - 1, key)

def heap_extract_max(A):
    """
    Removes the maximum value from the heap and returns it.
    The list size should be reduced by 1.
    """
    max = -99999999
    if len(A) < 1:
        print("Heap underflow error")
    else:
        max = A[0]
        A[0] = A[len(A) - 1]
        # A.heap_size = A.heap_size - 1
        del A[0]
        _max_heapify(A, 0, len(A))
    return max

def build_max_heap(A):
    """
    Takes a list A of unordered elements and reorders the elements
    to construct a max binary heap.
    """

    # A.heap_size = 1

    for i in range(len(A)//2 - 1, -1, -1):
        _max_heapify(A, i, len(A))

def heapsort(A):
    """
    Sorts a list of elements by converting the list into a heap
    and then extracting each element from biggest to smallest.
    Note that this is done in place.
    """

    build_max_heap(A)
    for i in range(len(A) - 1, 0, -1):
        A[0], A[i] = A[i], A[0]
        print(A)
        _max_heapify(A, 0, i)