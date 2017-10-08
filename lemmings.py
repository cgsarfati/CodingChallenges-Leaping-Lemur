"""Lazy lemmings.

Find the farthest any single lemming needs to travel for food.

    >>> furthest(3, [0, 1, 2])
    0

    >>> furthest(3, [2])
    2

    >>> furthest(3, [0])
    2

    >>> furthest(6, [2, 4])
    2

    >>> furthest(7, [0, 6])
    3
"""

# BRUTE FORCE (On2)


def furthest(num_holes, cafes):
    """Find longest distance between a hole and a cafe."""

    worst = 0

    for hole in range(num_holes):
        # lookng at all cafes, find distance to hole. pick min distance.
        dist = min([abs(hole - cafe) for cafe in cafes])

        # compare to longest distance. if dist > worst, replace.
        worst = max(worst, dist)

    return worst

# BINARY SEARCH (Ologn)


def furthest_optimized(num_holes, cafes):

    from bisect import bisect_left

    worst = 0

    for hole in range(num_holes):

        # find place we'd insert hole into cafes list
        idx = bisect_left(cafes, hole)

        # when hole after all cafes; find dist to prev cafe
        if idx == len(cafes):
            dist = hole - cafes[idx - 1]

        # when hole before all cafes; find dist preceeding cafe
        elif idx == 0:
            dist = cafes[idx] - hole

        # when hole is cafe
        elif cafes[idx] == hole:
            dist = 0

        # when hole b/w cafe; find min dist b/w before and after
        else:
            dist = min(hole - cafes[idx - 1], cafes[idx] - hole)

        # through each iteration, keep track of longest dist
        worst = max(worst, dist)

    return worst

# CLEVER SOLN (On)


def furthest_best(num_holes, cafes):
    """Find the 2 furthest cafes from each other, then determine which hole
    would have to travel the furthest between them."""

    # dist from 1st hole to 1st cafe, and last hole to last cafe
    distances = [cafes[0], num_holes - cafes[-1] - 1]

    # b/w cafes: distance is half the distance to leftward cafe
    for i in range(1, len(cafes)):
        distances.append((cafes[i] - cafes[i - 1]) // 2)

    # from 3 scenarios, pick longest distance
    return max(distances)


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED; GREAT JOB!\n"
