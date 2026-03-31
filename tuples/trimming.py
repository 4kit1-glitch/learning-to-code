
def mean(*args):
    return sum(args) / len(args)

def min_max(*args):
    return min(args), max(args)

def trimmed_mean(*args):
    """
    function takes an number of arguements 
    removes the min and max and returns
    the mean of the rest
    """

    min, max = min_max(args)
    arg_list = list(args)
    arg_list.remove(min)
    arg_list.remove(max)
    return mean(arg_list)