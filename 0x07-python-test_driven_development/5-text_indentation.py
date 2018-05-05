#!/usr/bin/python3
"""

    Module with one method: text_indentation(text)

"""


def text_indentation(text):
    """
        Print text with two newlines between each punctuation and colon
        If text is not str, raise error
    """
    if text is None or not isinstance(text, str):
        raise TypeError("text must be a string")
    t = text.replace('.', '.\n\n').replace('?', '?\n\n').replace(':', ':\n\n')
    line = []
    for s in t.split("\n"):
        line.append(s.lstrip())
    print("\n".join(line))
