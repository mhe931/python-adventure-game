"""
main.py
--------
Automatic story graph builder.

- Reads ALL story files in the "story" folder.
- Each file has a "From:" line and story text.
- The program builds choices dynamically based on "From:" references.
"""

import os

STORY_DIR = "story"


def load_all_stories():
    """
    Read all story files and return two dictionaries:
    - stories[file] = story text
    - links[file] = list of files that come FROM this file
    """
    stories = {}
    links = {}

    for filename in os.listdir(STORY_DIR):
        if not filename.endswith(".txt"):
            continue

        path = os.path.join(STORY_DIR, filename)
        with open(path, "r", encoding="utf-8") as f:
            lines = [line.strip() for line in f.readlines() if line.strip()]

        from_file = None
        story_text = []

        for line in lines:
            if line.lower().startswith("from:"):
                from_file = line.split(":", 1)[1].strip()
            else:
                story_text.append(line)

        # Save story text
        stories[filename] = "\n".join(story_text)

        # Add link (from -> current)
        if from_file:
            links.setdefault(from_file, []).append(filename)

    return stories, links


def play_game(start_file="start.txt"):
    """
    Play the game starting from start_file.
    """
    stories, links = load_all_stories()

    current_file = start_file

    while True:
        text = stories.get(current_file)

        if text is None:
            print(f"Error: Story file {current_file} not found.")
            break

        # Show story
        print("\n" + "=" * 40)
        print(text)
        print("=" * 40)

        # Find possible next steps
        choices = links.get(current_file, [])

        if not choices:
            print("The End.")
            break

        # Display numbered choices
        for i, choice_file in enumerate(choices, 1):
            # Show first line of the story as preview
            preview = stories[choice_file].split("\n")[0]
            print(f"{i}) {preview} -> {choice_file}")

        # Get player input
        user_input = input("Enter your choice: ").strip()

        if user_input.isdigit() and 1 <= int(user_input) <= len(choices):
            current_file = choices[int(user_input) - 1]
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    play_game()
