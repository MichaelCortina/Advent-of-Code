def to_int(file):
    """converts .txt file to integer array

    Args:
        file (string): relative filepath of target
    """
    with open(file) as f:
        contents = f.read()
    return [int(s) for s in contents.split()]

def group(lst, n):
    """groups list into tuples

    Args:
        lst (list):
        n (int): num of vars in each tuple

    Yields:
        tuple: sequence of tuples which can be cast to a list
    """
    for i in range(0, len(lst), n):
        val = lst[i:i+n]
        yield tuple(val)