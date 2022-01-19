# a small main programme
# use features.py
# use classes.py
import sys
import features


def main():
    """
    Executes the features 1 and 2.
    Using feature 1 to get sum of the two first given arguments

    :param argv: any number of actual arguments

    :type argv: list of arguments, the first being the actual execute command

    :return: None

    """
    arg = sys.argv
    length = features.feature_2(arg)
    if length == 2:
        s = features.feature_1(a=int(arg[1]))
    elif length > 2:
        s = features.feature_1(a=int(arg[1]), b=int(arg[2]))
    else:
        s = features.feature_1()

    print('number of arguments {n}'.format(n=length))
    print('sum of two first arguments {sum}'.format(sum=s))


if __name__ == '__main__':
    main()
