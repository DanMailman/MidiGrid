from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout
from PyQt5.QtCore import Qt
from tMidiPlayer import tMidiPlayer
from tMidiBtn import tMidiBtn
from kNote import NOTE_NUMS
from kNamClr import COLOR_RGBS

class tMidiGrid(QWidget):
    NUM_ROWS = 4
    NUM_COLS = 8

    def __init__(self, oMidiPlayer, parent=None):
        super().__init__(parent)
        self.oMidiPlayer = oMidiPlayer
        self.initUI()

    def initUI(self):
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

    @staticmethod
    def main():
        app = QApplication([])
        midiPlayer = tMidiPlayer()  # Replace with actual implementation
        grid = tMidiGrid(midiPlayer)
        grid.show()
        exit(app.exec_())

if __name__ == "__main__":
    tMidiGrid.main()
