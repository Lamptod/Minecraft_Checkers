import requests
from time import sleep
from colorama import Fore
amount = 0
with open("accounts.txt", 'r') as acc:
        amount += 1
        accounts = acc.read().splitlines()
        for account in accounts:
                splited = account.split(":")
                username = splited[0]
                password = splited[1]
                payload = {    
                        "username": username,      
                        "password": password,
                }
                session = requests.session()
                r1 = session.post("https://authserver.mojang.com/authenticate", json=payload, headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0", "Content-Type": "application/json"})
                if r1.status_code == 200:
                        x = r1.json()
                        token = x["accessToken"]
                        r2 = session.get("https://api.minecraftservices.com/minecraft/profile/namechange", headers={"Authorization": f"Bearer {token}"})
                        namecheck = r2.json()
                        if namecheck['nameChangeAllowed'] is True:
                                print(f"{Fore.GREEN}Found - {username}:{password}")
                                with open('CanChange.txt', 'a') as cc:
                                        cc.write(f"{account}\n")
                        else:
                               print(f"{Fore.RED}Can't name change - {username}:{password}") 
                else:
                        print(f"{Fore.RED}One of the details you enter is wrong. Try again - {username}")
        if amount == 30:
                amount = 0
                print(f"Sleeping for 1 minute to not get accounts locked/ip banned.")
input(f"{Fore.CYAN}Press enter to continue >> ")