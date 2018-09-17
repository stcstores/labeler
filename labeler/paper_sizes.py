"""This module contains preset paper sizes."""

from .paper_size import PaperSize


class A4(PaperSize):
    """PaperSize for A4 paper."""

    width = 210
    height = 297


class Thermal6x4Paper(PaperSize):
    """Paper size for 6x4 inch thermal address labels."""

    width = 152.4
    height = 101.6
