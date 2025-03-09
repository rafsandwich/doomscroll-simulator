# doomscroll-simulator
A command line, doomscroll-inspired simulator built in Python!

This project simulates a post-scrolling experience, where the user can enter commands on the console such as 'scroll', 'comment', 'like' (amongst others) and posts will be shown to them. The posts are partly randomly selected from different text files, in that the text file the user's post comes from depends on how many posts the user has viewed so far. ASCII art is also loaded from a text file. Most of the art is sourced from www.asciiart.eu, with authors credited according to their guidelines.

Data is collected on the user's session, such as how many likes they've made, comments they've made, how many posts they've ignored amongst others so that the program can trigger events based on how the user is interacting with it.

Posts have weighted rarity, meaning a user is more likely to encounter a Common post (~65% of the time) vs a Mythical post (~1% of the time). Some posts are targeted, in that they will trigger if the user has been interacting a certain way, and if the requirements are met (and a random check is passed) they will display instead of a normally selected post from a text file.

There is a typing-like text effect that occurs for some console output, to create a more natural - and in some places eerie - vibe. There are secrets throughout, hidden in some particular post, output or if the user completes a task (e.g. complete 25 scrolls).

## To run the code

Clone the repo locally and navigate to the root folder. Open your favourite IDE or, as intended, the terminal/command prompt at that path and type ```python3 doomscroller.py```. From here the program will run, and you'll be asked to enter a username (used for some dynamic posts). If you're stuck, try the 'help' command! Happy scrolling.
