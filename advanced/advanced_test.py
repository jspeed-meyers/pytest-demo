"""Advanced pytest capabilities"""

import sys

import pytest

from advanced import blackBox, createList, yo


def test_yo_failure():
    """Unit test that checks for appropriate error."""
    with pytest.raises(TypeError):
        yo("Nina", "Lucas")


@pytest.mark.xfail
def test_blackBox():
    """Unit test that is expected to fail."""
    assert blackBox("Eeny", "Meeny", 12) == "the Grinch"


@pytest.mark.skip
def test_createList():
    """Skip this unittest."""
    assert createList(5) == [1, 2, 3]


@pytest.mark.skipif(sys.platform == "win32", reason="Bill Gates said so.")
def test_createList2():
    """Skip this unittest if platform is windows."""
    assert createList(5) == [0, 1, 2, 3, 4]
