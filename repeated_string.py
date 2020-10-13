import math
import os
import random
import re
import sys

# - 13 letters from 'abcac' would be abcac abcac abc
# then it would be the number of times 'a' appears in the original list multiplied by n // len(list) + how many times 'a' appears in a partial list given by n % len/list

# Example: modulo and remainder for example string
s = "abcac"
n = 13

# length of the string
print("Length of s: ", len(s))

# calculations to show how to get to n when n // len(s) different than 0 (ex n=13)
print("How many full s string go in the substring n: ", n//len(s), "string would be: ", s*(n//len(s)))
print("Remainder from modulo: ", n%len(s), "string would be the number of characters from s on the outside: ", s[:n%len(s)])

# there are 10 characters in the substring (n=13)
print("Substring full: ", s * (n // len(s)) + s[:n%len(s)])

# find the "a" in the original string
print("Number of letter a in the original string: ", s.count("a"))

# how many times it would appear in the substring
print("Number of a's in the substring n:", (s.count("a") * (n // len(s)) + s[:n % len(s)].count("a")))

# Complete the repeatedString function below.
def repeatedString(s, n):
    """ Count the number of appearances of character "a" in a substring of s to repeat n characters from.

    Args:
        s (string): string to repeat
        n (int): the number of characters to consider

    Returns:
        int: the number of letter "a" in the first n letters of the infinite string 
    """

    return s.count("a") * (n // len(s)) + s[:n % len(s)].count("a")


if __name__ == "__main__":
    s = "epsxyyflvrrrxzvnoenvpegvuonodjoxfwdmcvwctmekpsnamchznsoxaklzjgrqruyzavshfbmuhdwwmpbkwcuomqhiyvuztwvq"
    n = 549382313570

    # expected output should be 16481469408
    print(repeatedString(s, n))
