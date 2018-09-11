"""This module contains LabelSheet, the base class for sheets of labels."""

import labels
from reportlab.graphics import renderPDF
from reportlab.pdfgen.canvas import Canvas

from .label_formats import DefaultLabelFormat
from .label_sizes import DefaultLabelSize
from .paper_sizes import A4


class LabelSheet:
    """
    Base class for label sheets.

    Contains the necessary information to create a sheet of labels.

    Attributes:
        paper_size:
            The size of paper the labels will be printed on.
            (labeler.PaperSize).
        label_size:
            The size of the labels (labler.LabelSize)
        columns:
            The number of columns of labels per sheet.
        rows:
            The number of rows of labels per sheet.
        left_margin:
            The gap to leave between the left side of the label and the
            padding.
        right_margin:
            The gap to leave between the right side of the label and the
            padding.
        left_padding:
            The gap between the left margin and the text.
        right_padding:
            The gap between the right margin and the text.
        top_padding:
            The gap between the top of the label and the text.
        bottom_padding:
            The gap between the top of the label and the text.
        corner_radius:
            Radius at which to round the corner.
        border:
            Draw the border of the label. Usefull for testing.

    """

    paper_size = A4()
    label_size = DefaultLabelSize()
    label_format = DefaultLabelFormat()
    left_margin = 0
    right_margin = 0
    top_margin = 0
    bottom_margin = 0
    left_padding = 0
    right_padding = 0
    top_padding = 0
    bottom_padding = 0
    corner_radius = 0
    border = False
    columns = 4
    rows = 10

    def __init__(self, **kwargs):
        """
        Create a label format.

        Kwargs:
            paper_size:
                The size of paper the labels will be printed on.
                (labeler.PaperSize).
            label_size:
                The size of the labels (labler.LabelSize)
            columns:
                The number of columns of labels per sheet.
            rows:
                The number of rows of labels per sheet.
            left_margin:
                The gap to leave between the left side of the label and the
                padding.
            right_margin:
                The gap to leave between the right side of the label and the
                padding.
            left_padding:
                The gap between the left margin and the text.
            right_padding:
                The gap between the right margin and the text.
            top_padding:
                The gap between the top of the label and the text.
            bottom_padding:
                The gap between the top of the label and the text.
            corner_radius:
                Radius at which to round the corner.
            border:
                Draw the border of the label. Usefull for testing.

        """
        self.paper_size = kwargs.get("paper_size", self.paper_size)
        self.label_size = kwargs.get("label_size", self.label_size)
        self.label_format = kwargs.get("label_format", self.label_format)
        self.left_margin = kwargs.get("left_margin", self.left_margin)
        self.right_margin = kwargs.get("right_margin", self.right_margin)
        self.top_margin = kwargs.get("top_margin", self.top_margin)
        self.bottom_margin = kwargs.get("bottom_margin", self.bottom_margin)
        self.left_padding = kwargs.get("left_padding", self.left_padding)
        self.right_padding = kwargs.get("right_padding", self.right_padding)
        self.top_padding = kwargs.get("top_padding", self.top_padding)
        self.bottom_padding = kwargs.get("bottom_padding", self.bottom_padding)
        self.corner_radius = kwargs.get("corner_radius", self.corner_radius)
        self.border = kwargs.get("border", self.border)
        self.columns = kwargs.get("columns", self.columns)
        self.rows = kwargs.get("rows", self.rows)

    def generate_PDF_from_data(self, data):
        """Return generated labels as a reportlab.pdfgen.canvas.Canvas."""
        specs = labels.Specification(
            self.paper_size.width,
            self.paper_size.height,
            self.columns,
            self.rows,
            self.label_size.width,
            self.label_size.height,
            left_margin=self.left_margin,
            right_margin=self.right_margin,
            top_margin=self.top_margin,
            bottom_margin=self.bottom_margin,
            left_padding=self.left_padding,
            right_padding=self.right_padding,
            top_padding=self.top_padding,
            bottom_padding=self.bottom_padding,
            corner_radius=self.corner_radius,
        )

        def draw_label(label, width, height, lines):
            label_format = self.label_format(width=width, height=height)
            label_format.make_label(label, lines)

        sheet = labels.Sheet(specs, draw_label, border=self.border)
        for item in data:
            sheet.add_label(item)
        canvas = Canvas(None, pagesize=sheet._pagesize)
        for page in sheet._pages:
            renderPDF.draw(page, canvas, 0, 0)
            canvas.showPage()
        return canvas
