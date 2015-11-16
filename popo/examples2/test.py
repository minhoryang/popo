from enum import Enum


class Major(object):
    """majorrrrr."""
    name = ""


class Target(object):
    """Let's go!"""
    name = ""
    score = 0.0
    major = Major
    minor = ""


class Cases(Enum):
    a = 1
    b = 2
