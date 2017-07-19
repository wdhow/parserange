# Parse a comma delimited and hyphenated number range and return a list of
# numbers that qualify.
#
# eg:
#     input: '1, 2, 3, 4, 40-45, 50'
#'    output: [1, 2, 3, 4, 40, 41, 42, 43, 44, 45, 50]
#
def parserange(seq):
    import re
    import itertools

    seq = seq.split(',')
    acc = []
    for i in seq:
        m = re.match(' *(?P<start>\d+) *(- *(?P<end>\d+))? *', i)
        if m != None:
            a = [m.group('start'), m.group('end')]
            a = [int(x) for x in a if x != None]

            if len(a) > 1:
                a = range(int(a[0]), int(a[1]+1))

            acc.append(a)

    num_range = list(set([x for x in list(itertools.chain.from_iterable(acc)) if x != None]))
    return num_range