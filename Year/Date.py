import requests
from os import path
from time import sleep
from colorama import Fore
amount = 0
with open("accounts.txt", 'r') as acc:
        accounts = acc.read().splitlines()
        for account in accounts:
                amount += 1
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
                        datecheck = r2.json()
                        date = datecheck["createdAt"].split('-')
                        year = date[0]
                        print(f"{Fore.CYAN}{year} {Fore.GREEN}- {username}")
                        with open(f'{year}.txt', 'a') as y:
                                y.write(f"{account}\n")
                else:
                        print(f"{Fore.RED}One of the details you enter is wrong. Try again. - {username}")
                if amount == 30:
                        print(f"{Fore.YELLOW}Sleeping for 1 Minute to not block accounts/block the ip")
                        sleep(60)
input(f"{Fore.CYAN}Press enter to continue >> ")