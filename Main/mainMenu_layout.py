from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton

def create_main_widget():
    print("Creating main widget")
    widget = QWidget()
    layout = QVBoxLayout()

    label = QLabel("Welcome to the RPG Toolkit", parent=widget)
    button1 = QPushButton("Character Creator", parent=widget)
    button2 = QPushButton("Load Creature", parent=widget)

    layout.addWidget(label)
    layout.addWidget(button1)
    layout.addWidget(button2)

    widget.setLayout(layout)
    return widget