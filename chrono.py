# inps = map(int, raw_input().split())
# count = 0
# line = raw_input()
# template = raw_input()

# def match(template, inp):
#     for i, char in enumerate(template):
#         if (char != "*") and (inp[i] != char):
#             return False
#     return True

# for i in range(len(line)-3):
#     if match(template, line[i:i+4]):
#         count += 1

# print count

import collections
import re
patients = collections.OrderedDict()
# this way patients.keys() returns names in order read

def select_name(vals):
    # returns highest-order name as string
    
    maxn = ("", -1)
    for name in vals:
        order = len(name.split())

        if '.' in name:
            order -= len(re.findall('\.',name))*0.3

        if ',' in name:
            name = ' '.join(name.split(',')[::-1]).strip()

        if order > maxn[1]:
            maxn = (name, order)

    return maxn[0]


for i in range(int(raw_input())):
    l = raw_input().split(':')

    if l[1] in patients:
        patients[l[1]] = list(patients[l[1]]+[l[0]])
    else:
        patients[l[1]] = [l[0]]
        
for key in patients.keys():
    vals = patients[key]
    print "{0}:{1}".format(select_name(vals), key)

