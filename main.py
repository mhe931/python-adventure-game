"""
Choose Your Own Adventure Game Engine
A simple, beginner-friendly game that reads story files and creates an interactive adventure.
"""

import os
import sys
from pathlib import Path

def load_story_files(story_dir):
    """
    Load all story files from the story directory and parse them.
    
    Returns:
        tuple: (stories dict, links dict)
        - stories: {filename: {"from_file": parent, "title": str, "text": str}}
        - links: {parent_file: [child1, child2, ...]}
    """
    stories = {}
    links = {}
    
    # Get all .txt files in the story directory
    story_path = Path(story_dir)
    if not story_path.exists():
        print(f"Error: Story directory '{story_dir}' not found!")
        return {}, {}
    
    txt_files = list(story_path.glob("*.txt"))
    if not txt_files:
        print(f"Error: No .txt files found in '{story_dir}'!")
        return {}, {}
    
    print(f"Loading {len(txt_files)} story files...")
    
    for file_path in txt_files:
        filename = file_path.stem  # filename without .txt extension
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read().strip()
            
            # Parse the file content
            story_data = parse_story_file(content, filename)
            if story_data:
                stories[filename] = story_data
                
        except Exception as e:
            print(f"Warning: Could not read {file_path.name}: {e}")
    
    # Build the links structure
    links = build_links(stories)
    
    print(f"Successfully loaded {len(stories)} stories with {sum(len(children) for children in links.values())} connections.")
    return stories, links

def parse_story_file(content, filename):
    """
    Parse a single story file content into structured data.
    
    Expected format:
    From: parent_file
    Title: story title
    Story text here...
    
    Returns:
        dict or None: {"from_file": str, "title": str, "text": str}
    """
    lines = content.split('\n')
    from_file = None
    title = None
    text_lines = []
    
    i = 0
    # Parse header fields
    while i < len(lines):
        line = lines[i].strip()
        
        if line.lower().startswith('from:'):
            from_file = line[5:].strip()
            # Handle "none" case
            if from_file.lower() == 'none':
                from_file = None
        elif line.lower().startswith('title:'):
            title = line[6:].strip()
        elif line == '':
            # Skip empty lines
            pass
        else:
            # This is the start of story text
            text_lines = lines[i:]
            break
        i += 1
    
    # Validate required fields
    if not title:
        print(f"Warning: {filename}.txt is missing a Title field")
        return None
    
    # Join story text
    story_text = '\n'.join(text_lines).strip()
    if not story_text:
        print(f"Warning: {filename}.txt has no story content")
        return None
    
    return {
        "from_file": from_file,
        "title": title,
        "text": story_text
    }

def build_links(stories):
    """
    Build a links dictionary from stories data.
    
    Args:
        stories: dict of story data
    
    Returns:
        dict: {parent_file: [child1, child2, ...]}
    """
    links = {}
    
    # Get all available story filenames for matching
    available_files = set(stories.keys())
    
    for filename, story_data in stories.items():
        from_file = story_data["from_file"]
        
        if from_file is None:
            # This is a root story
            continue
        
        # Resolve from_file (handle case variations and .txt extension)
        resolved_parent = resolve_filename(from_file, available_files)
        
        if resolved_parent:
            if resolved_parent not in links:
                links[resolved_parent] = []
            links[resolved_parent].append(filename)
        else:
            print(f"Warning: {filename}.txt references unknown parent '{from_file}'")
    
    return links

def resolve_filename(reference, available_files):
    """
    Resolve a filename reference to an actual file, handling case and extension variations.
    
    Args:
        reference: the filename reference from a story file
        available_files: set of available filenames (without .txt)
    
    Returns:
        str or None: resolved filename or None if not found
    """
    # Remove .txt if present
    clean_ref = reference.replace('.txt', '').strip()
    
    # Try exact match first
    if clean_ref in available_files:
        return clean_ref
    
    # Try case-insensitive match
    for available in available_files:
        if clean_ref.lower() == available.lower():
            return available
    
    return None

def find_root_story(stories):
    """
    Find the root story to start the game from.
    Priority: story with from_file=None, then "start" if it exists.
    
    Returns:
        str or None: filename of root story
    """
    # First, look for any story with from_file=None
    for filename, story_data in stories.items():
        if story_data["from_file"] is None:
            return filename
    
    # If no explicit root, look for "start"
    if "start" in stories:
        return "start"
    
    # If still no root found, use the first story alphabetically
    if stories:
        return sorted(stories.keys())[0]
    
    return None

def display_story(story_data):
    """Display a story section with nice formatting."""
    print("\n" + "="*60)
    print(f"📖 {story_data['title']}")
    print("="*60)
    print()
    print(story_data['text'])
    print()

def get_user_choice(max_choice):
    """
    Get a valid choice number from the user.
    
    Args:
        max_choice: maximum valid choice number
    
    Returns:
        int: user's choice (1-indexed)
    """
    while True:
        try:
            choice = input(f"Enter your choice (1-{max_choice}): ").strip()
            choice_num = int(choice)
            
            if 1 <= choice_num <= max_choice:
                return choice_num
            else:
                print(f"Please enter a number between 1 and {max_choice}.")
        
        except ValueError:
            print("Please enter a valid number.")
        except KeyboardInterrupt:
            print("\nGame interrupted. Goodbye!")
            sys.exit(0)

def play_game(stories, links):
    """
    Main game loop.
    
    Args:
        stories: dict of story data
        links: dict of story connections
    """
    # Find starting story
    current_story = find_root_story(stories)
    if not current_story:
        print("Error: No valid starting story found!")
        return
    
    print("🌟 Welcome to Choose Your Own Adventure! 🌟")
    print("Type Ctrl+C at any time to quit.\n")
    
    while True:
        # Display current story
        story_data = stories[current_story]
        display_story(story_data)
        
        # Check if there are any choices available
        available_choices = links.get(current_story, [])
        
        if not available_choices:
            print("🏁 THE END")
            print("Thank you for playing!")
            break
        
        # Display choices
        print("What do you want to do?")
        for i, choice_filename in enumerate(available_choices, 1):
            choice_story = stories[choice_filename]
            print(f"{i}. {choice_story['title']}")
        
        # Get user choice
        choice_num = get_user_choice(len(available_choices))
        current_story = available_choices[choice_num - 1]

def main():
    """Main entry point of the game."""
    story_dir = "story"
    
    # Load all story files
    stories, links = load_story_files(story_dir)
    
    if not stories:
        print("No valid stories found. Please check your story files!")
        return
    
    # Start the game
    play_game(stories, links)

if __name__ == "__main__":
    main()