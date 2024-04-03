#** Run reload_krita.py in the Krita Scripter to reload
# Krita Doc: https://api.kde.org/krita/html/classKrita.html

#from .globals import *
from krita import DockWidget
from PyQt5.Qt import PYQT_VERSION_STR
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QImage

class Gamebit(DockWidget):
  def __init__(self):
    super().__init__()
    self.setWindowTitle('Gamebit')
    print('CRTEATING GAMEBIT DOCKER')

    self.mainWidget = QWidget(self)
    self.mainWidget.setLayout(QVBoxLayout())
    self.setWidget(self.mainWidget)

    self.input_widget = QWidget(self.mainWidget)
    self.input_layout = QFormLayout()

    self.prompt = QPlainTextEdit(self.input_widget)
    self.prompt.setPlaceholderText("Describe your end goal...")
    self.prompt.setPlainText("A beautiful mountain li, oils on canvas.")

    self.steps = QSpinBox(self.input_widget)
    self.steps.setRange(5, 300)
    self.steps.setValue(32)
    self.steps.setMaximumWidth(50);

    self.input_layout.addRow("Textbox", self.prompt)
    self.input_layout.addRow("Steps", self.steps)

    self.input_widget.setLayout(self.input_layout)
    self.mainWidget.layout().addWidget(self.input_widget)

    self.gen = QPushButton(self.mainWidget)
    self.gen.setText("Generate")
    self.gen.clicked.connect(lambda: print("Clicked the gen beutton\nClicked the gen beutton\nClicked the gen beutton\nClicked the gen beutton\nClicked the gen beutton\n"))
    self.mainWidget.layout().addWidget(self.gen)


  # notifies when views are added or removed
    # 'pass' means do not do anything
  def canvasChanged(self, canvas):
    pass

# from krita import *

# class ExtensionTemplate(Extension):

#     def __init__(self, parent):
#         super().__init__(parent)

#     # Krita.instance() exists, so do any setup work
#     def setup(self):
#         pass

#     # called after setup(self)
#     def createActions(self, window):
#         pass

