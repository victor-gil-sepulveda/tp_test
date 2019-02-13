

def difference(part1, part2):
    return abs(max(part1), max(part2))


def wrong_trivial_solution(A):
    """
    This is the naive (and wrong) solution delivered
    """

    if len(A) == 0:
        return 0

    if len(A) == 1:
        return A[0]

    a = max(A)
    b = min(A)

    a_index = A.index(a)
    b_index = A.index(b)

    if a_index > b_index:
        return a - b
    else:
        return b - a


def exhaustive_solution(A):
    """
    This should be a correct, but exhaustive O(n^2) solution.
    Gets the maximum difference by calculating the difference for all given k values
    """
    differences = []
    for k in range(0, len(A)-1):
        differences.append(difference(A[0:k], A[k+1:]))

