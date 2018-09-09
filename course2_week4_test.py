"""
Week 4 practice project template for Python Data Representation
Update syntax for print in CodeSkulptor Docs
from "print ..." syntax in Python 2 to "print(...)" syntax for Python 3
"""

# HTML tags that bounds example code
PREFIX = "<pre class='cm'>"
POSTFIX = "</pre>"
PRINT = "print"


def update_line(line):
    """
    Takes a string line representing a single line of code
    and returns a string with print updated
    """

    # Strip left white space using built-in string method lstrip()
    stripline = line.lstrip()

    # If line is print statement,  use the format() method to add insert parentheses
    if stripline[:len(PRINT)] == PRINT:
        spaces = ' ' * line.find(PRINT)
        content = stripline[len(PRINT) + 1:]
        # print(len(spaces))
        return '{}print({})'.format(spaces, content)
    else:
        return line

    # Note that solution does not handle white space/comments after print statememt


# Some simple tests
# print(update_line(""))
# print(update_line("foobar()"))
# print(update_line("print 1 + 1"))
print(update_line("    print 2, 3, 4"))

# Expect output
##
##foobar()
##print(1 + 1)
##    print(2, 3, 4)

# def update_pre_block(pre_block):
#     """
#     Take a string that correspond to a <pre> block in html and parses it into lines.
#     Returns string corresponding to updated <pre> block with each line
#     updated via process_line()
#     """
#
#     # parse_line = pre_block.splitlines()
#     #
#     # for i in parse_line:
#     #     ans = update_line(i)
#     #
#     #     return ans
#
#     lines = pre_block.split("\n")
#     updated_block = update_line(lines[0])
#     for line in lines[1:]:
#         updated_block += "\n"
#         updated_block += update_line(line)
#     return updated_block
#
# # Some simple tests
# print(update_pre_block(""))
# print(update_pre_block("foobar()"))
# print(update_pre_block("if foo():\n    bar()"))
# print(update_pre_block("print\nprint 1+1\nprint 2, 3, 4"))
# print(update_pre_block("    print a + b\n    print 23 * 34\n        print 1234"))

# Expected output
##
##foobar()
##if foo():
##    bar()
##print()
##print(1+1)
##print(2, 3, 4)
##    print(a + b)
##    print(23 * 34)
##        print(1234)
