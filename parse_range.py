import re
import itertools


def parse_range(seq: str) -> list[int]:
    """Parse a comma delimited and hyphenated integer range and return a list of
    numbers that qualify.

    Example:
        parse_range("1, 2, 3, 4, 40-45, 50")
        [1, 2, 3, 4, 40, 41, 42, 43, 44, 45, 50]

    Args:
        seq (str): String containing comma delimited and/or hyphenated number ranges.

    Returns:
        list[int]: Individual integers extracted from the given `seq`.

    """
    seq = seq.split(",")
    acc = []
    for i in seq:
        m = re.match(r" *(?P<start>\d+) *(- *(?P<end>\d+))? *", i)

        if not m:
            continue

        a = [m.group("start"), m.group("end")]
        a = [int(x) for x in a if x]

        if len(a) > 1:
            a = range(int(a[0]), int(a[1] + 1))

        acc.append(a)

    return list(
        set([x for x in list(itertools.chain.from_iterable(acc)) if x])
    )
