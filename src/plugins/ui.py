from src import *
from src.plugins.files import *

class ui:
    def __init__(self):
        self.size = os.get_terminal_size().columns
        self.gradient1 = [0, 255, 96]
        self.gradient2 = [128, 163, 91]

    def banner(self):
        banner = f"""
{r'    __    _                    __  __   ____'.center(size)}
{r'   / /   (_)___ ___  ____     /  /  /  /__ /'.center(size)}
{r'  / /   / / __ `__  / _  /   /  /  /  __/ / '.center(size)}
{r' / /___/ / / / / / / ___/   /  /  /  / __/  '.center(size)}
{r'/_____/_/_/ /_/ /_/____/   /_____/  /____/  '.center(size)}
"""
            
        print(ab5.vgratient(banner, self.gradient1, self.gradient2))

    def stats(self):
        stats = f'{len(files().gettokens())} Tokens  |  {len(files().getproxies())} Proxies'.center(self.size)
        print(ab5.vgratient(stats, self.gradient1, self.gradient2))

    def menu(self):
        menu = f'''
{'   Servers            Spamming             Tokens            Bypass             Annoying             Extra       '.center(self.size)}
{'01 Joiner          06 Message spam     11 Checker         16 Onboarding      21 Mass Dm         26 User scraper  '.center(self.size)}
{'02 Leaver          07 Threads spam     12 Avatar changer  17 Reaction        22 Spam call       27 ID scraper    '.center(self.size)}
{'03 Is in server    08 Threads2 spam    13 Bio changer     18 Rules           23 Mass friend     28 Booster       '.center(self.size)}
{'04 Anti ban        09 Poll spam        14 Disp changer    19 Button          24 Mass ticket     29 Token nuke    '.center(self.size)}
{'05 Nick changer    10 Chat crasher     15 Humanizer       20 Restorecord     25 React bomb      30 Combo to token'.center(self.size)}
{'>> Next page'.center(self.size)}
'''
        
        print(ab5.vgratient(menu, self.gradient1, self.gradient2))

    def menu2(self):
        menu2 = f'''
{'IN WORK'.center(self.size)}
{'IN WORK'.center(self.size)}
{'IN WORK'.center(self.size)}
{'IN WORK'.center(self.size)}
{'IN WORK'.center(self.size)}
{'IN WORK'.center(self.size)}
{'<< Back'.center(self.size)}
'''
        
        print(ab5.vgratient(menu2, self.gradient1, self.gradient2))

    def cls(self):
        os.system('cls')
    
    def title(self, x):
        os.system(f'title {x}')

    def ask(self, x, yn=False):
        if yn:
            x = input(f'{co.green}[{x}]{co.black} (y/n) >> {S.RESET_ALL}')
            if x in ['y', 'Y', 'yes', 'Yes', 'YES']:
                return True
            else:
                return False
        else:
            return input(f'{co.green}[{x}]{co.black} >> {S.RESET_ALL}')