################################################################################
#     ____                          __     _                          _____
#    / __ \  __  __  ___    _____  / /_   (_)  ____    ____          |__  /
#   / / / / / / / / / _ \  / ___/ / __/  / /  / __ \  / __ \          /_ <
#  / /_/ / / /_/ / /  __/ (__  ) / /_   / /  / /_/ / / / / /        ___/ /
#  \___\_\ \__,_/  \___/ /____/  \__/  /_/   \____/ /_/ /_/        /____/
#
#  Question 3
################################################################################
#
# Instructions:
# Make a Python class for a magical oven that can combine ingredients at
# different temperatures to craft special materials.
#
# The oven class should have the methods:
# - add(item) to add an oven to be combined
# - freeze() to freeze the ingredients
# - boil() to boil the ingredients
# - wait() to combine the ingredients with no change in temperature
# - get_output() to get the result
#
# You will need to change the `make_oven()` function to return a new instance
# of your oven.
#
# The `alchemy_combine()` function will use your oven. You can see the expected
# formulas and their outputs in the test file, `question3_test.py`.

from typing import Dict, FrozenSet, List, Set, Tuple, Union

# a hashmap that maps a tuple of ingredients and oven status to an output
# useful for simplifying conditional logic
RECIPES = {
    (frozenset(["lead", "mercury"]), "boiling"): "gold",
    (frozenset(["water", "air"]), "freezing"): "snow",
    (frozenset(["cheese", "dough", "tomato"]), "boiling"): "pizza",
}


class MagicalOven:
    def __init__(
        self,
        recipes: Dict[Tuple[FrozenSet, str], str],
        items: Union[List[str], None] = None,
    ):
        # we assume ingredients are unique, and we use a set to get faster lookup
        if items is not None:
            self.ingredients = set(items)
        self.ingredients: Set[str] = set()

        self.oven_status: str = "waiting"
        self.recipes: Dict[Tuple[FrozenSet, str], str] = recipes

    def add(self, item):
        self.ingredients.add(item)

    def freeze(self):
        self.oven_status = "freezing"

    def boil(self):
        self.oven_status = "boiling"

    def wait(self):
        self.oven_status = "waiting"

    def get_output(self):
        ouput = self.recipes.get(
            (frozenset(self.ingredients), self.oven_status), "unknown"
        )
        return ouput


# This function should return an oven instance!
def make_oven() -> MagicalOven:
    return MagicalOven(recipes=RECIPES)


def alchemy_combine(oven, ingredients, temperature):
    for item in ingredients:
        oven.add(item)

    if temperature < 0:
        oven.freeze()
    elif temperature >= 100:
        oven.boil()
    else:
        oven.wait()

    return oven.get_output()
