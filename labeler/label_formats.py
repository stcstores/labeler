"""This module contains preset label formats."""

from reportlab.graphics import shapes
from reportlab.graphics.barcode import eanbc

from .label_format import LabelFormat


class DefaultLabelFormat(LabelFormat):
    """Labeler's default label format."""

    font = 'Helvetica-Bold'
    vertical_margin = 10
    horizontal_margin = 5
    max_font_size = 18

    def get_text_height(self):
        """Return the height of the text in ponts."""
        return int((self.height / 100) * 16)

    def get_horizontal_location(self):
        """Return the horizontal position of the text in ponts."""
        return self.width / 2

    @staticmethod
    def wrap(text, line_length):
        """Wrap the text if necessary."""
        if line_length < len(text):
            return [text]
        split_index = text[:line_length].rfind(' ')
        return [text[:split_index], text[split_index:]]


class BarcodeLabelFormat(DefaultLabelFormat):
    """A label format for barcodes."""

    def make_label(self, label, lines):
        """Add text to label."""
        text = lines[1]
        vertical_location = 15
        for line in self.wrap(text, 30):
            label.add(
                shapes.String(
                    self.get_horizontal_location(),
                    vertical_location,
                    line,
                    fontSize=8,
                    fontName=self.font,
                    textAnchor=self.text_anchor))
            vertical_location -= 10
        x_location = 15
        y_location = 25
        widget_class = eanbc.Ean13BarcodeWidget
        barcode = lines[0]
        bar_height = self.height * 0.5
        barcode_drawing = widget_class(
            barcode, x=x_location, y=y_location, barHeight=bar_height)
        label.add(barcode_drawing)
