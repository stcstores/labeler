"""This module contains the LabelSize class, the base class for label sizes."""


class LabelSize:
    """
    Contains information about the size of a label.

    Attributes:
        width:
            The width of the label.
        height:
            The height of the label.

    """

    width = 0
    height = 0

    def __init__(self, **kwargs):
        """
        Create a label size.

        Kwargs:
            width:
                The width of the label.
            height:
                The height of the label.

        """
        self.width = kwargs.get("width", self.width)
        self.height = kwargs.get("height", self.height)
