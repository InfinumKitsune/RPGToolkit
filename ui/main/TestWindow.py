from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QVBoxLayout, QHBoxLayout, QPushButton,
    QListWidget, QTextEdit, QSplitter
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("RPG Toolkit")

        # --- Left Sidebar ---
        sidebar = QWidget()
        sidebar_layout = QVBoxLayout()
        sidebar.setLayout(sidebar_layout)

        sidebar_layout.addWidget(QPushButton("NPC Generator"))
        sidebar_layout.addWidget(QPushButton("Item Creator"))
        sidebar_layout.addWidget(QPushButton("Encounter Builder"))
        sidebar_layout.addStretch()

        # --- Main Workspace ---
        workspace = QTextEdit()
        workspace.setPlaceholderText("Output, editors, or tools appear here...")

        # --- Splitter to make them resizable ---
        splitter = QSplitter()
        splitter.addWidget(sidebar)
        splitter.addWidget(workspace)

        # --- Main Layout ---
        container = QWidget()
        layout = QHBoxLayout()
        layout.addWidget(splitter)
        container.setLayout(layout)

        self.setCentralWidget(container)

app = QApplication([])
window = MainWindow()
window.show()
app.exec()
