import urllib.request
from colorama import Fore, Back, Style
from functions.getNums import getNums
from functions.bulkSend import bulkSend
from config import API_KEY
import sys
import os.path
print(Fore.GREEN+"""
    ███████╗███╗   ███╗███████╗    ███████╗███████╗███╗   ██╗██████╗ ███████╗██████╗ 
    ██╔════╝████╗ ████║██╔════╝    ██╔════╝██╔════╝████╗  ██║██╔══██╗██╔════╝██╔══██╗
    ███████╗██╔████╔██║███████╗    ███████╗█████╗  ██╔██╗ ██║██║  ██║█████╗  ██████╔╝
    ╚════██║██║╚██╔╝██║╚════██║    ╚════██║██╔══╝  ██║╚██╗██║██║  ██║██╔══╝  ██╔══██╗
    ███████║██║ ╚═╝ ██║███████║    ███████║███████╗██║ ╚████║██████╔╝███████╗██║  ██║
    ╚══════╝╚═╝     ╚═╝╚══════╝    ╚══════╝╚══════╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝"""+Fore.RED+"""                                                                     
    \033[1m★彡[ Author: """+Fore.GREEN+"""akshayitzme """+Fore.RED+"""	      Project: """+Fore.GREEN+"""𝚐𝚒𝚝𝚑𝚞𝚋.𝚌𝚘𝚖/𝚊𝚔𝚜𝚑𝚊𝚢𝚒𝚝𝚣𝚖𝚎/sms-sender"""+Fore.RED+""" ]彡★
""")

def connect(host='http://fast.com'):
    try:
        urllib.request.urlopen(host) #Python 3.x
        return True
    except:
        return False
if connect():
    pass
else:
    print(Fore.RED+'\t\033[1m >> Internet not Connected !')
    sys.exit()
fname= input(Fore.GREEN+'>> Enter Filename: \033[0m')
if os.path.exists(fname):
    msg= input(Fore.GREEN+'\033[1m>> Enter Message: ')
    check=input(Fore.GREEN+'\033[1m>> Confirm to Send ? [ y for yes : n for No ] ')
    if check in ['n', 'N', 'No', 'no', 'NO']:
        sys.exit()
    numsAr= getNums(fname)
    bulkSend(numsAr, msg, API_KEY)
else:
    print(Fore.RED+'\033[1m>> File Doesnt Exist !')
    sys.exit()