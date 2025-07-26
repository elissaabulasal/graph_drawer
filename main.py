from PyQt6.QtWidgets import QApplication
from ui import GraphUI
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = GraphUI()
    window.show()
    sys.exit(app.exec())
