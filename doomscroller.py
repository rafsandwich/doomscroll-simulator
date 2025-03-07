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
    "SourceOfIllumination",
    "Randy Sillier Guitar Channel",
    "Band Triple Turtle",
    "PBS Sports",
    "the Logspast",
    "DryRejective",
    "turtlecabaret",
    "Kafka",
    "thickchickenpie",
]

# user data dictionary for how the user is interacting
user_data = {
    "likes" : 0,
    "comments" : 0,
    "ignored_posts" : -1,
}

post_speed = 0.002
caution_speed = 0.05

def text_effect(text, speed):
    """For printing text with a typing-type effect"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush() # remove the buffer
        time.sleep(speed)

def generate_post(scroll_count):
    """Generate a random post, changing by the amount the user has scrolled"""
    level = min(scroll_count // 5, len(post_levels) -1) # increase level every 5 scrolls, and ensure it doesn't go out of bounds when checking post_levels[level]
    post = random.choice(post_levels[level])
    user = random.choice(usernames)

    text_effect("\n"+"="*len(post)+"\n", post_speed)
    text_effect(user+"\n", post_speed)
    text_effect("-"*len(post)+"\n", post_speed)
    text_effect(post+"\n", post_speed)
    text_effect("-"*len(post)+"\n", post_speed)
    text_effect(f"💬 {random.randint(1,100)} comments | ❤️ {random.randint(1,9999)} likes"+"\n", post_speed)
    text_effect("-"*len(post)+"\n", post_speed)



def doomscroll():
    """Main doomscroll loop"""
    scroll_count = 0
    liked = False
    commented = False

    print("\n🛜 Welcome to DOOMS. Type 'scroll' to continue, 'like' to like, 'comment' to comment, or 'stop' to exit.")

    while True:
        command = input("\n> ").lower()

        if command == "scroll":

            if not liked and not commented:
                user_data["ignored_posts"] += 1 # increment in user data if the user ignored the post
            
            generate_post(scroll_count)
            scroll_count += 1                # put before generate_post? investigate

            if scroll_count == 5: # level 1
                text_effect("\n⚠️ Caution: Unconfirmed reports of oddities are being reported by DOOMS powerusers tonight. \n", caution_speed)
            elif scroll_count == 10: # level 2
                text_effect("\n🔺 WARNING: DOOMS is UNST4BLE. All users are suggested to LOG OFF IMMEDIATELY. \n", caution_speed)
            elif scroll_count == 15: # level 3
                text_effect("\n🚨 SYSTEM ERROR: DO0MS I- OFFL1NE. US-RS -T1-L 0-LIN- PR3-4RE 40R -X-RACT10N. 🚨 \n", caution_speed)

            liked = False
            commented = False

        elif command == "like" and scroll_count > 0:
            if liked:
                print("❗ You've already liked this post! ")
            else:
                liked = True
                user_data["likes"] += 1

                print("❤️ You liked the post! ")

        elif command == "comment" and scroll_count > 0:
            if commented:
                print("❗ You've already commented on this post! ")
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
            break

        else:
            print("Invalid command. Please try 'scroll', 'like', 'comment' or 'stop'.")

doomscroll()


# add ascii for post layout on CLI
# move posts to a separate file
# user commenting on particular posts creates certain responses
# user liking certain posts creates certain responses
# if user ignores certain posts, create a response
# theme can be it slowly gets weirder? or more surreal?? -> introduced levels,
# different rarity of posts, like basic, uncommon etc. and 'random' choice reflects rarity