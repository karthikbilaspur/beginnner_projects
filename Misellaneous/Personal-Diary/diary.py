import json
import os
import datetime
import getpass
import random

DIARY_FILE = "diary.json"
PASSWORD = "password123"

def load_diary():
    if os.path.exists(DIARY_FILE):
        with open(DIARY_FILE, 'r') as file:
            return json.load(file)
    else:
        return []

def save_diary(entries):
    with open(DIARY_FILE, 'w') as file:
        json.dump(entries, file, indent=4)

def authenticate():
    attempts = 0
    while attempts < 3:
        password = getpass.getpass("Enter password: ")
        if password == PASSWORD:
            return True
        attempts += 1
        print("Incorrect password. Try again.")
    return False

def add_entry():
    diary = load_diary()
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    title = input("Enter title: ")
    entry = input("Enter diary entry: ")
    tags = input("Enter tags (comma-separated): ").split(',')
    tags = [tag.strip() for tag in tags]
    mood = input("Enter mood (happy/sad/excited/content): ")
    new_entry = {
        "id": len(diary) + 1,
        "date": date,
        "title": title,
        "entry": entry,
        "tags": tags,
        "mood": mood
    }
    diary.append(new_entry)
    save_diary(diary)
    print("Entry saved!")

def view_entries():
    diary = load_diary()
    for entry in diary:
        print(f"Entry {entry['id']}:")
        print(f"Date: {entry['date']}")
        print(f"Title: {entry['title']}")
        print(f"Entry: {entry['entry']}")
        print(f"Tags: {', '.join(entry['tags'])}")
        print(f"Mood: {entry['mood']}\n")

def search_entries():
    keyword = input("Enter search keyword: ").lower()
    diary = load_diary()
    found_entries = [entry for entry in diary if 
                     keyword in entry['title'].lower() or 
                     keyword in entry['entry'].lower() or 
                     keyword in ', '.join(entry['tags']).lower()]
    if found_entries:
        for entry in found_entries:
            print(f"Entry {entry['id']}:")
            print(f"Date: {entry['date']}")
            print(f"Title: {entry['title']}")
            print(f"Entry: {entry['entry']}")
            print(f"Tags: {', '.join(entry['tags'])}")
            print(f"Mood: {entry['mood']}\n")
    else:
        print("No matching entries found.")

def delete_entry():
    diary = load_diary()
    view_entries()
    entry_id = int(input("Enter entry ID to delete: "))
    for i, entry in enumerate(diary):
        if entry['id'] == entry_id:
            del diary[i]
            save_diary(diary)
            print("Entry deleted!")
            return
    print("Invalid entry ID.")

def populate_diary():
    templates = [
        {"title": "Daily Gratitude", "entry": "Today I'm grateful for..."},
        {"title": "Goals", "entry": "Tomorrow's objectives:"}
    ]
    diary = []
    for i in range(30):
        entry = {
            "id": i+1,
            "date": (datetime.datetime.now() + datetime.timedelta(days=i)).strftime("%Y-%m-%d"),
            "title": random.choice(templates)["title"],
            "entry": random.choice(templates)["entry"],
            "tags": ["daily", "gratitude"],
            "mood": random.choice(["happy", "motivated", "reflective"])
        }
        diary.append(entry)
    save_diary(diary)

def main():
    if authenticate():
        populate_diary()  # Populate diary.json initially
        while True:
            print("\nDiary Menu:")
            print("1. Add Entry")
            print("2. View Entries")
            print("3. Search Entries")
            print("4. Delete Entry")
            print("5. Update Entry")
            print("6. Exit")
            choice = input("Enter choice: ")
            if choice == "1":
                add_entry()
            elif choice == "2":
                view_entries()
            elif choice == "3":
                search_entries()
            elif choice == "4":
                delete_entry()
            elif choice == "5":
                update_entry()
            elif choice == "6":
                break
            else:
                print("Invalid choice. Please try again.")
    else:
        print("Authentication failed.")

if __name__ == "__main__":
    main()