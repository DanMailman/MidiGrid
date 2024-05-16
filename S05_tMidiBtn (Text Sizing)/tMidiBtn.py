"""
tMidiBtn.py
Dan Mailman
13-May-24

Description:
    This module defines the tMidiBtn class, which extends QPushButton from PyQt5.
    It is designed to represent a MIDI controller button that interacts with a MIDI player.
    Each button is associated with a specific musical instrument and note, and is styled
    with dynamic colors based on predefined settings.

Dependencies:
    PyQt5: Used for the GUI components.
    tMidiPlayer: A custom class handling MIDI playback functionalities.
    ClrUtils: Utilities for color manipulation including getting contrastive text colors.
    Utilities: Contains helper functions like ExitOnNoIntVal and ExitOnNoRGBVal for input validation.
    kNamClr, kNote, kInstr: Modules containing constants and mappings for colors, notes, and instruments.

Usage:
    This class is intended to be used in a graphical MIDI control application where each button triggers
    a specific note of an instrument. To test the button, run this module directly, and a GUI window
    with a functioning MIDI button will appear.

Example:
    >>> from tMidiPlayer import tMidiPlayer
    >>> btn = tMidiBtn(tMidiPlayer(), 'Red', 'Accordion', 'Bass_D♯/E♭')
    >>> btn.show()

Notes:
    - Ensure all dependencies are properly installed and available in your Python environment.
    - This module is part of a larger application that requires a graphical environment to run.
"""
# Operating System Interface
from sys import argv, exit  # Access command-line arguments and terminate program

# GUI components
from PyQt5.QtWidgets import QPushButton, QApplication  # Button and Application Widgets
from PyQt5.QtCore import Qt  # Qt constants
from PyQt5.QtGui import QFont, QFontMetrics  # Font handling

# Custom module imports for MIDI functionality
from tMidiPlayer import tMidiPlayer  # Custom class for handling MIDI player functionalities
from tMidiBtnDlg import tMidiBtnDlg

# Utility module imports for color and validation handling
from ClrUtils import get_contrastive_text_color, GetHexStr  # Color utilities
from Utilities import ExitOnNoIntVal, ExitOnNoRGBVal  # Input validation utilities

# Constant module imports for predefined values
from kNamClr import COLOR_RGBS  # Predefined color RGB values
from kNote import NOTE_NUMS  # Predefined note numbers
from kInstr import INSTR_NUMS  # Predefined instrument numbers

class tMidiBtn(QPushButton):
    MAX_FONT_SZ = 50  # Define the maximum font size
    MIN_FONT_SZ =  4  # Define the minimum font size
    def __init__(self, oMidiPlayer: tMidiPlayer, sNamClr: str, sInstr: str, sNote: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.oMidiPlayer = oMidiPlayer
        self.Instr, self.Note = None, None
        self.Update(sNamClr, sInstr, sNote)
        self.setFont(QFont('Arial', self.MIN_FONT_SZ))
        self.CalcFontSz()
    def Update(self, sNamClr, sInstr, sNote):
        nInstr = ExitOnNoIntVal(sInstr, INSTR_NUMS, 'Instrument')
        nNote = ExitOnNoIntVal(sNote, NOTE_NUMS, 'Note')
        color = ExitOnNoRGBVal(sNamClr, COLOR_RGBS, 'Color')
        text_color = get_contrastive_text_color(color)
        self.setObjectName("tMidiButton")  # Set a unique object name
        self.setStyleSheet(f"""QPushButton#tMidiButton {{
                            background-color: {GetHexStr(color)};
                            color: {text_color};
                            text-align: center;
                            padding: 4px;}}""")
        self.setText(f"{sInstr}\n{sNote}")
        self.Instr = nInstr
        self.Note = nNote
    def xCalcFontSz(self):
        test_fit = self.MIN_FONT_SZ
        font = QFont('Arial', test_fit)
        metrics = QFontMetrics(font)
        text_width = metrics.horizontalAdvance(self.text())
        text_height = metrics.height()

        print(f"Initial test_fit: {test_fit}, text_width: {text_width}, text_height: {text_height}, "
              f"button_width: {self.width()}, button_height: {self.height()}")
        # Incrementally increase font size until it doesn't fit
        while text_width <= self.width() and text_height <= self.height() and test_fit < self.MAX_FONT_SZ:
            test_fit += 1
            font = QFont('Arial', test_fit)
            metrics = QFontMetrics(font)
            text_width = metrics.horizontalAdvance(self.text())
            text_height = metrics.height()

            print(f"Testing test_fit: {test_fit}, text_width: {text_width}, text_height: {text_height},"
                  f" button_width: {self.width()}, button_height: {self.height()}")
        # Decrement font size by 1 to ensure it fits within the dimensions
        test_fit -= 1
        print(f"Final test_fit: {test_fit}")
        self.setFont(QFont('Arial', test_fit))
        self.update()  # Refresh the widget to apply font size immediately

    def binCalcFontSz(self):
        low = self.MIN_FONT_SZ
        high = self.MAX_FONT_SZ
        best_fit = low

        while low <= high:
            mid = (low + high) // 2
            font = QFont('Arial', mid)
            metrics = QFontMetrics(font)
            text_rect = metrics.boundingRect(self.text())
            text_width = text_rect.width()
            text_height = text_rect.height()

            if text_width <= self.width() - 10 and text_height <= self.height() - 10:
                best_fit = mid
                low = mid + 1
            else:
                high = mid - 1

        self.setFont(QFont('Arial', best_fit))
        self.update()  # Refresh the widget to apply font size immediately

    def CalcFontSz(self):
        font_size = self.MAX_FONT_SZ
        while font_size >= self.MIN_FONT_SZ:
            font = QFont('Arial', font_size)
            metrics = QFontMetrics(font)
            text_width = metrics.horizontalAdvance(self.text())
            text_height = metrics.height()
            if ((text_width < self.width() and text_height < self.height())
                or font_size == self.MIN_FONT_SZ):
                break
            font_size -= 1
        self.setFont(QFont('Arial', font_size))
        self.update()  # Refresh the widget to apply font size immediately

    def resizeEvent(self, event):
        self.CalcFontSz()  # Adjust font size when resized
        super().resizeEvent(event)
    def mousePressEvent(self, event):
        super().mousePressEvent(event)  # TODO: Optional?
        if event.button() == Qt.LeftButton:
            self.oMidiPlayer.On(self.Instr, self.Note)
    def mouseReleaseEvent(self, event):
        super().mouseReleaseEvent(event)  # Maintain base class behavior
        if event.button() == Qt.LeftButton:
            self.oMidiPlayer.Off(self.Instr, self.Note)
        elif event.button() == Qt.RightButton:
            self.openSelectionDialog()
    def openSelectionDialog(self):
        dialog = tMidiBtnDlg(self)
        if dialog.exec_():
            sNamClr, sInstr, sNote = dialog.getSelections()
            self.Update(sNamClr, sInstr, sNote)
    @staticmethod
    def main():
        app = QApplication(argv)
        class tSimPlayer:  # Mock tMidiPlayer class for testing
            @staticmethod
            def On(instr, note):
                print(f"Note {note} of instrument {instr} pressed.")
            @staticmethod
            def Off(instr, note):
                print(f"Note {note} of instrument {instr} released.")

        # Create an instance of tMidiBtn
        btn = tMidiBtn(tSimPlayer(),
                       'Red',
                       'Accordion',
                       'Bass_D♯/E♭')
        btn.show()
        exit(app.exec_())

if __name__ == "__main__":
    tMidiBtn.main()
