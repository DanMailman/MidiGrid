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
from sys import argv  # Access command-line arguments
from sys import exit  # Terminate program with exit code

# GUI components
from PyQt5.QtWidgets import QPushButton   # Button Widget
from PyQt5.QtWidgets import QApplication  # Application Widget
from PyQt5.QtCore import Qt               # LeftButton
LeftButton = Qt.LeftButton                # enum value

# Custom module imports for MIDI functionality
from tMidiPlayer import tMidiPlayer  # Custom class for handling MIDI player functionalities

# Utility module imports for color and validation handling
from ClrUtils import get_contrastive_text_color  # Utility to get contrastive text color for readability
from ClrUtils import GetHexStr  # Utility to convert RGB values to Hexadecimal color string
from Utilities import ExitOnNoIntVal  # Utility to exit and log error on invalid integer input
from Utilities import ExitOnNoRGBVal  # Utility to exit and log error on invalid RGB input

# Constant module imports for predefined values
from kNamClr import COLOR_RGBS  # Module containing predefined color RGB values
from kNote import NOTE_NUMS  # Module containing predefined note numbers
from kInstr import INSTR_NUMS  # Module containing predefined instrument numbers
class tMidiBtn(QPushButton):
    def __init__(self, oMidiPlayer: tMidiPlayer, sNamClr: str, sInstr: str, sNote: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        nInstr = ExitOnNoIntVal(sInstr, INSTR_NUMS, 'Instrument')
        nNote = ExitOnNoIntVal(sNote, NOTE_NUMS, 'Note')
        color = ExitOnNoRGBVal(sNamClr, COLOR_RGBS, 'Color')
        text_color = get_contrastive_text_color(color)
        self.setStyleSheet(f"background-color: {GetHexStr(color)}; color: {text_color};")
        self.setText(f"{sInstr}\n{sNote}")
        self.oMidiPlayer = oMidiPlayer
        self.Instr = nInstr
        self.Note = nNote
    def mousePressEvent(self, event):
        if event.button() == LeftButton:
            self.oMidiPlayer.On(self.Instr, self.Note)
    def mouseReleaseEvent(self, event):
        if event.button() == LeftButton:
            self.oMidiPlayer.Off(self.Instr, self.Note)
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
        btn = tMidiBtn(tMidiPlayer(), 'Red', 'Accordion', 'Bass_D♯/E♭')
        btn.show()
        exit(app.exec_())
if __name__ == "__main__":
    tMidiBtn.main()
