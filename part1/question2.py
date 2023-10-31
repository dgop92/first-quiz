################################################################################
#     ____                          __     _                          ___
#    / __ \  __  __  ___    _____  / /_   (_)  ____    ____          |__ \
#   / / / / / / / / / _ \  / ___/ / __/  / /  / __ \  / __ \         __/ /
#  / /_/ / / /_/ / /  __/ (__  ) / /_   / /  / /_/ / / / / /        / __/
#  \___\_\ \__,_/  \___/ /____/  \__/  /_/   \____/ /_/ /_/        /____/
#
#  Question 2
################################################################################
#
# Instructions:
# Write a function that will swap a tuple of two items. For example, the function
# should change (x, y) into (y, x).
# Assign the function to `swapper` so that the function `run_swapper(..)` can use
# it. As always, there is a test suite that checks the result. It is in
# `question2_test.py.`

from typing import Any, Tuple


def swapper(tuple_of_two: Tuple[Any, Any]):
    # We need to create a new tuple because tuples are immutable
    x, y = tuple_of_two
    return (y, x)


def run_swapper(list_of_tuples):
    return list(map(swapper, list_of_tuples))
