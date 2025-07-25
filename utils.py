def validateLevel(level):
    """
    Validates if the level is a positive integer.
    """
    try:
        lvl = int(level)
        if lvl < 0:
            raise ValueError("Level must be a non-negative integer.")
    except ValueError as e:
        print(f"{e} is an invalid level. Please enter a valid non-negative integer.")
        return None
    return lvl

def formatEntry(entry):
    """
    Formats the entry and creates baseline stats for the adventurer based off the class and level.
    """
    if not isinstance(entry, dict):
        print("Entry must be a dictionary.")
        return

    # Extracting name, level, and class from the entry
    name = entry.get('name', 'Unknown Adventurer')
    level = entry.get('level', 1)
    aClass = entry.get('class', 'Fighter')

    # Create baseline strength based on class
    if aClass.lower() in ['warrior', 'fighter', 'barbarian', 'paladin', 'ranger', 'monk', 'rogue', 'cleric', 'warlock']:
        strength = 10 + (level * 2)
    else: # Default strength for non-warrior classes
        strength = 5 + (level * 1)

    # Create baseline mana based on class
    if aClass.lower() in ['mage', 'sorcerer', 'wizard', 'warlock', 'necromancer', 'druid', 'cleric', 'paladin']:
        mana = 20 + (level * 3)
    else: # Default mana for non-magic classes
        mana = 10 + (level * 1)

    import math

    # Create baseline stats
    stats = {
        'name': name,
        'class': aClass,
        'level': level,
        'health': 50 + (level * 10),
        'mana': mana,
        'strength': strength,
        'stamina': 20 + (level * 3),
        'skills': {'light attack': math.ceil(level // 3), 'heavy attack': math.ceil(level // 7), 'magic attack': math.ceil(level // 5)}
    }

    # Format the stats for display
    fSkills = ''
    for skill, level in stats['skills'].items():
        fSkills += f'\t\t{skill.title()}: Level - {level}\n'
        
    formatted_stats = (
        f"\n"
        f"Adventurer: {stats['name']}\n"
        f"Class: {stats['class']}\n"
        f"Level: {stats['level']}\n"
        f"\tHealth: {stats['health']}\n"
        f"\tMana: {stats['mana']}\n"
        f"\tStrength: {stats['strength']}\n"
        f"\tStamina: {stats['stamina']}\n"
        f"\tSkills:\n"
        f"{fSkills}\n"
        )
    print(formatted_stats)

    save = False

    # Ask the user if they want to save the stats
    save_choice = input("Do you want to save these stats? (yes/no): ").strip().lower()
    if save_choice == 'yes':
        save = True
        return formatted_stats, save
    else:
        save = False
        print("Stats not saved.")
        return formatted_stats, save