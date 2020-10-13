import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    """ "Rotate" a list to the left. (Items on the left end up at the end of the list.)

    Args:
        a (array): python array
        d (int): number of rotations

    Returns:
        [array]: new rotated list
    """

    return a[d:len(a)] + a[:d]

if __name__ == "__main__":
    a = list(range(1, 25, 2))
    print("Original list:", a, "\nRotated list:", rotLeft(a, 5))
