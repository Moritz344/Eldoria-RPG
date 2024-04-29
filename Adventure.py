import sys
import time
from termcolor import cprint
import os
import random
import json 

def follower_text_animation(text):
     for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)
     print()

def loading_text(text):
    for i in text:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.5)
    print()

def save_account(name,age):
    # saved nur die accounts schreibt nur an json datei
    data = []
    if os.path.exists("accounts.json"):
        with open("accounts.json", "r") as file:
            data = json.load(file)
    data.append({"name": name, "age": age})
    with open("accounts.json","w") as file:
        json.dump(data,file)
def load_accounts():
    cprint("Type 'back' to get back to the main menu.","grey")
    cprint("Type 'play' to start the game","grey")
    print()
    MAX_ACCOUNTS = 1
    # schreibt alle accounts
    if os.path.exists("accounts.json"):
        with open("accounts.json","r") as file:
            data = json.load(file)
            if not data:
                print("no accounts found.")
            else:
                print("Saved Accounts:")
                for index, account in enumerate(data, 1):
                    print(f"{index}. Name: {account['name']}, Age: {account['age']}")
            print()
    else:
        print("No accounts found.")
    if len(data) > MAX_ACCOUNTS:
        print(f"You have reached the maximum number of accounts ({MAX_ACCOUNTS})")
        print(f"Please delete one. You can do that in the 'Delete Accounts' tab.")
        print()
        master = str(input("< "))
        if master == "back":
            play_game()
        else:
            master = str(input("< "))
            

    master = input("< ")
    if master == "back":
        play_game()
    elif master == "play":
        play_tab()

def delete_accounts():
    if os.path.exists("accounts.json"):
        with open("accounts.json","r") as file:
            data = json.load(file)
            print(data)
        print()
    print("Which Account would you like to delete?")
    print()
    delete_index = int(input("< "))
    with open("accounts.json") as file:
        data = json.load(file)
    if 1 <= delete_index <= len(data):
        deleted_account = data.pop(delete_index - 1)
        print(f"Deleted Account: Name: {deleted_account['name']}, Age: {deleted_account['age']}")
        with open("accounts.json","w") as file:
            json.dump(data,file)
        print("Account deleted successfully.")
    else:
        print("Invalid account number. No account deleted")
    time.sleep(0.9)
    play_game()
def newgame():
    follower_text_animation("What is your name?")
    name = str(input("< "))
    print()
    follower_text_animation("How old are you?")
    print()
    age = int(input("< "))
    print()
    save_account(name,age)
    follower_text_animation("Your Profile is saved.")
    play_game()
def play_tab():
    try:
        os.system("cls" if os.name == "nt" else "clear")
        if os.path.exists("accounts.json"):
            with open("accounts.json","r") as file:
                data = json.load(file)
                for account in data:
                    loading_text((account['name']))
                    follower_text_animation("Rang: A Tier")
                    follower_text_animation("Beruf: Abenteurer")
                    follower_text_animation("Fähigkeiten: Uknown")
                    cprint("Look at your bagpack!","green",attrs=["bold"])
    except Exception:
        print("Error")

    intro()
    print("+------------------------+")
    cprint("QUEST ACCEPTED","green")
    print("Information: Find the lost juwel. ")
    print("+------------------------+")
    cprint("type 'start' to start the quest and your adventure.","grey")
    cprint("type 'help' to see all commands you need.","grey")
    du = input("< ")
    if du == "start":
        day_1()
    elif du == "help":
        cprint("1. Backpack","green")
        cprint("2. Map","green")
    else:
        du = input("< ")
def intro():
    follower_text_animation("""
In a distant world called Eldoria,
there once existed a powerful jewel
known as "The Crystal of Eternity".
This jewel had the ability to maintain 
the balance of the elements and bring peace to the land.
However, many years ago, the Crystal was stolen and hidden
in the depths of an enchanted forest.""")
    follower_text_animation("""
As you are about to accept a new quest at the Guild as usual,
the door of the Guild swings open, and you see five knights and
a woman standing before you.
                            """)
    time.sleep(0.5)
    follower_text_animation("""

The woman is a general in the service of the King.
She informs you that the King has requested your presence urgently.
Without hesitation, you follow her as she leads you through the bustling
streets of the kingdom, towards the grand palace where the fate of Eldoria is decided.""")
    cprint("King: I choose you, hero! You, as the strongest, shall save us!","yellow",attrs=["bold"])
    time.sleep(0.5)
    follower_text_animation("What? no this is not happening...")
    time.sleep(1)
    follower_text_animation("I just wanted to live a peacfully live.")
    time.sleep(0.5)
    follower_text_animation("And now I have to save the world by my own? ...")
    time.sleep(1)
def day_1():
    # 1 - 7
    DRAGON = 10
    SWORD = -10
    LEVEL = 54
    follower_text_animation("""
    As you sit within the confines of the carriage,
    the landscape outside whizzes by in a blur of greenery
    and distant mountains.
                            """)
    cprint("The King gave you a letter with more Information about the special quest.","green",attrs=["bold"])
    print("Open(Y/n)")
    du = str(input("< "))
    if du == "Y":
        cprint("""
        
            +----------------------------------------------+
            - Find the juwel
            - The juwel is located in the demonic continent
              in the heart of the enchanted forest
            +----------------------------------------------+
              ""","black")
    elif du == "n":
        cprint("You stored the letter back in your backpack.","grey",attrs=["bold"])
    time.sleep(1)
    cprint("A Dragon arrives","red",attrs=["bold"])
    print("""
        +--------------------------------------+
        \****__             ____                                              
         |    *****\_      --/ *\-__                                          
         /_          (_    ./ ,/----'                                         
Art by     \__         (_./  /                                                
 Ironwing     \__           \___----^__                                       
               _/   _                  \                                      
        |    _/  __/ )\"\ _____         *\                                    
        |\__/   /    ^ ^       \____      )                                   
         \___--"                    \_____ )                                  
                                          "
        HEALTH: [############################]
        
        +--------------------------------------+
          """)
    print("1. Fight")
    print("2. Run")
    print()
    du = str(input("< "))
    if du == "1":
        print("""
            Backpack:
            +---------------------+

            Sword:
    
                  /| _______________
            O|===|* >_______________>
                  \|
            
            Potions:
              1. Healing
              2. Poison
            +---------------------+
            
              """)
        x = DRAGON - SWORD
        cprint("Your sword did 10 damage","green",attrs=["bold"])
        cprint("Dragon health: 0","red")
        cprint("You won the battle!","green",attrs=["bold"])
        level_up = LEVEL + 20
        follower_text_animation("Your leveled up")
        follower_text_animation("You made 20 Level plus.")
        du = str(input("< "))
    elif du == "2":
        cprint("You flew into the mountains.","green",attrs=["bold"])
        follower_text_animation("You can see the dragon flying to a human village...")
        print("1. Save the Village")
        print("2. Dont save the village")
        
def about_page():
    print("+----------------------------------------------+")
    follower_text_animation("""
In einer fernen Welt namens Eldoria war einst ein mächtiges
Juwel bekannt als "Der Kristall der Ewigkeit". Dieser Juwel 
hatte die Fähigkeit, das Gleichgewicht der Elemente zu 
erhalten und Frieden über das Land zu bringen.Doch vor vielen
Jahren wurde der Kristall gestohlen und in den Tiefen eines 
verzauberten Waldes versteckt.Der Spieler schlüpft in die Rolle eines jungen Abenteurers,
der auserwählt wurde, um die gefährliche Reise anzutreten und
das verlorene Juwel von Eldoria wiederzubeschaffen. 
Auf ihrem Weg begegnen sie faszinierenden Kreaturen, treffen auf
mächtige Zauberer und müssen sich mutig gegen finstere Schurken 
und gefährliche Monster stellen.
""")
    print("+----------------------------------------------+")
    cprint("Type 'back' to get back to the main menu.","grey")
    try:
        user = str(input("< "))
    except Exception:
        print("Please try again.")

    if user == "back":
        play_game()
    else:
        user = str(input("< "))
def quit_page():
    sys.exit(follower_text_animation("See you next time Adventure."))
def play_game():
    os.system("cls" if os.name == "nt" else "clear")
    print("""
     █████████╗    ██████╗ ██████╗██████╗██╗█████╗
     ██╔════██║    ██╔══████╔═══████╔══██████╔══██╗
     █████╗ ██║    ██║  ████║   ████████╔█████████║
     ██╔══╝ ██║    ██║  ████║   ████╔══██████╔══██║
     ████████████████████╔╚██████╔██║  ██████║  ██║
     ╚══════╚══════╚═════╝ ╚═════╝╚═╝  ╚═╚═╚═╝  ╚═╝
      """)
    print("""
     +--------------------------------------------+
                    -- EldoriaRPG --
     +--------------------------------------------+
     1 - Load Game
     2 - Create Game
     3 - About
     4 - Quit Game
     5 - Delete Accounts
     +--------------------------------------------+
      """)
    
    print()
    user = int(input("< "))
    if user == 1:
        load_accounts()
    elif user == 2:
        newgame()
    elif user == 3:
        about_page()
    elif user == 4:
        quit_page()
    elif user == 5:
        delete_accounts()

        
play_game()