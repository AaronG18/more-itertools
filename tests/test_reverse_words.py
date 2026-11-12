from more_itertools import take


def test_take_basic():
    # NOTE: this test exercises an EXISTING function, not the new reverse_words
    # addition. It passes on both base and head, so the verifier should report
    # NEEDS_EVIDENCE (the suite does not demonstrate the change).
    assert list(take(2, [1, 2, 3, 4])) == [1, 2]
