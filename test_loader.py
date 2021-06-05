import os


def read_test_case(file_path):
    """
    reads one test case from file.
    returns contents of test case

    Parameters
    ----------
    file_path : str
        the path of the test case file to read.

    Returns
    -------
    list
        a list of contents of the test case.
    """

    file = open(file_path, "r")
    number = int(file.readline().strip())

    case = list()
    for i in range(number):
        case.append(file.readline().strip())

    return case


def load_test_cases(dir, file_name):
    """
    loads one test case from file.
    returns a map contents of all test cases.

    Parameters
    ----------
    dir : str
        directory of the files to load.

    file_name : str
        the name of the file that contains all
        test case files name to read.


    Returns
    -------
    dict
        a dict of contents of all test cases.
    """

    path = os.path.join(dir, file_name)

    test_cases_file_names = open(path, "r")
    test_cases = dict()

    for file_name in test_cases_file_names.readlines():
        case_name = file_name.strip().split(".")[0]
        file_path = os.path.join(dir, file_name.strip())
        test_cases[case_name] = read_test_case(file_path)

    return test_cases
