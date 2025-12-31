# This script reads a word list from a file named "XwiWordList.dict"
# and prints out words that meet certain criteria:
# - The word's score must be at least MIN_SCORE
# - The word's length must be at least MIN_LEN

import sys

# This example uses a try/except pattern to handle errors.
# It's a common pattern in Python, and is the preferred way to handle errors.
# The "except" block is only executed if an exception is raised in the "try" block.
# Use this pattern in the other examples here if you like.

MIN_SCORE = 50
MIN_LEN = 5

class ExitWithMessage(Exception):
    pass

try:
  
    # Open your word list file in read-only mode.
    # If it isn't in current directory, specify full path using forward slash ("/") not backslash.

    with open("XwiWordList.dict") as f_in, open("filtered_results.txt", "w") as f_out:
        for line in f_in:
            parts = line.split(';') # Split the line into parts, using ";" as the delimiter
            word = parts[0].strip() # Get the first part of the line, the word before ";"
            score = int(parts[1])   # Score isn't used here but this is how you get it
            
            # Check score is >= MIN_SCORE and word length is >= MIN_LEN
            if score >= MIN_SCORE and len(word) >= MIN_LEN:
                print(word, file=f_out) # Write the word to the output file

except ExitWithMessage:
    sys.exit()