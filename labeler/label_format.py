"""This module contains the LabelFormat class."""

from reportlab.graphics import shapes
from reportlab.pdfbase.pdfmetrics import stringWidth


class LabelFormat:
    """
    Base class for label formats.

    Contains the necessary information render text onto a single label.

    Takes the size and margin size for a label, along with one or more lines
    of text and renders the label with the text fitting between the margins.

    Attributes:
        font:
            The name of the font to use for label text.
        width:
            The width of the label in points.
        height:
            The hight of the label in points.
        lines:
            List of strings where each string is a line of text to render on
            the label.
        vertical_margin:
            The gap to leave between the top and bottom of the label and the
            text in points.
        horizontal_margin:
            The gap to leave between the sides of the label and the text in
            points.
        max_font_size:
            The largest font size to use when fitting text. If this is 0 the
            font size will be the largest that can fit.

    """

    font = None
    width = 0
    height = 0
    vertical_margin = 0
    horizontal_margin = 0
    max_font_size = 0
    text_anchor = 'middle'

    def __init__(self, **kwargs):
        """
        Create new Label Format.

        Kwargs:
            font:
                The name of the font to use for label text.
            width:
                The width of the label in points.
            height:
                The hight of the label in points.
            lines:
                List of strings where each string is a line of text to render
                on the label.
            vertical_margin:
                The gap to leave between the top and bottom of the label and
                the text in points.
            horizontal_margin:
                The gap to leave between the sides of the label and the text in
                points.
            max_font_size:
                The largest font size to use when fitting text. If this is 0
                the font size will be the largest that can fit.

        """
        self.font = kwargs.get('font', self.font)
        self.width = kwargs.get('width', self.width)
        self.height = kwargs.get('height', self.height)
        self.vertical_margin = kwargs.get(
            'vertical_margin', self.vertical_margin)
        self.horizontal_margin = kwargs.get(
            'horizontal_margin', self.horizontal_margin)
        self.max_font_size = kwargs.get('max_font_size', self.max_font_size)
        self.text_anchor = kwargs.get('text_anchor', self.text_anchor)

    def get_text_height(self):
        """
        Return the height of the text.

        Sub-classes must implement this to set the height of the text.
        """
        raise NotImplementedError

    def get_horizontal_location(self):
        """
        Return the horiziontal location of the text.

        Sub-classes must implement this to set the horizontal location of the
        text.
        """
        raise NotImplementedError

    def get_usable_height(self):
        """Return the maximum gap between the top and bottom margins."""
        return self.height - (self.vertical_margin * 2)

    def get_usable_width(self):
        """Return the maximum gap between the left and right margins."""
        return self.width - (self.horizontal_margin * 2)

    def get_line_gap(self, lines):
        """Return the gap between each line of text."""
        return self.get_usable_height() - (self.get_text_height() * len(lines))

    def calculate_max_font_size(self, text):
        """Return the maximum size of text that can fit on the label."""
        font_size = self.max_font_size
        string_width = stringWidth(text, self.font, font_size)
        while string_width > self.get_usable_width():
            font_size *= 0.8
            string_width = stringWidth(text, self.font, font_size)
        return font_size

    def make_label(self, label, lines):
        """
        Add text to label.

        Args:
            label:
                reportlab.graphics.shapes.Drawing object to use as label.
            lines:
                List containing each line of text as a string.

        """
        horizontal_location = self.get_horizontal_location()
        vertical_location = self.vertical_margin
        for line in reversed(lines):
            font_size = self.calculate_max_font_size(line)
            label.add(
                shapes.String(
                    horizontal_location,
                    vertical_location,
                    line,
                    fontSize=font_size,
                    fontName=self.font,
                    textAnchor=self.text_anchor))
            vertical_location = vertical_location + self.get_line_gap(lines)
