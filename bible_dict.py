# Dictionary of available Bible versions from API at https://github.com/wldeh/bible-api
# Format: Key is bible ID:[bible Name, Font to use, bible API code]
# There are many to choose from, visit the API web site for more info.
# Feel free to add or delete from this dictionary, using the format presented.

bible_versions = {
    "ASV": ["American Standard Version", "FreeSerif", "en-asv"],
    "KJV": ["King James Version", "FreeSerif", "en-kjv"],
    "LSV": ["Literal Standard Version", "FreeSerif","en-lsv"],
    "KJVCPB": ["The Cambridge Paragraph Bible", "FreeSerif","en-US-kjvcpb"],
    "RV": ["Revision of the King James Version", "FreeSerif","en-rv"],
    "LXXUP": ["Brenton English Septuagint", "FreeSerif","en-US-lxxup"],
    "FBV": ["Free Bible Version", "FreeSerif","en-fbv"],
    "BSB": ["Berean Study Bible", "FreeSerif","en-bsb"],
    "WEB": ["World English Bible", "FreeSerif","en-web"],
    "T4T": ["Translation for Translators", "FreeSerif","en-t4t"],
    "DRA": ["Duay-Rheims American Edition", "FreeSerif","en-dra"]
}

"""
A few available fonts on RPi to choose from. You may need to change the size in config.py to properly fit
Z003
C059 Italic
Cantarell Italic
FreeSerif Italic
Liberation Mono Italic
Liberation Serif Italic
Nimbus Roman Italic
P052 Roman
URW Bookman Light Italic
Verdana
Times New Roman
Garamond
"""
