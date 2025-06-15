#!/bin/python3

# imports libraries
import requests
import pyfiglet
import sys
from termcolor import colored
import urllib3
from urllib.parse import parse_qsl

# Banner
print()
print(colored(pyfiglet.figlet_format("pybrute", font="slant"), color="blue"))
print(colored("Built By Jahid Hasan", color="green"))
print()

# important message
print(colored(f"""
    *************************************************************
    * Enter all POST parameters you want to use in this format: *
    *                                                           *        
    * param1=value1&param2=value2&param3=value3                 *
    *                                                           *                
    * Use {colored("^USER^", color="white")} {colored("for username placeholder", color='red')}                       {colored("*", color='red')}                
    {colored("*", color='red')} {colored("Use", color='red')} {colored("^PASS^", color="white")} {colored("for password placeholder", color='red')}                       {colored("*", color='red')}                        
    {colored("*************************************************************", color='red')}
    """, color='red'))


# BruteForce Modes
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
    print(colored("[*] Sniper Mode Activate", color='blue'))

    try:
        url = input(colored("Enter your target url: ", color="cyan"))
        param_template = input(colored("Enter post data template: ", color='cyan'))
        username = input(colored("Enter valid username: ", color='cyan'))
        password_list = input(colored("Enter passlist path: ", color='cyan'))
    except KeyboardInterrupt:
        print("\nexit")
        exit()
    print()

    # password list
    try:
        with open(password_list, 'rt') as f:
            password = []
            for line in f:
                password.append(line.strip())
    except FileNotFoundError:
        print(colored("password file not found", color="red"))
        exit()

    for passwd in password:
        post_data_string = param_template.replace("^USER^", username).replace("^PASS^", passwd)
        post_data = dict(parse_qsl(post_data_string))

        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        try:
            response = requests.post(url, headers=headers, data=post_data)
        except requests.exceptions.ConnectionError:
            print(colored("please enter valid url", color='red'))
            exit()

        except urllib3.exceptions.NameResolutionError:
            print(colored("please enter valid url", color='red'))
            exit()
        r_len = len(response.text)
        r_text = response.text.lower()

        if r_len > 5666:
            print(colored(f"[+] login successful {username}:{passwd}", color='green'))
            break

        elif "dashboard" in r_text or "logout" in  r_text:
            print(colored(f"[+] login successful {username}:{passwd}", color="green"))
            break

        else:
            print(colored(f"[-] faild attampt {username}:{passwd}", color='red'))
    else:
        print(colored("no valid credential found", color='red'))
        

# Cluster Bomb Mode
if mode == "2":
    print(colored("[*] Cluster Bomb Mode Activate", color="blue"))

    try:
        url = input(colored("Enter your target url: ", color="cyan"))
        param_template = input(colored("Enter post data template: ", color="cyan"))

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
            post_data_str = param_template.replace("^USER^", user).replace("^PASS^", passwd)
            post_data = dict(parse_qsl(post_data_str))
            try:
                response = requests.post(url, data=post_data)

            except requests.exceptions.RequestException as e:
                print("Request failed:", e)
                exit()
            except requests.exceptions.ConnectionError:
                print(colored("please enter valid url", color='red'))
                exit()

            except urllib3.exceptions.NameResolutionError:
                print(colored("please enter valid url", color='red'))
                exit()
            r_len = len(response.text)
            r_text = response.text.lower()

            if r_len > 5666:
                print(colored(f"[+] login successful {user}:{passwd}", color="green"))
                found = True
                break

            elif "dashboard" in r_text or "logout" in r_text:
                print(colored(f"[+] login successful {user}:{passwd}", color="green"))
                found = True
                break

            else:
                print(colored(f"[-] faild attampt {user}:{passwd}", color="red"))
        else:
            continue
        break

    if not found:
        for passwd in password:
            for user in username:
                post_data_str = param_template.replace("^USER^", passwd).replace("^PASS^", user)
                post_data = dict(parse_qsl(post_data_str))

                try:
                    response = requests.post(url, data=post_data)

                except requests.exceptions.ConnectionError:
                    print(colored("please enter valid url", color='red'))
                    exit()


                except urllib3.exceptions.NameResolutionError:
                    print(colored("please enter valid url", color='red'))
                    exit()

                r_len = len(response.text)
                r_text = response.text.lower()

                if r_len > 5666:
                    print(colored(f"login successful {passwd}:{user}", color="green"))
                    exit()

                elif "dashboard" in r_text or "logout" in r_text:
                    print(colored(f"[+] login successful {passwd}:{user}", color="green"))
                    exit()

                else:
                    print(colored(f"[-] faild attampt {passwd}:{user}", color="red"))
            else:
                continue
            break
        else:
            print(colored(f"no valid credential", color="red"))
            

# PitchFork Mode
if mode == "3":
    print(colored("[*] PitchFork Mode Activate", color="blue"))

    try:

        url = input(colored("Enter your target url: ", color="cyan"))
        param_template = input(colored("Enter post data template:  ", color="cyan"))
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
        post_data_str = param_template.replace("^USER^", user).replace("^PASS^", passwd)
        post_data = dict(parse_qsl(post_data_str))

        try:
            response = requests.post(url, data=post_data)
        except requests.exceptions.ConnectionError:
            print(colored("please enter valid url", color='red'))
            exit()

        except urllib3.exceptions.NameResolutionError:
            print(colored("please enter valid url", color='red'))
            exit()

        r_len = len(response.text)
        r_text = response.text.lower()

        if r_len > 5666:
            print(colored(f"[+] login successful {user}:{passwd}", color="green"))
            break

        elif "dashboard" in r_text or "logout" in r_text:
            print(colored(f"[+] login successful {user}:{passwd}", color="green"))
            break

        else:
            print(colored(f"[-] faild attampt {user}:{passwd}", color="red"))

    else:
        print(colored(f"no valid credential found", color="red"))

