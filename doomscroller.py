def doomscroll():
    """Main doomscroll loop"""
    scroll_count = 0
    print("Welcome to DOOMS. Type 'scroll' to continue, or 'stop' to exit")

    while True:
        command = input("> ").lower()

        if command == "scroll":
            print("Random placeholder content!")
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