"""nitro generator, but its improved"""
import random
import string
import time
import threading
from colorama import init, Fore

ALPHABETS = string.ascii_letters + string.digits

init(convert=True)

def algorithm():
    return "".join([ALPHABETS[int(random.random() * len(ALPHABETS))] for _ in range(16)])
def generator(amount):
    global CODES
    CODES = []
    for _ in range(amount):
        code = "https://discordapp.com/gifts/%s" % algorithm()
        print(f"Code: {code}")
        CODES.append(code)

print("%sCodes:%s " % (Fore.CYAN, Fore.WHITE), end="")
count = int(input())
start = time.time()
thread = threading.Thread(target=generator,args=(count,))
thread.start()
thread.join()
end = round(time.time() - start, 3)
print(f"took {end}s to run")
with open("codes.txt","w") as f: f.write("\n".join(CODES))