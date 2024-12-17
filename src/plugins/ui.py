from src import *
from src.plugins.files import *

class ui:
    # Slant
    def __init__(self):
        self.size = os.get_terminal_size().columns
        self.gradient1 = [0, 255, 96]
        self.gradient2 = [128, 163, 91]

    def banner(self):
        banner = f"""
\033[1m{r' █████        ███                              █████   █████  ████████ '.center(self.size)}\033[0m
\033[1m{r'░░███        ░░░                              ░░███   ░░███  ███░░░░███'.center(self.size)}\033[0m
\033[1m{r' ░███        ████  █████████████    ██████     ░███    ░███ ░░░    ░███'.center(self.size)}\033[0m
\033[1m{r' ░███       ░░███ ░░███░░███░░███  ███░░███    ░███    ░███    ███████ '.center(self.size)}\033[0m
\033[1m{r' ░███        ░███  ░███ ░███ ░███ ░███████     ░░███   ███    ███░░░░  '.center(self.size)}\033[0m
\033[1m{r' ░███      █ ░███  ░███ ░███ ░███ ░███░░░       ░░░█████░    ███      █'.center(self.size)}\033[0m
\033[1m{r' ███████████ █████ █████░███ █████░░██████        ░░███     ░██████████'.center(self.size)}\033[0m
\033[1m{r'░░░░░░░░░░░ ░░░░░ ░░░░░ ░░░ ░░░░░  ░░░░░░          ░░░      ░░░░░░░░░░ '.center(self.size)}\033[0m
"""
            
        print(ab5.vgratient(banner, self.gradient1, self.gradient2))

    def stats(self):
        stats = f'{len(files.gettokens())} Tokens  |  {len(files.getproxies())} Proxies'.center(self.size)
        print(ab5.vgratient(stats, self.gradient1, self.gradient2))

    def menu(self):
        menu = f"""
\033[1m{'01 Joiner (F)      06 Message spam (F) 11 Checker (F)     16 Onboarding      21 Mass Dm         26 User scraper  '.center(self.size)}\033[0m
\033[1m{'02 Leaver (F)      07 Threads spam     12 Avatar changer  17 Reaction (F)    22 Spam call       27 ID scraper    '.center(self.size)}\033[0m
\033[1m{'03 Is in server (F)08 Threads2 spam    13 Bio changer     18 Rules           23 Mass friend     28 Booster       '.center(self.size)}\033[0m
\033[1m{'04 Anti ban        09 Poll spam        14 Disp changer (F)19 Button          24 Mass ticket     29 Token nuke    '.center(self.size)}\033[0m
\033[1m{'05 Nick changer    10 Chat crasher     15 Pron changer    20 Restorecord     25 React bomb      30 Combo to token'.center(self.size)}\033[0m
\033[1m{'>> Next page'.center(self.size)}\033[0m
"""
            
        print(ab5.vgratient(menu, self.gradient1, self.gradient2))

    def menu2(self):
        menu2 = f"""
\033[1m{'31 Mass send       06 Message spam     11 Checker         16 Onboarding      21 Mass Dm         26 User scraper  '.center(self.size)}\033[0m
\033[1m{'32 Token fucker    07 Threads spam     12 Avatar changer  17 Reaction        22 Spam call       27 ID scraper    '.center(self.size)}\033[0m
\033[1m{'33 Invite scraper  08 Threads2 spam    13 Bio changer     18 Rules           23 Mass friend     28 Booster       '.center(self.size)}\033[0m
\033[1m{'34 Msg listener    09 Poll spam        14 Disp changer    19 Button          24 Mass ticket     29 Token nuke    '.center(self.size)}\033[0m
\033[1m{'35 None            10 Chat crasher     15 Pron changer    20 Restorecord     25 React bomb      30 Combo to token'.center(self.size)}\033[0m
\033[1m{'<< Back'.center(self.size)}\033[0m
"""
        
        print(ab5.vgratient(menu2, self.gradient1, self.gradient2))

    def cls(self):
        os.system('cls')
    
    def title(self, x):
        os.system(f'title {x}')

    def ask(self, x, yn=False):
        if yn:
            x = input(f'\033[1m{co.green}[{x}]{co.black} (y/n) >> {S.RESET_ALL}\033[0m')
            if x in ['y', 'Y', 'yes', 'Yes', 'YES']:
                return True
            else:
                return False
        else:
            return input(f'\033[1m{co.green}[{x}]{co.black} >> {S.RESET_ALL}\033[0m')
    
    def make_menu(self, options):
        for index, option in enumerate(options, 1):
            print(f'\033[1m{co.green}[{index:02d}]{co.black} >> {co.green}[{option}]{S.RESET_ALL}\033[0m')

        print('\n')