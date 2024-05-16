# tTxtReSzBtn.py
"""
tTxtReSzBtn.py

A custom QPushButton class that dynamically adjusts its font size to fit the text within the button dimensions.

Classes:
    tTxtReSzBtn -- A QPushButton subclass that resizes text dynamically based on the button's size.

Usage:
    Run this script directly to see a test application demonstrating the tTxtReSzBtn class:
        $ python tTxtReSzBtn.py

Author: Dan Mailman
Date: 15-May-24
"""
from PyQt5.QtWidgets import QPushButton, QApplication
from PyQt5.QtGui import QFont, QImage, QPainter
from PyQt5.QtCore import QRectF, Qt
from sys import argv, exit
# PyQt5 Imports:
# QPushButton: Provides the button widget.
# QApplication: Manages application-wide resources and settings.
# QFont: Represents the font used for rendering text.
# QImage: Used for offscreen image representation.
# QPainter: Provides functions to paint on widgets or images.
# QRectF: Defines a rectangle in floating point precision.
# Qt: Namespace containing flags and enums for various purposes.
# sys.argv: A list of command line arguments passed to the script.
# sys.exit: Exits from Python.

class tTxtReSzBtn(QPushButton):
    """
    tTxtReSzBtn is a custom QPushButton that dynamically adjusts its font size
    to fit the text within the button dimensions.

    Attributes:
        MIN_FONT_SZ (int): The minimum font size.
        MAX_FONT_SZ (int): The maximum font size.
        FONT_NAME (str): The font name.
        PADDING (int): The padding around the text.
    """

    def __init__(self, Txt, min_font_size=4, max_font_size=50, font_name='Arial', padding=10, *args, **kwargs):
        """
        Initializes the tTxtReSzBtn with specified text, font size range, font name, and padding.

        Args:
            Txt (str): The text to display on the button.
            min_font_size (int, optional): The minimum font size. Defaults to 4.
            max_font_size (int, optional): The maximum font size. Defaults to 50.
            font_name (str, optional): The font name. Defaults to 'Arial'.
            padding (int, optional): The padding around the text. Defaults to 10.
        """
        super().__init__(*args, **kwargs)
        self.MIN_FONT_SZ = min_font_size
        self.MAX_FONT_SZ = max_font_size
        self.FONT_NAME = font_name
        self.PADDING = padding
        self.UpdateText(Txt)
        self.setFont(QFont(self.FONT_NAME, self.MIN_FONT_SZ))
        self.CalcFontSz()

    def UpdateText(self, Txt):
        """
        Updates the button text and applies a stylesheet.

        Args:
            Txt (str): The new text to display on the button.
        """
        self.setText(Txt)
        #print(f'UpdateText(): self.text({self.text()})')

    def CalcFontSz(self):
        """
        Calculates and sets the optimal font size for the button text
        based on the button's current dimensions.
        """

        def getBoundingBox(text, font):
            """
            Calculates the bounding box of the text with the given font.

            Args:
                text (str): The text to measure.
                font (QFont): The font to use for measurement.

            Returns:
                QRectF: The bounding box of the text.
            """
            image = QImage(1, 1, QImage.Format_ARGB32)
            painter = QPainter(image)
            painter.setFont(font)
            rect = painter.boundingRect(QRectF(0, 0, float('inf'), float('inf')), Qt.TextWordWrap, text)
            painter.end()
            return rect

        available_width = self.width() - self.PADDING
        available_height = self.height() - self.PADDING

        for font_size in range(self.MIN_FONT_SZ, self.MAX_FONT_SZ + 1):
            font = QFont(self.FONT_NAME, font_size)
            rect = getBoundingBox(self.text(), font)

            if rect.width() > available_width or rect.height() > available_height:
                font_size -= 1  # Use the last fitting size
                break

        # Ensure font size is within bounds
        font_size = max(self.MIN_FONT_SZ, min(self.MAX_FONT_SZ, font_size))
        self.setFont(QFont(self.FONT_NAME, font_size))
        self.update()  # Refresh the widget to apply font size immediately

    def resizeEvent(self, event):
        """
        Recalculates the font size when the button is resized.

        Args:
            event (QResizeEvent): The resize event.
        """
        super().resizeEvent(event)
        self.CalcFontSz()  # Adjust font size when resized

    @staticmethod
    def main():
        """
        The main method to run a test application for the tTxtReSzBtn class.
        """
        app = QApplication(argv)
        sTxt = f"Accordion\nBass_D♯/E♭"
        btn = tTxtReSzBtn(sTxt, min_font_size=8, max_font_size=30, font_name='Times New Roman', padding=20)
        btn.resize(200, 100)  # Set initial size for testing
        btn.show()
        exit(app.exec_())


if __name__ == "__main__":
    tTxtReSzBtn.main()
