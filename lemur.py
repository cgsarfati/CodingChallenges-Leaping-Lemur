"""Leaping lemur.

Calculate the fewest number of jumps the lemur needs to
jump to the last tree. The lemur can jump 1 or 2 branches.
It cannot use deadly branch (1 in the list).

    >>> lemur([0])
    0

    >>> lemur([0, 0])
    1

    >>> lemur([0, 0, 0])
    1

    >>> lemur([0, 1, 0])
    1

    >>> lemur([0, 0, 1, 0])
    2

    >>> lemur([0, 0, 0, 0, 1, 0, 0, 1, 0])
    5
"""

# BRUTE FORCE


def lemur(branches):
    """Return number of jumps needed."""

    assert branches[0] == 0, "First branch must be alive"
    assert branches[-1] == 0, "Last branch must be alive"

    num_jumps = 0
    current = 0

    if len(branches) == 2:
        return 1

    while current != len(branches) - 1:
        peek = current + 2
        if branches[peek] == 0:
            num_jumps += 1
            current = peek
        else:
            num_jumps += 1
            current += 1

    return num_jumps

    # 0 = alive, 1 = dead
    # 1st and last always alive
    # jumping to end always possible
    # default - make lemur jump 2; if lands on dead, jump 1
    # counter for each iteration (2x/1x = 1 jump); return at end
    # need to know current value inside each iteration 
    # need to peek value two items ahead within each iteration (enumerate?)

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. NICE JUMPING!\n"