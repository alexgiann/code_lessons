def nth(s, n):
    '''(int, int) -> int
    Returns every number starting from s incrementing by n.
    >>> odds = nth(1, 2)
    >>> odds.__next__()
    1
    >>> odds.__next__()
    3
    '''

    while s >= 0:
        yield s
        s = s + n 
