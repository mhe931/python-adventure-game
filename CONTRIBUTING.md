

# Contributing Guide

Thank you for your interest in contributing! 🎉  
This project is meant for beginners, so the steps are simple and beginner-friendly.

---

## ✨ Contribution Workflow
0. **Give a Star the project**

   ⭐️On GitHub, click the "star" button at the top right. 
2. **Fork this repository**  
   On GitHub, click the "Fork" button at the top right.

3. **Clone your fork**  
   Open your terminal and run:
   ```bash
   git clone https://github.com/YOUR-USERNAME/choose-your-own-adventure.git
   cd choose-your-own-adventure
   ```

4. Create a new story file
Inside the story/ folder, add a new .txt file.
Example: mystery_room.txt


5. Write your story
Use this format:
ftom: start.txt

Your story text goes here.

Choices:
1) Choice description -> next_file.txt
2) Another choice -> different_file.txt

Story text: One or more sentences.

Choices: Start with a number, a parenthesis, and then -> filename.txt.



5. Test your story
Run:
```
python main.py
```
Make sure your choices lead to real files (or create them!).


6. Commit your changes
```
git add story/mystery_room.txt
git commit -m "Added a new story section: mystery_room.txt"
```

7. Push and submit a Pull Request
```
git push origin main
```
Then, go to your fork on GitHub and click "New Pull Request".




---

📂 File Naming Rules

Use lowercase letters and underscores.
✅ forest_path.txt
❌ Forest Path.txt

Always end with .txt.



---

✅ Story File Format

Must contain story text.

Must contain at least one choice.

Each choice must use this exact format:

1) Choice text -> filename.txt



---

🎉 Tips

Keep story sections short and fun.

Feel free to link back to existing files to create loops.

Be creative!


---
