from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout
from PyQt6.QtCore import Qt

def create_main_widget():
    print("Creating main widget")
    widget = QWidget()

    # Main vertical layout
    layout = QVBoxLayout()

    # Title label
    label = QLabel("Welcome to the RPG Toolkit", parent=widget)
    label.setAlignment(Qt.AlignmentFlag.AlignCenter)
    layout.addStretch()
    layout.addWidget(label)
    layout.addStretch()

    # Two column layout for buttons
    columns = QHBoxLayout()

    leftColumn = QVBoxLayout()
    rightColumn = QVBoxLayout()

    # Left column buttons
    leftColumn.addWidget(QPushButton("Character Menu"))
    leftColumn.addWidget(QPushButton("Games Menu"))
    leftColumn.addWidget(QPushButton("Editor Menu"))
    #leftColumn.addStretch()

    # Right column buttons
    rightColumn.addWidget(QPushButton("Social Menu"))
    rightColumn.addWidget(QPushButton("Settings"))
    rightColumn.addWidget(QPushButton("Exit"))
    #rightColumn.addStretch()

    # Add columns to the horizontal layout
    columns.addLayout(leftColumn)
    columns.addLayout(rightColumn)

    # Add the columns to the main layout
    layout.addLayout(columns)

    widget.setLayout(layout)
    return widget