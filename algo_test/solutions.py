

def difference(part1, part2):
    return abs(max(part1) - max(part2))


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
    for k in range(0, len(A)-1): # k in [0, N-1]
        differences.append(difference(A[0:k+1], A[k+1:]))
    # print differences
    return max(differences)


def target_solution(A):
    """
    The idea is doing the same that in the exhaustive solution but in only
    O(n) passes
    """
    differences = []
    max_p1 = A[0]
    max_p2 = A[-1]
    N = len(A)
    diff = [0]*(N-1)

    # O(n)
    for k in range(0, N-1): # 0 <= k <= N-2
        max_p1 = max(A[k], max_p1)
        max_p2 = max(A[N-1-k], max_p2)
        diff[k] += max_p1
        diff[N-2-k] -= max_p2 #N-N-2

    # O(n)
    max_diff = abs(diff[0])
    for i in range(len(diff)):
        max_diff = max(max_diff, abs(diff[i]))
        # diff[i] = abs(diff[i])

    # O(n)
    return max_diff #max(diff)
