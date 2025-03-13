
import json
import pyttsx3

# Load the survival guide data
survival_guide_data = {
    "Water Purification": "Boiling: Bring water to a rolling boil for at least 1 minute (3 minutes at high altitudes) to kill bacteria, viruses, and parasites.\nFiltration: Use cloth, sand, charcoal, and gravel to remove particles. Commercial filters (LifeStraw, Sawyer, Berkey) remove bacteria and protozoa.\nChemical Treatment: Purification tablets (chlorine dioxide, iodine) kill microbes. Bleach: Use 2 drops per quart (8 drops per gallon), wait 30 minutes.\nSolar Disinfection (SODIS): Fill clear plastic bottles, leave in direct sunlight for 6+ hours. UV radiation kills pathogens.\nDistillation: Boil water, collect steam into a clean container. Removes salt, heavy metals, and bacteria.",
    "Food Storage": "Dry Goods: Store in sealed, airtight containers to prevent pests and moisture.\nCanning: Use pressure canning for meats, vegetables; water-bath canning for acidic foods.\nRoot Cellaring: Store potatoes, carrots, onions in cool, dark, ventilated areas.\nDehydration: Dry fruits, meats (jerky), and vegetables to preserve them for months.\nFreezing: If available, freeze food at 0\u00b0F (-18\u00b0C) to extend shelf life indefinitely.",
    "First Aid": "Basic Supplies: Keep antiseptic, bandages, gauze, pain relievers, and wound dressings.\nCPR & Rescue Breathing: Learn and practice these skills for emergencies.\nInfection Control: Clean wounds with sterile water or alcohol; use antibiotic ointment.\nSplinting & Fractures: Immobilize with stiff objects (wood, rolled fabric), secure with tape or cloth.\nNatural Remedies: Honey for wounds, charcoal for poisoning, and aloe for burns.",
    "Shelter": "Emergency Shelter: Use tarps, mylar blankets, or debris to create insulation.\nLean-To: Use sturdy branches and cover with leaves or a tarp.\nDebris Hut: Build a dome of sticks and cover with leaves for insulation.\nUnderground Shelter: Dig into hillsides or caves for thermal regulation.\nSnow Shelter: Dig into packed snow, create an air vent, and insulate with layers.",
    "Fire Making": "Friction Methods: Bow drill, hand drill, fire plow using dry wood and kindling.\nFlint & Steel: Strike steel against flint to create sparks.\nChemical Fire Starting: Use potassium permanganate with glycerin for ignition.\nFirestarters: Cotton balls soaked in petroleum jelly, char cloth, or dryer lint.\nSolar Fire: Use a magnifying glass or a polished metal surface to concentrate sunlight.",
    "Navigation": "Using a Compass: Hold level, align needle with north, follow cardinal directions.\nSun Navigation: Sun rises in the east, sets in the west. Shadow sticks indicate direction.\nStar Navigation: Use the North Star in the Northern Hemisphere, Southern Cross in the Southern Hemisphere.\nLandmarks: Identify rivers, mountains, and ridges to orient yourself.\nMoss Growth: In shaded areas, moss often grows on the north side of trees (not always reliable).",
    "Barter and Trade": "Bartering Skills: Offer useful services such as repair, medicine, or foraging skills.\nHigh-Value Trade Goods: Salt, spices, alcohol, antibiotics, batteries, and ammunition.\nBartering Safety: Avoid revealing all goods at once; negotiate in neutral locations.\nCommunity Trade Networks: Find barter-friendly groups via prepper networks, churches, and co-ops.\nDIY Production: Learn to make soap, candles, tools, or food items for trade.",
    "Emergency Communication": "HAM Radio: Obtain a license to use amateur radio frequencies for long-range contact.\nCB Radio: Citizen\u2019s Band radios work short-range (5-10 miles) without licensing.\nSignal Flares: Use in open areas to signal for help.\nMirror Signaling: Reflect sunlight toward rescuers using a shiny object.\nEncrypted Messaging: Use offline, decentralized apps like Briar or mesh networks for secure communication."
}

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def display_menu():
    print("\n🔹 Offline AI Survival Guide 🔹")
    print("Select a topic by entering the corresponding number or type the topic name. Type 'exit' to quit:\n")
    for i, topic in enumerate(survival_guide_data.keys(), start=1):
        print(f" {i}. {topic}")

def search_survival_guide(topic):
    topic_lower = topic.lower()
    for key, value in survival_guide_data.items():
        if topic_lower in key.lower():
            response = f"**{key}**\n{value}"
            speak(response)
            return response
    return "Topic not found. Try searching for another survival skill."

if __name__ == "__main__":
    speak("Welcome to the Offline AI Survival Guide. You can ask for survival topics or select from a menu.")
    while True:
        display_menu()
        choice = input("\nEnter a number, a topic name, or type 'search' to manually search for any term (or 'exit' to quit): ").strip()

        if choice.lower() == 'exit':
            speak("Exiting. Stay safe!")
            print("Exiting... Stay safe!")
            break

        if choice.lower() == 'search':
            search_term = input("Enter search term: ").strip()
            print("\n" + search_survival_guide(search_term) + "\n")
            continue

        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= len(survival_guide_data):
                selected_topic = list(survival_guide_data.keys())[choice - 1]
                print("\n" + search_survival_guide(selected_topic) + "\n")
            else:
                print("Invalid selection. Please choose a valid number.")
        else:
            print("\n" + search_survival_guide(choice) + "\n")
