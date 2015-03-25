# Path Reconstruction

# Reminder: This question is primarily an algorithmic exercise, so please submit an efficient solution.  You can submit working code in your choice of a number of mainstream (and some non-mainstream) languages: C, C++, Java, C#, PHP, Python, R, Ruby, Javascript, CoffeeScript, Haskell, Scala.  The code should read from stdin and write to stdout.  You may use standard libraries, but not third-party libraries.

# Email back the solution as an attachment, and also describe the asymptotic time complexity of your solution in big-O notation.

# You're given a list of pairs of words.  The words are the (unique) names of vertices on a graph, and the pairs are the directed edges in the graph.  Example:

# lax jfk
# sfo bos
# jfk sea
# bos lax

# Your job is to reorder the list (which is in an arbitrary order) into a path, such that the second word of some pair (i) is equal to the first word of the next pair in the list (i + 1).  In other words, the reordered list should form a path through the graph.  For the above example, you should produce:

# sfo bos
# bos lax
# lax jfk
# jfk sea

# You can assume there are no cycles and that there's exactly one unique path that traverses all the edges.

# Your program should read the list from stdin, one pair per line, and write the reordered list to stdout, following the above format.





# Razi Shaban
# 3/21/15
#
# Path Reconstruction
# Input an unordered list of vertices, print them in order.
# run: python infer2.py < infer2.test
# 
# The program below has an average runtime of O(n), thanks to leveraging
# hash-table properties. It also has an amortized worst-case (AWC) runtime of 
# O(n^2), but Python is smart enough to avoid this scenario [0]. Inserting n 
# edges into the dict and origins costs O(1) each, O(n) AWC, for a runtime of 
# O(n), O(n^2) AWC. Pulling edges from the dictionary to output the path has a
# similar runtime, O(1) to get each edge's information, O(n) AWC for O(n) 
# runtime, O(n^2) AWC. Finding the starting point of the path is the most 
# expensive operation; we must check if each origin is in the destinations dict.
# Fortunately, using another dictionary (a space-time tradeoff) allows us to 
# do each check in O(1), O(n) AWC, for a total runtime of O(n), O(n^2) AWC.
# Thus, our average runtime will be O(n) and our AWC runtime will be O(n^2).
#
# [0] https://wiki.python.org/moin/TimeComplexity

import sys

edges = dict()
destinations = dict()
origins = list()
start = ""

for line in sys.stdin:
    # add each edge to the dict, O(1) times n loops
    e = line.strip().split()
    origins.append(e[0])
    edges[e[0]] = e[1]
    destinations[e[1]] = 1

# now we have to find our starting point
for o in origins:
    if o not in destinations: # O(1)
        start = o
        break

if start == "":
    raise Exception("Input edges form a cycle")

for i in range(len(origins)):
    dest = edges[start]
    print "{0} {1}".format(start, dest)
    start = dest