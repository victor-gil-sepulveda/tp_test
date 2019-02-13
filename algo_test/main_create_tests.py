import inspect
import numpy
from numpy import random
import algo_test
import os
from algo_test.solutions import wrong_trivial_solution, exhaustive_solution


def generate_test_arrays(file_path, num_tests, n_min, n_max):
    test_arrays = []

    for i in range(num_tests):
        # Create the test array
        A = list(random.uniform(-1000000, 1000000, max(n_min, n_max * random.random())).astype(int))
        max_diff_naive = wrong_trivial_solution(A)
        max_diff_exhaustive = exhaustive_solution(A)
        if max_diff_naive != max_diff_exhaustive:
            # This is a good candidate for testing
            test_arrays.append(A)
    numpy.save(file_path, test_arrays)

if __name__ == "__main__":
    test_folder = os.path.join(os.path.dirname(inspect.getfile(algo_test)), "tests")

    # Generate tests with different sizes

    generate_test_arrays(os.path.join(test_folder, "private_short"), 100, 2, 100)

    generate_test_arrays(os.path.join(test_folder, "private_long"), 50, 1000, 10000)

    generate_test_arrays(os.path.join(test_folder, "private_very_long"), 10, 10000, 100000)


