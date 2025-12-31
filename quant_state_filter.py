import sys

class ExitWithMessage(Exception):
    pass

try:
    # 1. Load the states into a list 
    with open("states.txt") as s_file:
        states = [line.strip().lower() for line in s_file if line.strip()]

    # 2. Load the words into a set
    with open("filtered_results.txt") as f:
        word_set = {line.strip().lower() for line in f if line.strip()}

    # 3. Perform the logic
    with open("results.txt", "w") as out_file:
        for word in word_set:
            # Check if word meets length requirement
            if len(word) >= 7:
                for state in states:
                    # If the 2-letter state code is inside the word
                    if state in word:
                        # Remove the state code once
                        new_word = word.replace(state, "", 1)
                        
                        # See if the remaining letters form another word in our list
                        if new_word in word_set:
                            print(f"Original: {word} | Removed: {state} | Result: {new_word}", file=out_file)

except FileNotFoundError:
    print("Error: One of the required files (states.txt or filtered_results.txt) is missing.")
    raise ExitWithMessage()
except ExitWithMessage:
    sys.exit()