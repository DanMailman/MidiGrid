"""
tMidiGrid.py
Dan Mailman
15-May-24

Description:
    This module defines the tMidiGrid class, which extends QWidget from PyQt5.
    It creates a grid layout of tMidiBtn buttons, which represent a MIDI controller grid
    that interacts with a MIDI player. Each button is associated with a specific musical
    instrument and note, and dynamically resizes based on the window size.

Dependencies:
    PyQt5: Used for the GUI components.
    tMidiPlayer: A custom class handling MIDI playback functionalities.
    tMidiBtn: Custom button class that represents a MIDI controller button.
    kNote: Module containing constants and mappings for notes.
    kNamClr: Module containing constants and mappings for colors.

Usage:
    This class is intended to be used in a graphical MIDI control application.
    To test the grid, run this module directly, and a GUI window with a functioning
    MIDI button grid will appear.

Example:
    >>> from tMidiPlayer import tMidiPlayer
    >>> grid = tMidiGrid(tMidiPlayer())
    >>> grid.show()

Notes:
    - Ensure all dependencies are properly installed and available in your Python environment.
    - This module is part of a larger application that requires a graphical environment to run.
"""

from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QSizePolicy
from PyQt5.QtCore import Qt
from tMidiPlayer import tMidiPlayer
from tMidiBtn import tMidiBtn
from kNote import NOTE_NUMS
from kNamClr import COLOR_RGBS

class tMidiGrid(QWidget):
    """
    tMidiGrid is a custom QWidget that creates a grid layout of tMidiBtn buttons,
    each representing a MIDI controller button.

    Attributes:
        NUM_ROWS (int): The number of rows in the grid.
        NUM_COLS (int): The number of columns in the grid.
        oMidiPlayer (tMidiPlayer): The MIDI player instance used to handle MIDI functionalities.
    """
    NUM_ROWS = 4
    NUM_COLS = 8

    def __init__(self, oMidiPlayer, parent=None):
        """
        Initializes the tMidiGrid with the specified MIDI player.

        Args:
            oMidiPlayer (tMidiPlayer): The MIDI player instance.
            parent (QWidget, optional): The parent widget. Defaults to None.
        """
        super().__init__(parent)
        self.oMidiPlayer = oMidiPlayer
        self.initUI()

    def initUI(self):
        """
        Initializes the user interface by creating a grid layout and adding
        tMidiBtn buttons to it.
        """
        layout = QGridLayout(self)
        layout.setSpacing(0)  # Remove spacing between buttons
        self.setLayout(layout)

        # Generate a sorted list of notes and colors
        sorted_notes = sorted(NOTE_NUMS.items(), key=lambda x: x[1])[:self.NUM_ROWS * self.NUM_COLS]
        sorted_colors = sorted(COLOR_RGBS.keys())[:self.NUM_ROWS * self.NUM_COLS]

        index = 0
        for row in range(self.NUM_ROWS):
            for col in range(self.NUM_COLS):
                if index < len(sorted_notes) and index < len(sorted_colors):
                    note, color = sorted_notes[index][0], sorted_colors[index]
                    btn = tMidiBtn(self.oMidiPlayer, color, 'Accordion', note)
                    btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                    layout.addWidget(btn, row, col)
                    layout.setRowStretch(row, 1)
                    layout.setColumnStretch(col, 1)
                index += 1

    def resizeEvent(self, event):
        """
        Handles the resize event to ensure the grid is resized properly.

        Args:
            event (QResizeEvent): The resize event.
        """
        super().resizeEvent(event)
        self.updateGridSize()

    def updateGridSize(self):
        """
        Updates the size of each cell in the grid based on the current window size.
        """
        grid_layout = self.layout()
        total_rows = grid_layout.rowCount()
        total_cols = grid_layout.columnCount()
        for row in range(total_rows):
            grid_layout.setRowStretch(row, 1)
        for col in range(total_cols):
            grid_layout.setColumnStretch(col, 1)

    @staticmethod
    def main():
        """
        The main method to run a test application for the tMidiGrid class.
        """
        app = QApplication([])
        midiPlayer = tMidiPlayer()  # Replace with actual implementation
        grid = tMidiGrid(midiPlayer)
        grid.setMinimumSize(100, 100)  # Set a small minimum size
        grid.resize(300, 150)  # Set a small initial size
        grid.show()
        exit(app.exec_())

if __name__ == "__main__":
    tMidiGrid.main()
