from prime import getPrimes

def test(n):
    """
    >>> test(5)
    [2, 3, 5, 7, 11]
    >>> test(10)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    >>> test(0)
    []
    >>> test(1)
    [2]
    """
    return getPrimes(n)

if __name__ == "__main__":
    import doctest
    doctest.testmod()