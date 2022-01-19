# Containing two simple feature functions

def feature_1(a=0, b=0):
    """
    Return the sum of the two arguments.

    :param a: first argument.
    :param b: second argument.
    :type a: integer or float or other number
    :type b: integer or float or other number
    :return: the sum a + b
    :rtype: same as the arguments

    """
    return a + b


def feature_2(a=[]):
    """
    Return the length of the argument.

    :param a: argument.
    :type a: list
    :return: length of list
    :rtype: integer

    """
    return len(a)
