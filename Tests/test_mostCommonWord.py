import pytest
from CC.Mock_Interviews.CC34.MostCommonWord.mostCommonWord import most_common_word


def test_most_common_word():
    book = "In a galaxy far far away"
    assert most_common_word(book) == "far"

    book = "Taco cat ate a taco"
    assert most_common_word(book) == "taco"

    book = "No. Try not. Do or do not. There is no try."
    assert most_common_word(book) == "no"
