# discord lookup tool made by erwin
import os
import requests
from colorama import Fore, Back, Style
import ctypes

def main_menu():
    os.system("cls")
    ctypes.windll.kernel32.SetConsoleTitleW("simpylookup | id & invite lookup")
    print(Fore.BLUE + """
     _                       _             _                
 ___(_)_ __ ___  _ __  _   _| | ___   ___ | | ___   _ _ __  
/ __| | '_ ` _ \| '_ \| | | | |/ _ \ / _ \| |/ / | | | '_ \ 
\__ \ | | | | | | |_) | |_| | | (_) | (_) |   <| |_| | |_) |
|___/_|_| |_| |_| .__/ \__, |_|\___/ \___/|_|\_\\\\__,_| .__/ 
                |_|    |___/                         |_|    
""", Style.RESET_ALL)
    print("What do you want to Lookup?")
    print("1. User")
    print("2. Invite")
    choice = input("Select an option (1/2): ")
    if choice == '1':
        option_1()
    elif choice == '2':
        option_2()
    else:
        print("Please select a valid option.")
        main_menu()

def option_1():
    user = input("User-id: ")
    print("Request send to api...")
    response = requests.get(f"https://discordlookup.mesavirep.xyz/v1/user/{user}")
    if response.status_code == 200:
        user_data = response.json()
        print("")
        print(Fore.GREEN + "Received user data:")
        print("User ID:", user_data["id"])
        print("Tag:", user_data["tag"])
        print("Global Name:", user_data["global_name"])
        print("Badges:", user_data["badges"])
        avatar = user_data["avatar"]
        print("Avatar ID:", avatar["id"])
        print("Avatar Link:", avatar["link"])
        print("Is Avatar Animated:", avatar["is_animated"])
        banner = user_data["banner"]
        print("Banner ID:", banner["id"])
        print("Banner Link:", banner["link"])
        print("Is Banner Animated:", banner["is_animated"])
        print("Banner Color:", banner["color"])
        print(Style.RESET_ALL)
        input("Press Enter to go back...")
        main_menu()
    else:
        print("")
        print(Fore.RED + "Request failed with status code:", response.status_code)
        print(Style.RESET_ALL)
        input("Press Enter to go back...")
        main_menu()

def option_2():
    while True:
        print("")
        print("What Invite type do you want to Lookup?")
        print("1. Vanity")
        print("2. Code")
        
        choice = input("Enter your choice (1/2): ")
      
        if choice == "1":
            invite = input("discord.gg/")
            print("Request sent to the API...")
            response = requests.get(f"https://discord.com/api/invites/{invite}")
            if response.status_code == 200:
                json_data = response.json()
                print("")
                print(Fore.GREEN + "Received JSON data:")
                print("Type:", json_data["type"])
                print("Code:", json_data["code"])
                print("Guild Name:", json_data["guild"]["name"])
                print("Guild ID:", json_data["guild"]["id"])
                print("Guild Description:", json_data["guild"]["description"])
                print(Style.RESET_ALL)
                input("Press Enter to go back...")
                main_menu()
            else:
                print("")
                print(Fore.RED + "Request failed with status code:", response.status_code)
                print(Style.RESET_ALL)
                input("Press Enter to continue...")
                main_menu()
        elif choice == "2":
            invite = input("discord.gg/")
            print("Request sent to the API...")
            response = requests.get(f"https://discord.com/api/invites/{invite}")
            if response.status_code == 200:
                json_data = response.json()
                print("")
                print(Fore.GREEN + "Received JSON data:")
                print("Type:", json_data["type"])
                print("Code:", json_data["code"])
                print("Inviter ID:", json_data["inviter"]["id"])
                print("Inviter Username:", json_data["inviter"]["username"])
                print("Guild Name:", json_data["guild"]["name"])
                print("Guild ID:", json_data["guild"]["id"])
                print("Guild Description:", json_data["guild"]["description"])
                print(Style.RESET_ALL)
                input("Press Enter to go back...")
                main_menu()
            else:
                print("")
                print(Fore.RED + "Request failed with status code:", response.status_code)
                print(Style.RESET_ALL)
                input("Press Enter to continue...")
                main_menu()
        else:
            print("Invalid choice. Please enter '1' or '2'.")

if __name__ == "__main__":
    main_menu()