# Josh Lim
# Comp Sci 30 P4
# 01/16/2020
# File to format all the code
import re


def border(string):
    border = """
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
""".strip("\n")
    string = re.sub(r'(^[ \t]+|[ \t]+(?=:))', '', string, flags=re.M)
    formatedString = f"{border}\n{string}\n{border}"
    return formatedString
