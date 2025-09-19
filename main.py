"""
main.py
--------
This is the central game script. It loads story files from the "story" folder,
presents text and choices, and lets the player navigate through the adventure.

Beginner-friendly design:
- Easy to read and modify.
- Handles basic input errors.
- Uses plain text files for story content.
"""

import os

STORY_DIR = "story"

def load_story(filename):
    """
    Load and return the story text and choices from a given file.

    Story file format:
    ------------------
    Story text (can be multiple lines)

    Choices:
    1) Choice text -> next_file.txt
    2) Choice text -> another_file.txt
    """
    path = os.path.join(STORY_DIR, filename)

    if not os.path.exists(path):
        print(f"Error: Could not find {filename} in {STORY_DIR}/")
        return None, {}

    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # Separate story text and choices
    text_lines = []
    choices = {}

    for line in lines:
        line = line.strip()
        if line.startswith(tuple(str(i) for i in range(1, 10))):  # a numbered choice
            try:
                number, rest = line.split(")", 1)
                choice_text, next_file = rest.split("->")
                choices[number.strip()] = {
                    "text": choice_text.strip(),
                    "next": next_file.strip()
                }
            except ValueError:
                continue  # skip malformed lines
        elif line:
            text_lines.append(line)

    return "\n".join(text_lines), choices


def play_game(start_file="start.txt"):
    """
    Play the game starting from the given file.
    """
    current_file = start_file

    while True:
        text, choices = load_story(current_file)

        if text is None:
            break

        # Show story text
        print("\n" + "="*40)
        print(text)
        print("="*40)

        if not choices:
            print("The End.")
            break

        # Show choices
        for num, choice in choices.items():
            print(f"{num}) {choice['text']}")

        # Get user input
        user_input = input("Enter your choice: ").strip()

        if user_input in choices:
            current_file = choices[user_input]["next"]
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    play_game()
