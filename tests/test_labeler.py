from pathlib import Path

import labeler
from labeler import __version__


def test_version_file_attributes():
    assert hasattr(__version__, "__title__")
    assert hasattr(__version__, "__description__")
    assert hasattr(__version__, "__url__")
    assert hasattr(__version__, "__version__")
    assert hasattr(__version__, "__author__")
    assert hasattr(__version__, "__author_email__")
    assert hasattr(__version__, "__license__")
    assert hasattr(__version__, "__copyright__")


def test_default_format(tmpdir):
    data = [
        ["UK 12", "Pink Cat Slipper", "FW987"],
        ['38" Regular Tall', "Grey Shoulders, Blue Body", "45632"],
        ["Medium", "Grey", "64535"],
        ["UK 12", "Pink Cat Slipper", "FW987"],
        ['38" Regular Tall', "Grey Shoulders, Blue Body", "45632"],
        ["Medium", "Grey", "64535"],
        ['38" Regular Tall', "Grey Shoulders, Blue Body", "45632"],
        ["Medium", "Grey", "64535"],
    ]

    label_format = labeler.DefaultLabelFormat
    sheet = labeler.STW046025PO(label_format=label_format)
    canvas = sheet.generate_PDF_from_data(data)
    canvas._filename = str(Path(tmpdir / "test.pdf"))
    canvas.save()


def test_address_label_format(tmpdir):
    data = [
        ["UK 12", "Pink Cat Slipper", "FW987"],
        ['38" Regular Tall', "Grey Shoulders, Blue Body", "45632"],
        ["Medium", "Grey", "64535"],
        ["UK 12", "Pink Cat Slipper", "FW987"],
        ['38" Regular Tall', "Grey Shoulders, Blue Body", "45632"],
        ["Medium", "Grey", "64535"],
        ['38" Regular Tall', "Grey Shoulders, Blue Body", "45632"],
        ["Medium", "Grey", "64535"],
        [
            '38" Regular Tall',
            "Grey Shoulders, Blue Body",
            "45632",
            "more words",
            "and some more",
            "and more",
            "and more",
        ],
        ["86759", "PAW PATROL SKYE"],
    ]

    label_format = labeler.AddressLabelFormat
    sheet = labeler.ThermalAddressLabel4x6Sheet(label_format=label_format)
    canvas = sheet.generate_PDF_from_data(data)
    canvas._filename = str(Path(tmpdir / "test.pdf"))
    canvas.save()


def test_small_label_format(tmpdir):
    data = [
        ["UK 12", "Pink Cat Slipper", "FW987"],
        ['38" Regular Tall', "Grey Shoulders, Blue Body", "45632"],
        ["Medium", "Grey", "64535"],
        ["UK 12", "Pink Cat Slipper", "FW987"],
        ['38" Regular Tall', "Grey Shoulders, Blue Body", "45632"],
        ["Medium", "Grey", "64535"],
        ['38" Regular Tall', "Grey Shoulders, Blue Body", "45632"],
        ["Medium", "Grey", "64535"],
        [
            '38" Regular Tall',
            "Grey Shoulders, Blue Body",
            "45632",
            "more words",
            "and some more",
            "and more",
            "and more",
        ],
        ["86759", "PAW PATROL SKYE"],
    ]

    label_format = labeler.SmallLabelFormat
    sheet = labeler.STW046025PO(label_format=label_format)
    canvas = sheet.generate_PDF_from_data(data)
    canvas._filename = str(Path(tmpdir / "test.pdf"))
    canvas.save()
