import utils
import time

def create_adventurer():
    name = input("Enter the name of the adventurer: ")
    while True:
        try:
            # Validate level input
            level = int(input("Enter the level of the adventurer (1-100): "))
            lvl = utils.validateLevel(level)
            if lvl is not None:
                break
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a valid level between 1 and 100.")
    aClass = input("Enter the class of the adventurer (e.g., Warrior, Mage, Rogue): ")

    entry = {
        'name': name,
        'level': lvl,
        'class': aClass,
    }

    # Check if the adventurer already exists
    updatedLines = []
    update_choice = 'no'
    with open('adventurers.txt', 'r') as file:
        existing_entries = file.readlines()
        for line in existing_entries:
            if name.lower() in line.lower():
                print(f"An adventurer with the name '{name}' already exists. Are you updating their stats? (yes/no): ")
                update_choice = input().strip().lower()
                if update_choice == 'no':
                    print("Please log a new adventurer or update an existing one. Exiting to menu.")
                    time.sleep(3)
                    main()
    
    formatted_stats, save = utils.formatEntry(entry)

    if save == True:
        # Update existing adventurer stats
        if update_choice == 'yes':
            updatedLines.append(formatted_stats)
            with open('adventurers.txt', 'w') as file:
                file.writelines(updatedLines)
            print("Adventurer stats updated successfully!")

        # Save a new adventurer to the file
        try:
            with open('adventurers.txt', 'a') as file:
                file.write(formatted_stats)
            print("Adventurer stats saved successfully!")
        except Exception as e:
            print(f"An error occurred while saving the stats: {e}")

def main():
    print("Welcome to the Adventurer Log Builder!")
    print("Please select from the following options:")
    print("1. Create a new adventurer")
    print("2. View existing adventurers")
    print("3. Exit")

    while True:
        choice = input("Enter your choice (1-3): ")
        
        if choice == '1':
            create_adventurer()
        elif choice == '2':
            try:
                with open('adventurers.txt', 'r') as file:
                    adventurers = file.readlines()
                    if adventurers:
                        print("\nExisting Adventurers:")
                        for adventurer in adventurers:
                            print(adventurer)
                    else:
                        print("No adventurers found.")
            except FileNotFoundError:
                print("No adventurers have been created yet.")
        elif choice == '3':
            print("Exiting the Adventurer Log Builder. Goodbye!")
            break


if __name__ == "__main__":
    main()
