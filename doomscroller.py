import random

# first 5 scrolls
level_0_posts = [
    "I was just trying to clear my acne .. *cut to cutting board*",
    "'what do you think it's gonna be?', 'i'm the uncle i think it'll be a girl say less' #boyorgirl?",
    "AI generated food baffles cuisine experts, quoted saying 'I can't believe it's not butter'"
]

# scrolls 5-9
level_1_posts = [
    "A) Level 1 post", # placeholders for testing
    "B) Level 1 post"
]

# scrolls 10 - 14
level_2_posts = [
    "A) Level 2 post",
    "B) Level 2 post"
]

# scrolls 15+
level_3_posts = [
    "A) Level 3 post",
    "B) Level 3 post"
]

post_levels = [level_0_posts, level_1_posts, level_2_posts, level_3_posts]

def generate_post(scroll_count):
    """Generate a random post, changing by the amount the user has scrolled"""
    level = min(scroll_count // 5, len(post_levels) -1) # increase level every 5 scrolls, and ensure it doesn't go out of bounds when checking post_levels[level]
    post = random.choice(post_levels[level])
    return post

def doomscroll():
    """Main doomscroll loop"""
    scroll_count = 0
    print("Welcome to DOOMS. Type 'scroll' to continue, 'comment' to comment, or 'stop' to exit.")

    while True:
        command = input("> ").lower()

        if command == "scroll":
            print("\n" + generate_post(scroll_count) + "\n")
            scroll_count += 1
        elif command == "stop":
            print("You have escaped the scrolling, for now ..")
            print(f"You scrolled through {scroll_count} post(s)!")
            break
        else:
            print("Invalid command. Please try 'scroll' or 'stop'.")

doomscroll()

# add likes
# add comments
# add ascii for post layout on CLI
# add way to generate posts
# user can comment on posts
# user can like posts
# events if user interacts with certain posts
# log which posts user does not interact with
# theme can be it slowly gets weirder? or more surreal??