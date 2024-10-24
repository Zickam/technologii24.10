import pytest

from prime import getPrimes

class TestPrimes:
    def test_1(self):
        n = 10
        expected = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        actual = getPrimes(n)
        assert expected == actual

    def test_2(self):
        n = 5
        expected = [2, 3, 5, 7, 11]
        actual = getPrimes(n)
        assert expected == actual

    def test_3(self):
        n = 0
        expected = []
        actual = getPrimes(n)
        assert expected == actual

    def test_4(self):
        n = 1
        expected = [2]
        actual = getPrimes(n)
        assert expected == actual
