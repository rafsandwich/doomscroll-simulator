import random
import sys
import time

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

# dictionary for tracking posts rarity percentage
post_rarity = {
    "Common" : 67,
    "Uncommon" : 25,
    "Rare" : 7,
    "Mythical" : 1
}

# dict for how many times the user has encountered each rarity
rarity_appearances = {
    "Common" : 0,
    "Uncommon" : 0,
    "Rare" : 0,
    "Mythical" : 0
}

user_comments = [
    "💭 You left a thoughtful comment.",
    "❓ Your comment doesn't seem to work, as if someone has removed it ...",
    "🚩 Your comment got flagged for offensive language.",
    "🚩 Your comment got flagged for misinformation.",
    "💬 Someone replied to your comment: 'L take'",
    "💬 Someone replied to your comment: 'Did you know? The correct definition of the word ...'",
    "❤️ Someone liked your comment immediately!",
    "😔 I don't think anyone will like this comment .."
]

usernames = [
    "🎵💡 SourceOfIllumination 💡🎵",
    "🎸 Randy Sillier Guitar Channel 🎸",
    "Band Triple Turtle 🐢🐢🐢",
    "PBS Sports ⚽",
    "🎅 the Logspast 🧙‍♂️",
    "💧 DryRejective ❌",
    "♣️ turtlecabaret™️",
    "Kafka ✏️✏️",
    "🥧 thickchickenpie 🥧",
]

# user data dictionary for how the user is interacting
user_data = {
    "likes" : 0,
    "comments" : 0,
    "ignored_posts" : -1,
}

post_speed = 0.002
prompt_speed = 0.01
caution_speed = 0.05

def text_effect(text, speed):
    """For printing text with a typing-type effect"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush() # remove the buffer
        time.sleep(speed)

def load_ascii_art(filename="ascii_art.txt"):
    """Loads ASCII art from a text file and returns a list of drawings.
        All Ascii art sourced from ASCII Art Archive www.asciiart.eu !"""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            art = file.read().strip().split("\n===\n")  # split ASCII by '===' delimiter into a list
            return art
    except FileNotFoundError:
        return ["ASCII art not found"]

def get_post_rarity():
    """Generate a random post rarity, weighted by the values in the post_rarity dict"""
    rarities = list(post_rarity.keys()) # list containing post rarity keys
    weights = list(post_rarity.values()) # list containing post rarity values
    return random.choices(rarities, weights, k=1)[0] # list of rarities, list of weights from keys, pick 1 element, return single element from output list

def generate_post(scroll_count, username):
    """Generate a random post, changing by the amount the user has scrolled"""
    level = min(scroll_count // 5, len(post_levels) -1) # increase level every 5 scrolls, and ensure it doesn't go out of bounds when checking post_levels[level]

    targeted_posts = [
        f"Why does @{username} keep commenting so much?",
        f"I've got a really obsessive fan, their name starts with {username[0]} and ends with {username[-1]}...",
        f"What are you searching for, {username}?",
        f"Mx. {username[0].upper()}, I've changed the ads for you. ☣️ I hope you like it."
    ]

    if user_data["comments"] >= 5 and random.random() <0.1: # if user has made enough comments, 10% chance they get a targeted post
        post = random.choice(targeted_posts)
    else:
        post = random.choice(post_levels[level]) # else, get a post for the level they are currently on

    user = random.choice(usernames)

    ascii_art = random.choice(ascii_art_list)

    rarity = get_post_rarity()
    rarity_appearances[rarity] += 1

    # handling 'drawing' the post and its associated contents
    text_effect("\n"+"="*len(post)+"\n", post_speed)
    text_effect(user+"\n", post_speed)
    text_effect("-"*len(post)+"\n", post_speed)
    print(ascii_art)
    text_effect(post+"\n", post_speed)
    text_effect("-"*len(post)+"\n", post_speed)
    text_effect(f"💬 {random.randint(1,100)} comments | ❤️ {random.randint(1,9999)} likes"+"\n", post_speed)
    text_effect("-"*len(post)+"\n", post_speed)
    if rarity == "Common":
        text_effect(f"This post is {rarity} quality. 🟢\n", post_speed)
    elif rarity == "Uncommon":
        text_effect(f"This post is {rarity} quality, nice find! 🔵\n", post_speed)
    elif rarity == "Rare":
        text_effect(f"🟣 Woah, this post is {rarity} quality - those are very hard to come by! 🟣\n", prompt_speed)
    elif rarity == "Mythical":
        text_effect(f"🟠 ❗❗🎊 DING DING DING! This is a 🏅~ {rarity} ~🏅 quality post. Exceptionally hard to find - well done! 🎊❗❗ 🟠\n", caution_speed)


def doomscroll():
    """Main doomscroll loop"""
    scroll_count = 0
    liked = False
    commented = False

    ignored_warning = False
    
    text_effect("🛡️ To create an account, please enter a username: ", prompt_speed)
    username = input()
    text_effect("📶 Connecting ... ... ✅\n", caution_speed)

    print("\n🛜 Welcome to DOOMS. Type 'scroll' to continue, 'like' to like, 'comment' to comment, or 'stop' to exit.")

    while True:
        command = input("\n> ").lower()

        if command == "scroll":

            if not liked and not commented:
                user_data["ignored_posts"] += 1 # increment in user data if the user ignored the post
            
            generate_post(scroll_count, username)
            scroll_count += 1

            if user_data["ignored_posts"] == 6 and not ignored_warning:
                text_effect("\n🧠 DOOMS is trying harder to get your attention ...\n", prompt_speed)
                ignored_warning = True

            if scroll_count == 5:    # level 1
                text_effect("\n⚠️ Caution: Unconfirmed reports of 'oddities' are being reported by DOOMS powerusers tonight. \n", caution_speed)
            elif scroll_count == 10: # level 2
                text_effect("\n🔺 WARNING: DOOMS is UNST4BLE. All users are suggested to LOG OFF IMMEDIATELY. \n", caution_speed)
            elif scroll_count == 15: # level 3
                text_effect("\n🚨 SYSTEM ERROR: DO0MS I- OFFL1NE. US-RS -T1-L 0-LIN- PR3-4RE 40R -X-RACT10N. 🚨 \n", caution_speed)
            if scroll_count == 20: # break free?

                print("-- maybe a function here for displaying stats, and then can call it if 'stop' is used as well. --")

            liked = False
            commented = False

        elif command == "like" and scroll_count > 0:
            if liked:
                print("\n❗ You've already liked this post! ")
            else:
                liked = True
                user_data["likes"] += 1

                print("\n❤️ You liked the post! ")

        elif command == "comment" and scroll_count > 0:
            if commented:
                print("\n❗ You've already commented on this post! ")
            else:
                commented = True
                user_data["comments"] += 1

                print("\n"+random.choice(user_comments))

        elif command == "stop":
            print("\n♾️ You have escaped the scrolling, for now .. \n")
            print(f"You scrolled through {scroll_count} post(s)!")

            if user_data["ignored_posts"]== -1: # if user stops instantly, correct ignored_posts to 0
                user_data["ignored_posts"] = 0
            print(user_data)
            print(rarity_appearances)
            break

        else:
            print("Invalid command. Please try 'scroll', 'like', 'comment' or 'stop'.")

ascii_art_list = load_ascii_art()
doomscroll()


# add ascii art for post on CLI

# move posts to a separate file

# theme can be it slowly gets weirder? or more surreal?? -> introduced levels,

# stop users from using 'stop' if they have scrolled too far, and maybe pass a random check to actually escape the program

# stats command to display rarities encountered amongst other things
# add secret commands:
    # >help >free >dooms 
    # other commands hidden in certain posts, like user finds weird string -> >dksoka -> does something weird