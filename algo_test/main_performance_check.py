import os
import time
import numpy
import inspect
import algo_test
from algo_test.solutions import exhaustive_solution, target_solution


def performance_test(testset_path):
    A_npy = numpy.load(testset_path)
    for i in range(len(A_npy)):
        A = list(A_npy[i])
        t1 = time.time()
        exhaustive_solution(A)
        t2 = time.time()
        target_solution(A)
        t3 = time.time()
        print t2-t1, t3-t2


if __name__ == "__main__":
    test_folder = os.path.join(os.path.dirname(inspect.getfile(algo_test)), "tests")

    performance_test(os.path.join(test_folder, "{npy_file}.npy".format(npy_file="private_long")))
