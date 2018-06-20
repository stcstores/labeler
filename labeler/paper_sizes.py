"""This module contains preset paper sizes."""

from .paper_size import PaperSize


class A4(PaperSize):
    """PaperSize for A4 paper."""

    width = 210
    height = 297
