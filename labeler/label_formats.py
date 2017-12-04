from reportlab.graphics.barcode import eanbc

from .label_format import LabelFormat


class DefaultLabelFormat(LabelFormat):
    font = 'Helvetica-Bold'
    vertical_margin = 10
    horizontal_margin = 5
    max_font_size = 18

    def get_text_height(self):
        return int((self.height / 100) * 16)

    def get_horizontal_location(self):
        return self.width / 2


class BarcodeLabelFormat(DefaultLabelFormat):

    def make_label(self, label, lines):
        x_location = 15
        y_location = 20
        widget_class = eanbc.Ean13BarcodeWidget
        barcode = lines[0]
        bar_height = self.height * 0.7
        barcode_drawing = widget_class(
            barcode, x=x_location, y=y_location,
            barHeight=bar_height)
        label.add(barcode_drawing)
