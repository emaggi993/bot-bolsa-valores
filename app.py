
import sys
from PySide6.QtWidgets import QApplication

from controllers.main_window import MainWidowsForm

if __name__=="__main__":
    app = QApplication()

    window = MainWidowsForm()

    window.show()

    sys.exit(app.exec())