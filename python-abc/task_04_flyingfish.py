#!/usr/bin/env python3
"""Module for Fish, Bird and FlyingFish classes"""


class Fish:
    """Fish class with swim and habitat methods"""

    def swim(self):
        """Prints swimming message"""
        print("The fish is swimming")

    def habitat(self):
        """Prints habitat message"""
        print("The fish lives in water")


class Bird:
    """Bird class with fly and habitat methods"""

    def fly(self):
        """Prints flying message"""
        print("The bird is flying")

    def habitat(self):
        """Prints habitat message"""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """FlyingFish class that inherits from both Fish and Bird"""

    def swim(self):
        """Prints swimming message"""
        print("The flying fish is swimming!")

    def fly(self):
        """Prints flying message"""
        print("The flying fish is soaring!")

    def habitat(self):
        """Prints habitat message"""
        print("The flying fish lives both in water and the sky!")
