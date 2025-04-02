
import sqlite3

def search_guides(term):
    conn = sqlite3.connect('survival_guides_complete.db')
    cursor = conn.cursor()
    query = "SELECT title, category, content FROM survival_guide WHERE title LIKE ? OR content LIKE ?"
    wildcard_term = f"%{term}%"
    cursor.execute(query, (wildcard_term, wildcard_term))
    results = cursor.fetchall()
    conn.close()
    return results

def main():
    print("🌿 Welcome to the Survival AI Terminal 🌿")
    while True:
        term = input("\nEnter a search term (or type 'exit' to quit): ").strip()
        if term.lower() == 'exit':
            print("Exiting survival guide. Stay safe out there.")
            break
        results = search_guides(term)
        if results:
            print(f"\nFound {len(results)} result(s):\n")
            for title, category, content in results:
                print(f"---\nTitle: {title}\nCategory: {category}\n\n{content}\n")
        else:
            print("No results found. Try a different term.")

if __name__ == "__main__":
    main()
