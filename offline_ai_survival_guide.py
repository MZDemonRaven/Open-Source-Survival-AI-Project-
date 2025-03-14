import json
import os

# Load the updated survival guide JSON file
SURVIVAL_GUIDE_PATH = "updated_offline_survival_guide.json"

try:
    with open(SURVIVAL_GUIDE_PATH, "r", encoding="utf-8") as f:
        survival_data = json.load(f)
except FileNotFoundError:
    print(f"Error: {SURVIVAL_GUIDE_PATH} not found. Make sure the JSON file is in the same directory.")
    exit()

def display_menu():
    print("\n🔹 **Survival Topics Menu** 🔹")
    for i, topic in enumerate(survival_data.keys(), 1):
        print(f"{i}. {topic}")
    print("Type a topic name to view details, or type 'exit' to quit.")

def search_survival_guide():
    while True:
        display_menu()
        user_input = input("\nEnter a survival topic (or type 'exit' to quit): ").strip()
        if user_input.lower() == "exit":
            print("Exiting survival guide.")
            break
        elif user_input in survival_data:
            print(f"\n🔹 {user_input} 🔹\n{survival_data[user_input]}")
        else:
            print("Topic not found. Try searching for another survival skill.")

if __name__ == "__main__":
    print("\n🔹 Offline AI Survival Guide 🔹")
    search_survival_guide()