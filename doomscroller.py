import random
import sys
import time

# storing glitchy text out the way because it makes the program hard to read!
weird_text = [



    "e̮̎͟͞n̵̪̜̖͙̪͙̹̤͚̰̞̰͂ͧ̒͛͂ͦ̈́ͩͥ̾̈̄̍͆̓̔̃͐̉̊ͪ͂̕j̧̨̛͔̱̱͓̦̘̟̹͎͆̇͆̄̌͋́̒̆͑͛͋_̸̵̸̛̩͇̗̫̫̲̯̇ͩͬ̓̊͑͋̎͞o̸̷̢̨̗͚̥͉͔̺͈̊́̋͛ͥ̀͌ͫͩ͌ͣͧ̀̿̔̈́̈y̧̨̝̼̜͉̥̾͂͗͠͠"
]

# text for when the user tries to escape the program after going to deep
escape_text = [
    "W༙྇H༙྇E༙྇R༙྇E༙྇ A༙྇R༙྇E༙྇ Y༙྇O༙྇U༙྇ G༙྇O༙྇I༙྇N༙྇G༙྇ .༙྇.༙྇.༙྇ S༙྇T༙྇A༙྇Y༙྇ L༙྇O༙྇N༙྇G༙྇E༙྇R༙྇",
    "D҉O҉N҉'҉T҉ L҉E҉A҉V҉E҉",
    "💀𝔜𝙾𝔘 ℭ𝙰𝔑'𝔗 𝔖𝚃𝔒𝙿 𝚃ℌ𝙸𝔖💀",



    "N̴̨̺̻̤͉̱̐͛ͯ͛ͤ̂ͬͭ͆͘̕̕O̶̴̸̸̦̱͈̳͈̤̿̾ͬ̌̈͆ͩ̽ͨͮ̿͡",


    "𐌙Ꝋ𐌵'𐌐𐌄 𐌍Ꝋ𐌕 ᏵꝊ𐌉𐌍Ᏽ 𐌀𐌍𐌙Ꮤ𐋅𐌄𐌐𐌄"
]

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
    "scrolled" : 0,
    "secrets_found" : 0
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

def display_stats():
    """Display stats from users session"""

    print(f"\nYou've scrolled through {user_data['scrolled']} post(s)! 📺")
    print(f"You've made {user_data['comments']} comment(s) 💬 and {user_data['likes']} like(s) ❤️.")
    
    if rarity_appearances["Mythical"] > 0:
        print(f"\nWhat a huge achievement, you encounted {rarity_appearances['Mythical']} Mythical post(s)! 🎉🟠🍾")
    print("\n🔵🟢 Here's a breakdown of your scrolled posts rarity: 🟣🟠")
    for rarity, value in rarity_appearances.items():
        print(rarity + ": " + str(value))
    
    if user_data["secrets_found"] == 0:
        print("\nYou have not found any secrets ... ❓")
    else:
        print(f"\nGood work, you found {user_data['secrets_found']} secret(s). 🔎")


def doomscroll():
    """Main doomscroll loop"""

    scroll_count = 0
    liked = False
    commented = False

    dooms_found = False
    free_flag = False
    log_off_found = False

    ignored_warning = False
    
    text_effect("🛡️ To create an account, please enter a username: ", prompt_speed)
    username = input()
    text_effect("📶 Connecting ... ... ✅\n", caution_speed)

    print("\n🛜 Welcome to DOOMS. Type 'scroll' to continue, 'help' for other commands, or 'stop' to exit.")

    while True:
        command = input("\n> ").lower()

        if command == "scroll":

            if not liked and not commented:
                user_data["ignored_posts"] += 1 # increment in user data if the user ignored the post
            
            generate_post(scroll_count, username)
            scroll_count += 1
            user_data["scrolled"] += 1

            if user_data["ignored_posts"] == 6 and not ignored_warning:
                text_effect("\n🧠 DOOMS is trying harder to get your attention ...\n", prompt_speed)
                ignored_warning = True

            if scroll_count == 5:    # level 1
                text_effect("\n⚠️ Caution: Unconfirmed reports of 'oddities' are being reported by DOOMS powerusers tonight. \n", caution_speed/1.5)
            elif scroll_count == 10: # level 2
                text_effect("\n🛑 WARNING: DOOMS is UNST4BLE. All users are suggested to LOG OFF IMMEDIATELY. \n", caution_speed)
            elif scroll_count == 15: # level 3
                text_effect("\n🚨 SYSTEM ERROR: DO0MS I- OFFL1NE. US-RS -T1-L 0-LIN- PR3-4RE 40R -X-RACT10N. 🚨 \n", caution_speed)
            elif scroll_count == 25:

                text_effect(f"""\n𝚆𝙴𝙻𝙲𝙾𝙼𝙴 𝚃𝙾 𝚃𝙷𝙴 ☠ 𝙽𝙴𝚆 ☠ 𝙾𝚁𝙳𝙴𝚁 {username.upper()}.

                ŦɎ₱Ɇ ░F░R░E░E░ 𝔞𝔫𝔡 𝔴𝔢 𝔴𝔦𝔩𝔩 𝔦𝔪𝔭𝔞𝔯𝔱 𝚘𝚗 𝚢𝚘𝚞 𝚊 𝔤𝔦𝔣𝔱.""", caution_speed/1.5)
                free_flag = True

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
            if scroll_count >= 15:
                if random.random() < 0.3: # pass a random check if you've scrolled too far
                    print("\n♾️ It was hard .. but you have escaped the scrolling, for now ... ♾️")
                    display_stats()
                    break
                else:
                    text_effect("\n" + random.choice(escape_text) +"\n", caution_speed)
            else:
                print("\n♾️ You have escaped the scrolling, for now ... ♾️")
                display_stats()
                break
        
        elif command == "stats":
            display_stats()
            pass
        
        elif command == "help":
            print("\n'scroll': scroll to the next post.")
            print("'like': like the current post, providing one is there.")
            print("'comment': comment on the current post, providing one is there.")
            print("'stop': stop the program and exit DOOMS.")
            print("'help': display other commands .. but not all of them.")
            print("'stats': display stats from the users current session.")

        elif command == "log off" and not log_off_found:
            text_effect("\nYou log off ... But you're still here. 🔒\n", caution_speed)
            user_data["secrets_found"] += 1
            log_off_found = True

        elif command == "dooms" and not dooms_found:
            text_effect("\n🎈 Something is going to happen tonight ...\n", caution_speed)
            user_data["secrets_found"] += 1
            dooms_found = True

        elif command == "free" and free_flag:
            print(weird_text[0])
            user_data["secrets_found"] += 1
            free_flag = False

        else:
            print("⛔ Invalid command. Please try 'help' for available options.")

ascii_art_list = load_ascii_art()
doomscroll()


# move posts to a separate file
# other commands hidden in certain posts, like user finds weird string -> >dksoka -> does something weird / increase secret count
# theme can be it slowly gets weirder? or more surreal?? -> introduced levels,

# FUTURE IDEAS
# you have to find a key to log off

