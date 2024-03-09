import os
try:
    import requests, colorama
    from colorama import Fore,Back,Style
    import time
except ModuleNotFoundError:
    print("[!] Some Modules Were Not Found")
    os.system("pip install requests")
    os.system("pip install colorama")
    os.system("pip install time")
    import requests, colorama
    from colorama import Fore,Back,Style
    import time

    print(Fore.GREEN + "[+] Installed Missing Modules")

print(Fore.CYAN + """
  _______    _                 _____ _               _             
 |__   __|  | |               / ____| |             | |            
    | | ___ | | _____ _ __   | |    | |__   ___  ___| | _____ _ __ 
    | |/ _ \| |/ / _ \ '_ \  | |    | '_ \ / _ \/ __| |/ / _ \ '__|
    | | (_) |   <  __/ | | | | |____| | | |  __/ (__|   <  __/ |   
    |_|\___/|_|\_\___|_| |_|  \_____|_| |_|\___|\___|_|\_\___|_|   
                                                                   
    Made By ISellStuff
      
      1.Check Tokens
      2.Exit                                                               """)

op = input("[>] ")
if op == '2':
    time.sleep(1.5)
    print(Fore.RED + "[+] Closing....")
    quit()

def check(token):
    headers = {
         'Authorization':f'{token}',
         'Referer':'https://discord.com/channels/@me',
         'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0',
          'X-Debug-Options':'bugReporterEnabled',
            'X-Discord-Locale':'en-US',
            'X-Discord-Timezone':'America/Los_Angeles',
            'X-Super-Properties':'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyMi4wLjAuMCBTYWZhcmkvNTM3LjM2IEVkZy8xMjIuMC4wLjAiLCJicm93c2VyX3ZlcnNpb24iOiIxMjIuMC4wLjAiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MjczNTA3LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ=='

     }
    r = requests.get("https://discord.com/api/v9/users/@me/billing/country-code", headers=headers)
    if r.status_code == 200:
        hits = open('valid_tokens.txt','a')
        hits.write(f"[Valid Token]: {token}\n")
        print(Fore.GREEN + f"[+] Valid Token: {token}")
    elif r.status_code == 401:
        print(Fore.RED + f"[!] Invalid Token: {token}")
    else:
        print(Fore.YELLOW + "[!] Warning Rate Limited")
file = open('tokens.txt','r').readlines()
for i in file:
    seq = i.strip()
    tokenn = seq.split(":")
    check(tokenn[0])
print()
input(Fore.GREEN + "[+] Valid Tokens Sent To Valid_Tokens.txt")
