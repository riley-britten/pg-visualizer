def parse_table(s):
    """
    Takes a Cayley table as a string formatted as in GAP and
    returns the Cayley table as an array of arrays of ints.
    This will generally involve relabeling elements.
    """ 
    # Remove whitespace
    s = ''.join(s.split())

    # Split into rows
    s = s.split("],")

    for i in range(len(s)):
        s[i] = s[i].strip("[]")
        s[i] = s[i].split(",")

    # Create a dictionary relabeling elements of the magma
    relabel = {}
    for i in range(len(s[0])):
        relabel[s[0][i]] = i

    for i in range(len(s)):
        for j in range(len(s[i])):
            s[i][j] = relabel[s[i][j]]
    return s
