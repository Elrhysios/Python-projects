import os
import difflib

#get the directory where this script filee is saved
script_dir = os.path.dirname(os.path.abspath(__file__))

#join it with  filename for any OS
file_path = os.path.join(script_dir, "words.txt")

#oppen the file using the dynamic path
with open(file_path, "r") as file:
    english_words_list = [line.strip() for line in file]

#prints ths bar on top
print("\n" + "="*50 + "\n")
while True:
    #user input fot the search
    search = input("Search: ").lower().strip()
    if not search:
        continue

#gets the 5 clostest matches (change teh n number for more responses)
    closest_matches = difflib.get_close_matches(search, english_words_list, n=10, cutoff=0.3)

    print()
    if closest_matches:
        if closest_matches[0].lower() == search:
            print(f"Exact match found: {closest_matches[0]}")
            
            if len(closest_matches) > 1:
                print("\nSimilar words:")
                print()
                for match in closest_matches[1:]:
                    print(f"- {match}")
        else:
            print("No exact match found. Did you mean:")
            print()
            for match in closest_matches:
                print(f"- {match}")
    else:
        print("No matches or suggestions found.")

    #the ccool little bar thingy
    print("\n" + "="*50 + "\n")
