import numpy
import os
import inspect
import algo_test
from algo_test.solutions import exhaustive_solution, target_solution


def check_solution(testset_path):
    print "- Checking", testset_path
    A_npy = numpy.load(testset_path)
    ok_guys = 0
    ko_guys = 0
    for i in range(len(A_npy)):
        A = list(A_npy[i])
        d1 = exhaustive_solution(A)
        d2 = target_solution(A)
        if d1 != d2:
            print "ERROR in test array nr", i
            ko_guys += 1
        else:
            ok_guys += 1
    print "Test for {testset}:\n\t- OK: {ok_guys}\n\t- KO: {ko_guys}\n".format(testset=testset_path,
                                                                               ok_guys=ok_guys,
                                                                               ko_guys=ko_guys)

if __name__ == "__main__":
    test_folder = os.path.join(os.path.dirname(inspect.getfile(algo_test)), "tests")

    # check_solution(os.path.join(test_folder, "{npy_file}.npy".format(npy_file="public")))
    #
    # check_solution(os.path.join(test_folder, "{npy_file}.npy".format(npy_file="private_very_short")))

    # check_solution(os.path.join(test_folder, "{npy_file}.npy".format(npy_file="private_short")))
    #
    # check_solution(os.path.join(test_folder, "{npy_file}.npy".format(npy_file="private_long")))
    #
    check_solution(os.path.join(test_folder, "{npy_file}.npy".format(npy_file="private_very_long")))
