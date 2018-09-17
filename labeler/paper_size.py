"""This module contains the PaperSize class, the base class for paper sizes."""


class PaperSize:
    """
    Contains information about the size prining paper.

    Attributes:
        width:
            The width of the label.
        height:
            The height of the label.

    """

    width = 210
    height = 297

    def __init__(self, **kwargs):
        """
        Create a paper size.

        Kwargs:
            width:
                The width of the label.
            height:
                The height of the label.

        """
        self.width = kwargs.get("width", self.width)
        self.height = kwargs.get("height", self.height)
