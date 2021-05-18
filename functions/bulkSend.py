import requests, os, sys
from colorama import Fore, Back, Style

def bulkSend(nums, msg, apiKey):
    failed=[]
    count=0
    for i in nums:
        count+=1
        resp = requests.post('https://textbelt.com/text', {
            'phone': i,
            'message': msg,
            'key': apiKey,
        })
        result= resp.json()
        res= str(result['success'])
        if res == 'False':
            stats= Fore.RED+'Failed'+Style.RESET_ALL
        else:
            stats= Fore.GREEN+'Success'+Style.RESET_ALL
        print(Fore.GREEN+'\033[1m>> [{}] '.format(count)+'Target: {}'.format(Fore.BLUE+i)+Fore.GREEN+'\tStatus: {}'.format(stats)+Fore.GREEN+'\t\033[1mRemaining: {}'.format(result['quotaRemaining']) ,end='\r')
        if res == "False":
            failed.append(i)
    filename= os.path.join( os.getcwd(), 'error_log.txt')
    file = open(filename, 'w')
    for x in failed:
        file.write(x+'\n')
    success= len(nums) - len(failed)
    print(Fore.GREEN+'\033[K\033[1m>> '+Fore.YELLOW+'Total: {}'.format(len(nums))+Fore.GREEN+'\tSuccess: {}'.format(success)+Fore.RED+'\t Failed: {}'.format(len(failed))+Fore.GREEN+'\tRemaining: {}'.format(result['quotaRemaining'])+Style.RESET_ALL)
    print(Fore.GREEN+'\033[1m>> Failed Numbers Stored in'+Fore.YELLOW+' error_log.txt'+Style.RESET_ALL)
    sys.exit()