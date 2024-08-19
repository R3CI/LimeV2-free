from core import *

class UI:
    # Rowan Cap
    def __init__(self):
        self.size = os.get_terminal_size().columns - 3
        self.res = Fore.RESET
        self.red = Fore.RED
        self.black = Fore.LIGHTBLACK_EX
        self.magenta = Fore.MAGENTA
        self.cyan = Fore.CYAN
        self.lightblue = Fore.LIGHTBLUE_EX
        self.darkblue = Fore.BLUE
        self.purple = Fore.LIGHTMAGENTA_EX
        self.green = Fore.GREEN
        self.yellow = Fore.YELLOW

    def banner(self):
        banner = f'''
{'    dMP     dMP dMMMMMMMMb  dMMMMMP '.center(self.size)}
{'   dMP     amr dMP"dMP"dMP dMP      '.center(self.size)}
{'  dMP     dMP dMP dMP dMP dMMMP     '.center(self.size)}  
{' dMP     dMP dMP dMP dMP dMP        '.center(self.size)}
{'dMMMMMP dMP dMP dMP dMP dMMMMMP     '.center(self.size)}
'''
        #banner = vgratient(banner, [0, 123, 255], [1, 7, 56])
        banner = pystyle.Colorate.Horizontal(pystyle.Colors.green_to_white, banner)
        print(banner)    


    def menu(self):
        menu = f'''
{'REP Report an issue  |  EX See all extra options  |  PANEL Customer panel'.center(self.size)}
{''.center(self.size)}
{'01 Server managment       09 Mass DM menu           17 Server booster    '.center(self.size)}
{'02 Token managment        10 Spam call              18 None              '.center(self.size)}
{'03 Spamming menu          11 Button spammer         19 Scrape usernames  '.center(self.size)}
{'04 Bypass menu            12 Mass ticket maker      20 Scrape ids        '.center(self.size)}
{'05 VC menu                13 Mass friender          21 Invite scraper    '.center(self.size)}
{'06 Webhook menu           14 Reaction bomber        22 None              '.center(self.size)}
{'07 Server admin menu      15 Mass invite maker      23 None              '.center(self.size)}
{'08 Mass report menu       16 Poll voter             24 None              '.center(self.size)}
'''
        #menu = vgratient(menu, [0, 123, 255], [1, 7, 56])
        menu = pystyle.Colorate.Horizontal(pystyle.Colors.green_to_white, menu)
        

        print(menu) 

    def make_menu(self, options: list, retunrN: bool = False, tabs: int = 0):
        tabs = '\t' * tabs
        if retunrN:
            options.append('Return')
        for index, option in enumerate(options, 1):
            if option != 'Return':
                option_str = f'{index:02d} -> {option}\n'
            else:
                option_str = f'<< -> {option}\n'
            thong = Colorate.Horizontal(Colors.green_to_white, f'{tabs}{option_str}')
            print(thong)  
        print('\n')

    def ask(self, question: str, yn: bool = False):  
        if not yn:
            answerthong = Colorate.Horizontal(Colors.green_to_white, f'[{question}] -> ') 
            answer = input(answerthong)
            return answer
        else:
            answerthong = Colorate.Horizontal(Colors.green_to_white, f'[{question}] (y/n) -> ') 
            answer = input(answerthong)
            if answer in ['y', 'Y']:
                return True
            else:
                return False
            
    def authbanner(self):
        banner = f'''
{'    dMP     dMP dMMMMMMMMb  dMMMMMP         .aMMMb  dMP dMP dMMMMMMP dMP dMP '.center(self.size)}
{'   dMP     amr dMP"dMP"dMP dMP             dMP"dMP dMP dMP    dMP   dMP dMP  '.center(self.size)}
{'  dMP     dMP dMP dMP dMP dMMMP           dMMMMMP dMP dMP    dMP   dMMMMMP   '.center(self.size)}
{' dMP     dMP dMP dMP dMP dMP             dMP dMP dMP.aMP    dMP   dMP dMP    '.center(self.size)}
{'dMMMMMP dMP dMP dMP dMP dMMMMMP         dMP dMP  VMMMP"    dMP   dMP dMP     '.center(self.size)}
'''
        #banner = vgratient(banner, [0, 123, 255], [1, 7, 56])
        banner = pystyle.Colorate.Horizontal(pystyle.Colors.green_to_white, banner)
        print(banner)  