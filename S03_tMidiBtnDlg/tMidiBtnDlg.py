from PyQt5.QtWidgets import QDialog, QDialogButtonBox
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtWidgets import QLabel

# Constant module imports for predefined values
from kNamClr import COLOR_RGBS  # Module containing predefined color RGB values
from kNote import NOTE_NUMS     # Module containing predefined note numbers
from kInstr import INSTR_NUMS   # Module containing predefined instrument numbers
class tMidiBtnDlg(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Select MIDI Settings')
        layout = QVBoxLayout(self)
        self.SetupDialog(layout)
        self.setLayout(layout)
    def SetupDialog(self, layout):
        self.comboColor = QComboBox()
        self.comboInstrument = QComboBox()
        self.comboNote = QComboBox()
        self.comboColor.addItems(COLOR_RGBS.keys())
        self.comboInstrument.addItems(INSTR_NUMS.keys())
        self.comboNote.addItems(NOTE_NUMS.keys())
        layout.addWidget(QLabel('Select Color:'))
        layout.addWidget(self.comboColor)
        layout.addWidget(QLabel('Select Instrument:'))
        layout.addWidget(self.comboInstrument)
        layout.addWidget(QLabel('Select Note:'))
        layout.addWidget(self.comboNote)
        btns = QDialogButtonBox(QDialogButtonBox.Ok |
                                QDialogButtonBox.Cancel)
        btns.accepted.connect(self.accept)
        btns.rejected.connect(self.reject)
        layout.addWidget(btns)
    def getSelections(self):
        return (self.comboColor.currentText(),
                self.comboInstrument.currentText(),
                self.comboNote.currentText())

if __name__ == "__main__":
    from tMidiBtn import tMidiBtn
    tMidiBtn.main()
