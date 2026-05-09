#!/usr/bin/env python3
"""Module for SwimMixin, FlyMixin and Dragon classes"""


class SwimMixin:
    """Mixin class that provides swimming ability"""

    def swim(self):
        """Prints swimming message"""
        print("The creature swims!")


class FlyMixin:
    """Mixin class that provides flying ability"""

    def fly(self):
        """Prints flying message"""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon class that inherits from SwimMixin and FlyMixin"""

    def roar(self):
        """Prints roaring message"""
        print("The dragon roars!")
