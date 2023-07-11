import pytest
from CC.Mock_Interviews.CC34.UniqueString.uniqueString import is_unique


def test_is_unique():
    assert is_unique("The quick brown fox jumps over the lazy dog") == False
    assert is_unique("I love cats") == True
    assert is_unique("Donald the duck") == False
