from test_loader import load_test_cases
import time
al = list()


def compute_LPS(string, M, lps):
    """
    A utility function to fill lps[] or compute prefix function
    used in KMP string matching algorithm. Refer
    https://www.geeksforgeeks.org/archives/11902 for details
    """

    # lps[i] = the longest proper prefix of pat[0..i]
    # which is also a suffix of pat[0..i]
    length = 0
    i = 1
    lps[0] = 0  # lps[0] is always 0

    # loop calculates lps[i] for i = 1 to M-1
    while i < M:
        if string[i] == string[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            # For edge cases. Consider the example AAACAAAA
            if length != 0:
                length = lps[length-1]
            else:
                lps[i] = 0
                i += 1

    # Returns true if string is repetition of one of
    # its substrings else return false.


def is_beautiful(string):
    """
    checks given string is beautiful string, O(n)

    Parameters
    ----------
    string : str
        string to be checked for beautifulness.

    Returns
    -------
    bool
        a boolean value indicating if string is beautiful or not.

    """

    # Find length of string and create an array to
    # store longest proper prefix values used in KMP.
    n = len(string)
    lps = [0] * n

    # Preprocess the pattern (calculate lps[] array)
    compute_LPS(string, n, lps)

    # Find length of longest suffix which is also
    # prefix of str.
    length = lps[n - 1]

    # If there exist a suffix which is also prefix AND
    # the substring that repeats exaactly 2 times.
    if length > 0 and n / length == 2:
        return True
    else:
        return False


def find_subsequences(string, answer):
    """
    finds subsequences of a string in a recursive manner.
    writes found subsequences to the al dict.

    Parameters
    ----------
    string : str
        string

    answer: str
        answer
    """

    if len(string) == 0:
        if len(answer) > 1:
            al.append(answer)
        return

    find_subsequences(string[1:], answer + string[0])

    find_subsequences(string[1:], answer)


def calculate_beautiful_string_count(string):
    """
    calcules beautiful substrings count for given string.
    returns count of beautiful substrings.

    Parameters
    ----------
    string : str
        list of strings to calculate beautiful substrings

    Returns
    -------
    int
        number of beautiful substrings for given string.
    """

    subsequences = find_subsequences(string, "")
    n = len(al)
    count = 0
    for i in range(n):
        if is_beautiful(al[i]):
            count += 1

    return count


def print_list(lst):
    [print(item) for item in lst]


def run_tests():
    cases = load_test_cases("./test", "test_cases.txt")
    f = open("./outputs/results.txt", "w")

    for case_name, case_strings in cases.items():
        beautiful_string_counts = list()
        start = time.time()
        for s in case_strings:
            al = list()
            beautiful_string_counts.append(
                calculate_beautiful_string_count(s))

        print("Case:", case_name)
        print_list(beautiful_string_counts)
        elapsed_time = time.time() - start
        print("\nTook: ", elapsed_time, " seconds")
        print("--------------------------------------------------------\n")

        f.write(f"Case: {case_name}\n")
        [f.write(f"{item}\n") for item in beautiful_string_counts]
        f.write(f"\nTook: {elapsed_time} seconds.\n")
        f.write("--------------------------------------------------------\n\n")


if __name__ == "__main__":
    global_counter = 0
    run_tests()
