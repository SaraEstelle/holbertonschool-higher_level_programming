#!/usr/bin/env python3
"""The mystical Dragon: Mastering Mixins"""


class SwimMixin:
    """Mixin class to add swimming capability."""
    def swim(self):
        """Print a message indicating that the creature swims."""
        print("The Creature swims!")


class FlyMixin:
    """Mixin class to add flying capability."""
    def fly(self):
        """Print a message indicating that the creature flies."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Class representing a Dragon, which can both swim and fly."""
    def roar(self):
        """Print a message indicating that the dragon roars."""
        print("The dragon roars!")
