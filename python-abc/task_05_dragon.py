#!/usr/bin/env python3
"""The mystical Dragon: Mastering Mixins"""


class SwimMixin:
    def swim(self):
        print("The Creature swims!")


class FlyMixin:
    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    def roar(self):
        print("The dragon roars!")
