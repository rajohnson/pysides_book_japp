import sys
from PySide6.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv)
w = QWidget()
w.resize(250,150)
w.setWindowTitle('Simple')
w.show()
app.exec()