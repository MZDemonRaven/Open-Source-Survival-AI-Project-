
import json

# Load the survival guide data
with open("offline_survival_guide.json", "r", encoding="utf-8") as f:
    survival_data = json.load(f)

def display_menu():
    print("\n🔹 Offline AI Survival Guide 🔹\n")
    print("Select a category:")
    for idx, key in enumerate(survival_data.keys(), start=1):
        print(f"{idx}. {key}")
    print("0. Exit")

def search_topic(topic):
    return survival_data.get(topic, "Topic not found. Try searching for another survival skill.")

def main():
    while True:
        display_menu()
        choice = input("\nEnter a number or type a topic to search: ").strip()
        
        if choice.isdigit():
            choice = int(choice)
            if choice == 0:
                print("Exiting...")
                break
            elif 1 <= choice <= len(survival_data):
                topic = list(survival_data.keys())[choice - 1]
                print(f"\n🔹 {topic} 🔹\n{search_topic(topic)}\n")
            else:
                print("Invalid choice. Try again.")
        else:
            print(f"\n🔹 {choice} 🔹\n{search_topic(choice)}\n")

if __name__ == "__main__":
    main()
