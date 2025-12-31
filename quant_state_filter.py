import sys


class ExitWithMessage(Exception):
    pass

try:
  
    # Open your word list file in read-only mode.
    # If it isn't in current directory, specify full path using forward slash ("/") not backslash.

    with open("filtered_results.txt") as f:
        for line in f:
            word = line

except ExitWithMessage:
    sys.exit()