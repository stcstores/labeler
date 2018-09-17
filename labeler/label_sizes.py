"""This module contains preset label sizes."""

from .label_size import LabelSize


class DefaultLabelSize(LabelSize):
    """The default label size."""

    width = 45.7
    height = 25.4


class Thermal6x4Label(LabelSize):
    """Label size for 6x4 inch thermal address labels."""

    width = 152.4
    height = 101.6
