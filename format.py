# Josh Lim
# Comp Sci 30 P4
# 01/16/2020
# File to format all the code
import re

# Code adapted from Stack Overflow: Remove spaces and tabs within a string
# in Python
# https://stackoverflow.com/questions/21966556/remove-spaces-and-tabs-within-a
# -string-in-python/21969193


def border(string):
    """Funtion that takes a string, string and removes all spaces and tabs
    and then adds a border before and after the string"""
    border = """
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
""".strip("\n")  # border style
    # strips the inputed string of tabs and new lines
    string = re.sub(r'(^[ \t]+|[ \t]+(?=:))', '', string, flags=re.M)
    formatedString = f"{border}\n{string}\n{border}"  # adds borders
    return formatedString  # returns formatedString
