from more_itertools import tail


def test_tail_with_pad_shorter_than_n():
    assert list(tail(5, 'ABC', pad='-')) == ['-', '-', 'A', 'B', 'C']


def test_tail_with_pad_longer_than_n():
    assert list(tail(3, 'ABCDEFG', pad='-')) == ['E', 'F', 'G']


def test_tail_without_pad_unchanged():
    assert list(tail(3, 'ABCDEFG')) == ['E', 'F', 'G']
