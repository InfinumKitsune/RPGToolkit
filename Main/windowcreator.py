import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel
from mainMenu_layout import create_main_widget

class MainWindow(QMainWindow):
    def __init__(self):
        print("Initializing Main Window")
        super().__init__()
        self.setWindowTitle("RPG Toolkit")
        self.setGeometry(100, 100, 800, 600)

        central_widget = create_main_widget()
        self.setCentralWidget(central_widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())