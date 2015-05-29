import re


def strip_internal_comments(text):
    """Removes internal comments from a string and normalizes whitespace
    around them.

    Comments are in the format [[comment]]. For example, the string 'Lorem
    ispum [[dolor sit]] amet.' will be transformed to 'Lorem ipsum amet.'
    Further examples: https://www.regex101.com/r/eN0iR4/2
    """

    return re.sub(pattern=r'(\s)?\[\[.*\]\](\s)?', repl=' ', string=text)
