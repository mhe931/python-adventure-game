"""
main.py
--------
Updated to use "From:" and "Choices:" structure.
This makes it easier for contributors to connect story parts without reading all files.
"""

import os

STORY_DIR = "story"


def load_story(filename):
    """
    Load and return the story metadata, text, and choices from a file.

    Expected format:
    ----------------
    From: previous_file.txt

    Story text...

    Choices:
    1) Choice text -> next_file.txt
    2) Another choice -> different_file.txt
    """
    path = os.path.join(STORY_DIR, filename)

    if not os.path.exists(path):
        print(f"Error: Could not find {filename} in {STORY_DIR}/")
        return None, None, {}

    with open(path, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]

    from_file = None
    story_text = []
    choices = {}
    parsing_choices = False

    for line in lines:
        if line.lower().startswith("from:"):
            from_file = line.split(":", 1)[1].strip()

        elif line.lower().startswith("choices:"):
            parsing_choices = True

        elif parsing_choices and line[0].isdigit() and ")" in line:
            # Parse numbered choice
            try:
                number, rest = line.split(")", 1)
                choice_text, next_file = rest.split("->")
                choices[number.strip()] = {
                    "text": choice_text.strip(),
                    "next": next_file.strip()
                }
            except ValueError:
                continue

        elif not parsing_choices:
            story_text.append(line)

    return from_file, "\n".join(story_text), choices


def play_game(start_file="start.txt"):
    """
    Play the game starting from the given file.
    """
    current_file = start_file

    while True:
        from_file, text, choices = load_story(current_file)

        if text is None:
            break

        # Show story text
        print("\n" + "=" * 40)
        print(text)
        print("=" * 40)

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
