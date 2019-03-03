import random
import string
from colorama import init, Fore, Back, Style
import colorama
init(convert=True)

text = '''
     /\       (_)      | \ | (_) |              / ____|                         | |            
    /  \   _____ _ __  |  \| |_| |_ _ __ ___   | |  __  ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
   / /\ \ |_  / | '__| | . ` | | __| '__/ _ \  | | |_ |/ _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
  / ____ \ / /| | |    | |\  | | |_| | | (_) | | |__| |  __/ | | |  __/ | | (_| | |_ (_) | |   
 /_/    \_\___|_|_|    |_| \_|_|\__|_|  \___/   \_____|\___|_| |_|\___|_|  \__,_|\__\___/|_|   
'''

print(Fore.CYAN + text + Fore.WHITE)
f = open('nitro_codes.txt', 'a')
print()
print(Fore.CYAN + '# Codes: ')
amount = int(input())
fix = 1
while fix <= amount:
    code = ('').join(random.choices(string.ascii_letters + string.digits, k=16))
    discord_url = "https://discordapp.com/gifts/"
    f.write(discord_url + code + '\n')
    discord_code = discord_url + code
    print(Fore.GREEN + discord_code)
    fix += 1