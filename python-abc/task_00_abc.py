#!/usr/bin/env python3
"""abstract animal Class and Subclasses."""

from abc import ABC , abstractmethod


class Animal(ABC):
    """Abstract base class representing an animal."""

    @abstractmethod
    def sound(self):
        """Abstract method that must be implemented by subclasses."""
        pass


class Dog(Animal):
    """Dog class implementing the sound method."""

    def sound(self):
        return"Bark"

class Cat(Animal):
    """Cat class implementing the sound method."""

    def sound(self):
        return "Meow"
