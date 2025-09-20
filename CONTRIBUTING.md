## CONTRIBUTING.md
```markdown
# Contributing to Choose Your Own Adventure 🚀

Thank you for wanting to add to our collaborative adventure! This guide will walk you through everything you need to know to contribute new story sections.

## 🎯 Quick Start

**Don't worry if you're new to programming or Git!** Adding a story is simple:

1. **Fork & Clone** the project (or ask your teacher to help)
2. **Create** a new `.txt` file in the `story/` folder
3. **Write** your story using the simple format below
4. **Test** it by running the game
5. **Submit** a pull request

## 📝 Story File Format
Every story file must follow this exact format:


From: parent_file_name
Title: Short description that players will see as a choice
Your actual story text goes here.
You can write multiple paragraphs.
Make it exciting and engaging!
End with something that leads to choices or concludes the story.


### The Three Required Parts:

1. **From:** - Which story this connects to
2. **Title:** - What players see when choosing this option  
3. **Story Text** - Your creative writing!

## 🔗 Understanding Connections

The `From:` field tells the game which story leads to yours.

### Examples:
- `From: start` - Your story connects to start.txt
- `From: forest` - Your story connects to forest.txt  
- `From: none` - Your story is a starting point (rare)

### Rules:
- You can use `forest` or `forest.txt` (both work)
- Case doesn't matter: `Forest`, `forest`, `FOREST` all work
- The file you reference must exist in the `story/` folder

## 🎨 Writing Guidelines

### Good Story Titles:
- "Enter the haunted mansion"
- "Talk to the wise old wizard"
- "Climb the mountain path"
- "Investigate the strange noise"

### Bad Story Titles:
- "Yes" or "No" (too vague)
- "Story 1" (not descriptive)
- "asdf" (not helpful to players)

### Good Story Content:
- **Descriptive**: Paint a picture with your words
- **Engaging**: Make the reader want to know what happens next
- **Clear**: Easy to understand what's happening
- **Connected**: Reference what happened in the parent story

## 📁 Step-by-Step: Adding Your Story

### Step 1: Choose Your Connection Point
Look at existing stories and pick where yours should connect. For example, if you want to add to the forest path:
- Look at `forest.txt` to understand the context
- Your story's `From:` field should be `From: forest`

### Step 2: Create Your File
1. Create a new file in the `story/` folder
2. Name it something descriptive: `haunted_house.txt`, `wizard_tower.txt`, etc.
3. Use lowercase and underscores instead of spaces

### Step 3: Write Your Story


From: forest
Title: Discover the abandoned cabin
As you push through the thick underbrush, you stumble upon a small, weathered cabin hidden among the trees. The wooden walls are covered in moss, and the windows are dark and empty.
The front door hangs slightly open, creaking softly in the breeze. You notice strange symbols carved into the door frame - they seem to glow faintly in the dim forest light.
Do you dare to enter this mysterious place?


### Step 4: Test Your Story
1. Save your file in the `story/` folder
2. Run the game: `python main.py`
3. Play through to your story to make sure it works
4. Check that your title appears as a choice option

### Step 5: Submit Your Contribution
1. **Commit** your changes: `git add story/your_file.txt`
2. **Commit** with a message: `git commit -m "Add haunted cabin story"`
3. **Push** to your fork: `git push origin main`
4. **Create a Pull Request** on the main repository

## 🐛 Common Mistakes to Avoid

### ❌ Wrong Format:

Title: My story
From: start
This is my story text.


**Problem**: `From:` must come before `Title:`

### ❌ Missing Title:


From: forest
This is a story about a cave.

**Problem**: No `Title:` field

### ❌ Wrong File Reference:

From: story_that_doesnt_exist
Title: My adventure
**Problem**: The parent file doesn't exist

### ❌ Empty Story:
From: start
Title: Short story
**Problem**: No actual story content

## 💡 Creative Ideas

### Story Types You Can Add:
- **Branches**: Add new choices to existing stories
- **Endings**: Create conclusion points for story paths
- **Side Quests**: Add optional detours and adventures
- **Character Encounters**: Introduce new people, creatures, or allies
- **Locations**: Describe new places to explore

### Themes to Explore:
- Mystery and detective work
- Fantasy and magic
- Science fiction
- Historical adventures
- Modern-day scenarios
- Horror (keep it appropriate!)
- Comedy and humor
- Educational content

## 🤝 Collaboration Tips

1. **Read Existing Stories First** - Understand the current adventure
2. **Maintain Consistency** - Keep the tone and style similar
3. **Don't Contradict** - Make sure your story fits with what came before
4. **Be Original** - Add your own creative flair
5. **Keep It Appropriate** - Remember this is for educational use

## 🎓 For Teachers

This project is designed to teach:
- **Creative Writing**: Students practice storytelling
- **File Management**: Understanding folder structures
- **Version Control**: Basic Git concepts
- **Collaboration**: Working together on a shared project
- **Following Instructions**: Reading and applying guidelines

### Classroom Workflow:
1. Fork the repository for your class
2. Have students clone the class fork
3. Assign different story branches to different students
4. Review submissions before merging
5. Play the completed adventure together!

## 🆘 Getting Help

### If Your Story Doesn't Show Up:
1. Check that your file is in the `story/` folder
2. Verify the `From:` field references an existing story
3. Make sure you have both `From:` and `Title:` fields
4. Run the game and look for error messages

### If You're Stuck:
- Look at the existing story files as examples
- Ask a classmate or teacher for help
- Check that your file follows the exact format
- Make sure your file ends with `.txt`

### Common Error Messages:
- "Missing Title field" = Add `Title:` to your file
- "References unknown parent" = Check your `From:` field
- "No story content" = Add text after the Title line

## 🌟 Advanced Tips

Once you're comfortable with basic stories, try:

### Creating Multiple Connected Stories:
File: mystery_house.txt
From: village
Title: Investigate the mystery house
File: house_basement.txt
From: mystery_house
Title: Explore the basement
File: house_attic.txt
From: mystery_house
Title: Check the attic

### Building Story Chains:
Create a series of connected adventures that form a longer narrative arc.

### Adding Variety:
- Include different types of choices (moral decisions, puzzle solutions, etc.)
- Create stories with different outcomes based on previous choices
- Add educational content (history, science, literature) wrapped in adventure

---

**Ready to start writing? Jump in and add your story to the adventure!** 🎉

Remember: Every great writer started with a single story. Your contribution will help create an amazing collaborative adventure that others will enjoy for years to come!