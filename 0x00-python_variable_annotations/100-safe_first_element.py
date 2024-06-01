#!/usr/bin/env python3

"""
    Task: Augument the following code with the correct duck-typed annotations
"""

import typing


# The types of the elements of the input are not know
def safe_first_element(lst: typing.Sequence[typing.Any]) -> \
        typing.Union[typing.Any, None]:
    """Implemented the right duck-typed annotations"""
    if lst:
        return lst[0]
    else:
        return None
