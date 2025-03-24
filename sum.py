def divide(x,y):
    """
    precondition y should not be 0
    """
    assert(y!=0)
    s=x/y
    assert(s>0 or s<0)
    return s