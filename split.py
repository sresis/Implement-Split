"""Split a string by splitter and return list of splits.

This should work like the built-in Python .split() method [*].
YOU MAY NOT USE the .split() method in your solution!
YOU MAY NOT USE regular expressions in your solution!

For example:

    >>> split("i love balloonicorn", " ")
    ['i', 'love', 'balloonicorn']

    >>> split("that is which is that which is that", " that ")
    ['that is which is', 'which is that']

    >>> split("that is which is that which is that", "that")
    ['', ' is which is ', ' which is ', '']

    >>> split("hello world", "nope")
    ['hello world']

* Note: the actual Python split method has special behavior
  when it is not passed anything for the splitter -- you do
  not need to implement that.

"""


def split(astring, splitter):
    """Split a string by splitter and return list of splits."""
    # if :len(n) equals the splitter
    # find indexes of splitter
    splitter_idx = []
    i = 0
    while i < len(astring) - len(splitter) + 1:
        if astring[i:(i + len(splitter))] == splitter:
            splitter_idx.append(i)
        i += 1
    # take everything before each split index
    i = 0
    start_val = 0
    final_list = []
    for i in splitter_idx:
        final_list.append(astring[start_val:i])
        start_val = i + len(splitter)
    final_list.append(astring[start_val:])
    return final_list


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. FINE SPLITTING!\n")
