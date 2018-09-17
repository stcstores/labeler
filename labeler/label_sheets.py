"""This module contains preset label sheets."""

from . import paper_sizes
from .label_sheet import LabelSheet
from .label_size import LabelSize
from .paper_size import PaperSize


class STW046025PO(LabelSheet):
    """Label sheet preset for STW046025PO label paper."""

    paper_size = paper_sizes.A4
    label_size = LabelSize(width=45, height=25)
    columns = 4
    rows = 10
    left_margin = 9
    right_margin = 9
    top_margin = 21
    bottom_margin = 21
    corner_radius = 2
    left_padding = 0
    right_padding = 0
    padding_top = 0
    padding_bottom = 0


class ThermalAddressLabel4x6Sheet(LabelSheet):
    """Label sheet preset for 4x6 thermal address labels."""

    paper_size = PaperSize(width=152, height=101)
    label_size = LabelSize(width=152, height=101)
    columns = 1
    rows = 1
    left_margin = 0
    right_margin = 0
    top_margin = 0
    bottom_margin = 0
    corner_radius = 2
    left_padding = 0
    right_padding = 0
    padding_top = 0
    padding_bottom = 0
