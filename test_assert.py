from prime import getPrimes

def test1():
    n = 10
    expected = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    actual = getPrimes(n)
    assert expected == actual

def test2():
    n = 5
    expected = [2, 3, 5, 7, 11]
    actual = getPrimes(n)
    assert expected == actual

def test3():
    n = 0
    expected = []
    actual = getPrimes(n)
    assert expected == actual

def test4():
    n = 1
    expected = [2]
    actual = getPrimes(n)
    assert expected == actual

def test():
    test1()
    test2()
    test3()
    test4()
    print("Tests passed")

if __name__ == "__main__":
    test()
