# Quest Review Logging System
This system allows users to write a short review, which is then saved to a text file.
It uses a function and exception handling to safely store feedback.

## Features
- Function write_review() handles saving reviews
- Appends each review to quest_book.txt
- Stores both the user’s name and message
- Handles disk errors (IOError)
- Runs until the user types "stop"

# How to use
Enter your name and your review.
Valid input → review saved to the file.
Disk error → clear warning message.
Type "stop" to exit.


## Learning Purpose
Practice with:
- file handling (open, append mode)
- functions
- exception handling
- simple text‑based logging
- separating logic into modules and packages
