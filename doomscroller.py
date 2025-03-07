import random

posts = [
    "I was just trying to clear my acne .. *cut to cutting board*",
    "'what do you think it's gonna be?', 'i'm the uncle i think it'll be a girl say less' #boyorgirl?",
    "AI generated food baffles cuisine experts, quoted saying 'I can't believe it's not butter'"

]

def generate_post(scroll_count):
    """Generate a random post, changing by the amount the user has scrolled"""
    level = scroll_count // 5 # not yet used
    post = random.choice(posts)
    return post

def doomscroll():
    """Main doomscroll loop"""
    scroll_count = 0
    print("Welcome to DOOMS. Type 'scroll' to continue, or 'stop' to exit.")

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