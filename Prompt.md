You are an expert Python developer and teacher.  
Write the complete code and file structure for a beginner-friendly, collaborative "Choose Your Own Adventure" game project.  
The project must be designed for open-source classroom use, making it easy for students to contribute new story sections without reading the entire codebase.
## Functional Requirements
1. Project Structure
   - main.py: central script that loads and runs the game.
   - story/: folder containing text files for story sections.
   - README.md: project overview and play instructions.
   - CONTRIBUTING.md: step-by-step guide for beginners to add new story files.
2. Story File Format
   - Each story file is plain text with this structure:
     
     From: parent_file   # e.g., "start" or "start.txt" or "none"
     Title: short descriptive title
     Story text goes here (multiple lines allowed).
     
   - From: indicates the parent story file.  
     - "none" or missing = this is a root story (starting point).
     - Case-insensitive, should resolve to an actual filename in story/.
   - Title: is mandatory and will be shown to players as the choice text.  
   - Contributors only need to write From + Title + Text. No manual choices.
3. Game Engine (main.py)
   - On startup, read all files in story/.
   - Build two structures:
     - stories[file] = {"from_file": parent, "title": str, "text": str}
     - links[parent] = [child1, child2, ...]
   - Automatically resolve From: values:
     - Accept both start and start.txt.
     - Match case-insensitively.
   - Ignore invalid/unresolvable From: values.
   - Automatically detect the root story (from_file=None or explicitly none).  
     - Default to start.txt if it exists.
   - When playing:
     - Display the current story’s text.
     - Show available child stories as numbered options using their Title:.
     - If no children exist → display "The End".
4. User Input Handling
   - Choices are numbers only.
   - Robust against invalid input (retry on error).
5. Documentation
   - README.md: explain what the project is, how to run it, and how to play.
   - CONTRIBUTING.md: clear instructions for beginners on how to fork, clone, create a new .txt file in story/, add From and Title, and submit a pull request.
## Technical Constraints
- Python 3.x
- Pure standard library (no external dependencies).
- Code must be clean, readable, well-commented, and Pythonic.
- Assume this will be used by absolute beginners — prioritize simplicity and clarity.
## Output
- Provide the full project scaffold in a clear directory tree format.
- Include complete code for main.py.
- Include example story files (start.txt, forest.txt, cave.txt) to demonstrate the system.
- Provide full text for README.md and CONTRIBUTING.md.