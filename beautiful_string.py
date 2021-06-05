def computeLPS(string, M, lps):
    length = 0
    i = 1

    lps[0] = 0

    while i < M:
        if string[i] == string[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length-1]
            else:
                lps[i] = 0
                i += 1


# Check is beautiful string, O(n)
def isBeautiful(string):
    n = len(string)
    lps = [0] * n

    computeLPS(string, n, lps)

    length = lps[n-1]

    if length > 0 and n / length == 2:
        return True
    else:
        False


# Find subsequences of a string.
def find_subsequences(string, answer):
    if len(string) == 0:
        if len(answer) > 1:
            al.append(answer)
        return

    find_subsequences(string[1:], answer + string[0])

    find_subsequences(string[1:], answer)


strings_list = []
string_count = int(input("How many strings: "))
for i in range(string_count):
    input_string = input("Enter string: ")
    strings_list.append(input_string)


for s in strings_list:
    al = list()
    subsequences = find_subsequences(s, "")
    n = len(al)
    count = 0
    for i in range(n):
        if isBeautiful(al[i]):
            count += 1

    print(count)
