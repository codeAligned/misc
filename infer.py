# Razi Shaban
# 3/19/15
#
# The runtime of the code below is O(n*log(n)) for each test case, as 
# Python's sorted runs a modified mergesort @ O(n*log(n)) and we then
# generate the triangular number to count matching indices. triangular(n)
# runs in O(n), and in the worst case we are running triangular on the
# entire entry, for a worst-case triangular runtime of O(n), which is 
# asymptotically bound by O(n*log(n)). Thus, our whole-program runtime is
# O(m*log(m) * num_cases), where m = max_len(entries), as we can use
# our longest entry as an upper bound for all of the entries.

# accepted solution to https://www.hackerrank.com/contests/101feb14/challenges/sherlock-and-pairs
# run: python infer.py < infer.test

import sys

def triangular(n):
    # recursion depth is quickly exceeded :( but this is the idea:
    # if n == 0:
    #     return 0
    # else:
    #     return n + triangular(n-1)
    num = 0
    while n >= 1:
        num += n
        n -= 1
    return num


def main():
    data = sys.stdin.readlines()
    num_cases = int(data[0])
    

    for i in range(1, num_cases*2 + 1, 2):
        # Python allows us to not need array_size (data[i]). Thanks Python!
        # Counting by two allows us to get right to the test cases
        dupl_count = 0

        array = map(int, data[i+1].split())
        sorted_array = sorted(array)

        j = 1
        curr_count = 0
        while j < len(sorted_array):
            # dealing with multiple duplicates
            if sorted_array[j] == sorted_array[j-1]:
                curr_count += 1
            else:
                if curr_count > 0:
                    dupl_count += 2*triangular(curr_count)
                    curr_count = 0

            j += 1

        # this is a pretty ugly way to deal with the while loop, but it works
        if curr_count > 0:
            dupl_count += 2*triangular(curr_count)

        print dupl_count;

main()