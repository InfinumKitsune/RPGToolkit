from dataclasses import dataclass, field

@dataclass
class Character:
    name: str
    race: str
    char_class: str
    stats: dict
    status: str = "Ready"
    id: int = field(default_factory=int)