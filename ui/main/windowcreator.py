import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QTabWidget, QVBoxLayout
from ui.main.mainMenu_layout import create_main_widget
from core.characters.character_manager import CharacterManager
from core.characters.character import Character

#Create a main window for the application using PyQt6
class MainWindow(QMainWindow):
    def __init__(self):
        print("Initializing Main Window")
        super().__init__()
        self.setWindowTitle("RPG Toolkit")
        self.setGeometry(100, 100, 800, 600)

        central_widget = create_main_widget()
        self.setCentralWidget(central_widget)

        # Initialize tabs
        self.tabs = QTabWidget()

        # Character tabs
        self.tabs.addTab(CharacterLogTab(self.character_manager), "Character Log")
        self.tabs.addTab(CharacterCreatorTab(self.character_manager), "Character Creator")
        self.tabs.addTab(LivingQuaratersTab(self.character_manager), "Home")

        # Editor tabs

        # Games tabs

        # Social tabs

        # Settings tabs


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

def run_app():
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()