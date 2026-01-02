from PyQt6.QtCore import QObject, pyqtSignal

class CharacterManager(QObject):
    character_added = pyqtSignal(object)
    character_updated = pyqtSignal(object)
    character_deleted = pyqtSignal(object)
    # Signals will go here later

    def __init__(self):
        super().__init__()
        self.characters = []  # List to store character data
        self._next_id = 1  # Internal counter for unique IDs

    def add_character(self, character):
        character.id = self._next_id
        self._next_id += 1

        self.characters.append(character)
        self.character_added.emit(character)

    def update_character(self, character):
        # For now, assume the character object is already updated

        self.character_updated.emit(character)

    def delete_character(self, character):
        if character in self.characters:
            self.characters.remove(character)
            self.character_deleted.emit(character)