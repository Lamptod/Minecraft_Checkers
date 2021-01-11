import requests
from colorama import Fore, Style
print("Choose a name to check for:")
target = input(">> ")
with open("accounts.txt", 'r') as acc:
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
                        r2 = session.get("https://api.minecraftservices.com/minecraft/profile", headers={"Authorization": f"Bearer {token}"})
                        namecheck = r2.json()
                        if target == str(namecheck['name']):
                                print(f"{Fore.GREEN}Found - {username}:{password}")
                else:
                        print(f"{Fore.RED}One of the details you enter is wrong. Try again - {username}")