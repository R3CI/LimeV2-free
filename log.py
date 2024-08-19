from core import *
from core import  __DEBUG__

class log:
    def __init__(self):
        self.res = Fore.RESET
        self.red = Fore.RED
        self.black = Fore.LIGHTBLACK_EX
        self.magenta = Fore.MAGENTA
        self.cyan = Fore.CYAN
        self.lightblue = Fore.LIGHTBLUE_EX
        self.darkblue = Fore.BLUE
        self.purple = Fore.LIGHTMAGENTA_EX
        self.green = Fore.LIGHTGREEN_EX
        self.yellow = Fore.YELLOW

    def gettime(self):
        datetime =  dt.now().strftime(f'{self.black}%H:%M:%S')
        
        return datetime
    
    def check_db(thong: str) -> tuple[bool, str]:
        db = {
            '10014': 'Unknown emoji',
            '30010': 'Max reactions',
            '40007': 'Banned',
            '40002': 'Locked',
            '50109': 'Invalid JSON',
            '200000': 'Automod flagged',
            '50007': 'Not allowed',
            '50008': 'Unable to send',
            '50001': 'No access/Not inside',
            '50013': 'Missing permissions',
            '50024': 'Cant do that on this channel',
            '80003': 'Cant self friend',
            '50168': 'Not in a VC',
            '20028': 'Limited',
            '0': 'Unauthorized',
            '401: Unauthorized': 'Unauthorized',
            'Cloudflare': 'Cloudflare',
            'captcha_key': 'Hcaptcha',
            'Unauthorized': 'Unauthorized',
            'retry_after': 'Limited',
            'You need to verify': 'Locked',
            'Cannot send messages to this user': 'Disabled DMS',
            'You are being blocked from accessing our API': 'API BAN'
        }

        for code, message in db.items():
            if code in thong:
                return True, message
        return False, thong

    def log(self, main: str = 'UNKNOWN', end: str = 'UNKNOWN', inp: bool = False):
        start = Colorate.Horizontal(Colors.green_to_white, f'[{main}]') 
        end = Colorate.Horizontal(Colors.green_to_white, f'{end}') 
        log = f'{start}{self.res} -> {end}'
        if not inp:
            print(log)
        else:
            input(log)

    def wip(self):
        main = Colorate.Horizontal(Colors.green_to_white, f'[UI]') 
        end = Colorate.Horizontal(Colors.green_to_white, f'[Work in progress...]') 
        input(f'{self.gettime()} {main}{self.res} -> {end}')

    def good(self, main: str, end: str):
        main = Colorate.Horizontal(Colors.green_to_white, f'[{main}]') 
        end = Colorate.Horizontal(Colors.green_to_white, f'[{end}]') 
        print(f'{self.gettime()} {main}{self.res} -> {end}')

    def fail(self, end: str):
        found = False
        try:
            found, end = self.check_db(end)
        except:
            pass

        if not found:
            try:
                end = json.loads(end)['message']
            except:
                pass

        main = Colorate.Horizontal(Colors.red_to_white, f'[Fail]') 
        end = Colorate.Horizontal(Colors.red_to_white, f'[{end}]') 
        print(f'{self.gettime()} {main}{self.res} -> {end}')

    def warn(self, end: str):
        main = Colorate.Horizontal(Colors.yellow_to_green, f'[Warn]') 
        end = Colorate.Horizontal(Colors.yellow_to_green, f'[{end}]') 
        print(f'{self.gettime()} {main}{self.res} -> {end}')

    def locked(self, end: str):
        main = Colorate.Horizontal(Colors.red_to_black, f'[Locked]') 
        end = Colorate.Horizontal(Colors.red_to_white, f'[{end}]') 
        print(f'{self.gettime()} {main}{self.res} -> {end}')

    def liimt(self, end: str):
        main = Colorate.Horizontal(Colors.yellow_to_red, f'[Limited]') 
        end = Colorate.Horizontal(Colors.yellow_to_red, f'[{end}]') 
        print(f'{self.gettime()} {main}{self.res} -> {end}')
        
    def hcap(self, end: str):
        main = Colorate.Horizontal(Colors.blue_to_cyan, f'[HCaptcha]') 
        end = Colorate.Horizontal(Colors.blue_to_cyan, f'[{end}]') 
        print(f'{self.gettime()} {main}{self.res} -> {end}')

    def debug(self, end: str):
        if __DEBUG__:
            print(f'{self.gettime()} {self.res}[DEBUG]{self.res} -> {end}')

log = log()