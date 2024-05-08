import os, sys, time

print('Downloading libs and preping, please wait')

if sys.version_info[:3] != (3, 11, 7):
    print(f'Ur current version of python ({sys.version_info.major}.{sys.version_info.minor}) we only support 3.11.7 atm.')
    time.sleep(5)
    sys.exit()

try:
    from colorama import Fore, Back, init; init()
    import requests
    import uuid
    import threading
    import base64
    import tls_client
    import random
    import websocket
    import json
    import string
    import re
    from datetime import datetime
    from tkinter import filedialog
    import tkinter as tk
    import threading
    import tkinter as tk
    import threading
    import time
except ModuleNotFoundError as e:
    missing_lib = str(e).split("'")[1]
    print(f'Some libs are missing, downloading them now. MISSING: {missing_lib}')
    os.system('pip uninstall -y websockets'); os.system('pip uninstall -y websocket')
    for lib in ['websocket-client', 'colorama', 'requests', 'tls-client', 'datetime']:
        os.system(f'pip install -q {lib}')
    print('All done! please rerun')
    time.sleep(2.5)
    sys.exit()

except Exception as e:
    input(f'Error while importing {e}')
    time.sleep(5)
    sys.exit()

version = float('1.0')

main_name = f'Vanadium V{version} - FREE'

# region START CMD

class cmd:
    res = Fore.RESET
    r = Fore.RED
    b = Fore.LIGHTBLACK_EX
    m = Fore.MAGENTA
    c = Fore.CYAN
    p = Fore.LIGHTMAGENTA_EX
    g = Fore.GREEN
    y = Fore.YELLOW
    tips = [
        'Input ur token inside of config.jsonc for easier use',
        'Use proxies to avoid ratelimits',
        'Free public proxies have a high chance of being blacklisted',
        'U can input the whole invite inside of the joiner',
        'If u cant find a valid discord invite for the discord server use https://dsc.gg/vanadium',
        'Fast raid is an unstable feature',
        'U can find a lot of things inside of the data folder',
        'The proxy format is user:password@host:port or host:port',
        'The combo token format is email:password:token',
        'If u dont know what ur doing dont use debug mode its made for me to test and while developing',
        'If u get constant captchas it may just be u that used the api too much',
        'Buying paid is a great investment!11!!!'
    ]
    def __init__(self):
        self.size = os.get_terminal_size().columns
        self.size = self.size - 1
        self.date = datetime.now().strftime('%H:%M:%S')
        self.date_ = datetime.now()
        self.date_ = f'{self.date_.day}_{self.date_.month}_{self.date_.year}'
        with open(f'data\\tokens.txt', 'r') as f:
            self.token_amt = sum(1 for _ in f)
        with open(f'data\\combo_tokens.txt', 'r') as f:
            self.combo_amt = sum(1 for _ in f)
        with open(f'data\\proxies.txt', 'r') as f:
            self.prx_amt = sum(1 for _ in f)

    def banner(self):
        banner = f'''{cmd().r}  
{f'Currently using free version | buy paid on dsc.gg/vanadium :money:'.center(self.size)} 
{f'██╗   ██╗ █████╗ ███╗   ██╗ █████╗ ██████╗ ██╗██╗   ██╗███╗   ███╗'.center(self.size)}
{f'██║   ██║██╔══██╗████╗  ██║██╔══██╗██╔══██╗██║██║   ██║████╗ ████║'.center(self.size)}
{f'██║   ██║███████║██╔██╗ ██║███████║██║  ██║██║██║   ██║██╔████╔██║'.center(self.size)} 
{f'╚██╗ ██╔╝██╔══██║██║╚██╗██║██╔══██║██║  ██║██║██║   ██║██║╚██╔╝██║'.center(self.size)}
{f' ╚████╔╝ ██║  ██║██║ ╚████║██║  ██║██████╔╝██║╚██████╔╝██║ ╚═╝ ██║'.center(self.size)}
{f'  ╚═══╝  ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═════╝ ╚═╝ ╚═════╝ ╚═╝     ╚═╝'.center(self.size)}
'''
        print(banner)

    def menu(self):
        menu = f'''{cmd().r}  
{f'Currently using free version | buy paid on dsc.gg/vanadium :money:'.center(self.size)} 
{f'██╗   ██╗ █████╗ ███╗   ██╗ █████╗ ██████╗ ██╗██╗   ██╗███╗   ███╗'.center(self.size)}
{f'██║   ██║██╔══██╗████╗  ██║██╔══██╗██╔══██╗██║██║   ██║████╗ ████║'.center(self.size)}
{f'██║   ██║███████║██╔██╗ ██║███████║██║  ██║██║██║   ██║██╔████╔██║'.center(self.size)} 
{f'╚██╗ ██╔╝██╔══██║██║╚██╗██║██╔══██║██║  ██║██║██║   ██║██║╚██╔╝██║'.center(self.size)}
{f' ╚████╔╝ ██║  ██║██║ ╚████║██║  ██║██████╔╝██║╚██████╔╝██║ ╚═╝ ██║'.center(self.size)}
{f'  ╚═══╝  ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═════╝ ╚═╝ ╚═════╝ ╚═╝     ╚═╝'.center(self.size)}
{f'TIP ~> {random.choice(cmd().tips)}'.center(self.size)}
{f''.center(self.size)}
{f'(*) - Combo tokens needed      (#) - Beta feature      (!) - Can be token harming'.center(self.size)}
{f'Tokens loaded - [ {self.token_amt} ]    Combo tokens loaded - [ {self.combo_amt} ]    Proxies loaded - [ {self.prx_amt} ]    Main token state - [ {main_token_state} ]'.center(self.size)}
{f''.center(self.size)}
{f'  [ 01 ] - Guild menu         [ 08 ] - Token humanizer       [ 15 ] - Reaction bomber    [ 22 ] - Friender (!)   '.center(self.size)}
{f'  [ 02 ] - Checker            [ 09 ] - Bio changer           [ 16 ] - Spam call          [ 23 ] - VC joiner      '.center(self.size)} 
{f'  [ 03 ] - Spammer            [ 10 ] - Username changer (*)  [ 17 ] - Mass DM (!)        [ 24 ] - VC spammer     '.center(self.size)}
{f'  [ 04 ] - Bypasses           [ 11 ] - Display changer       [ 18 ] - Mass report        [ 25 ] - Mass pin       '.center(self.size)}
{f'  [ 05 ] - Fast raid (#)      [ 12 ] - Avatar changer        [ 19 ] - Button spammer     [ 26 ] - Mass respond   '.center(self.size)}
{f'  [ 06 ] - Combo to token     [ 13 ] - Nick changer          [ 20 ] - Thread spammer     [ 27 ] - Join greet spam'.center(self.size)}
{f'  [ 07 ] - Onliner            [ 14 ] - Password changer (*)  [ 21 ] - Forum spammer      [ >> ] - Next page      '.center(self.size)}
'''
        for x in ['-', 'None', '*', '#', '!']:
            menu = menu.replace(x, f'{cmd().b}{x}{cmd().r}')

        print(menu)
    
    def menu2(self):

        menu2 = f'''{cmd().r}  
{f'Currently using free version | buy paid on dsc.gg/vanadium :money:'.center(self.size)} 
{f'██╗   ██╗ █████╗ ███╗   ██╗ █████╗ ██████╗ ██╗██╗   ██╗███╗   ███╗'.center(self.size)}
{f'██║   ██║██╔══██╗████╗  ██║██╔══██╗██╔══██╗██║██║   ██║████╗ ████║'.center(self.size)}
{f'██║   ██║███████║██╔██╗ ██║███████║██║  ██║██║██║   ██║██╔████╔██║'.center(self.size)} 
{f'╚██╗ ██╔╝██╔══██║██║╚██╗██║██╔══██║██║  ██║██║██║   ██║██║╚██╔╝██║'.center(self.size)}
{f' ╚████╔╝ ██║  ██║██║ ╚████║██║  ██║██████╔╝██║╚██████╔╝██║ ╚═╝ ██║'.center(self.size)}
{f'  ╚═══╝  ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═════╝ ╚═╝ ╚═════╝ ╚═╝     ╚═╝'.center(self.size)}
{f'TIP ~> {random.choice(cmd().tips)}'.center(self.size)}
{f''.center(self.size)}
{f'(*) - Combo tokens needed      (#) - Beta feature      (!) - Can be token harming'.center(self.size)}
{f'Tokens loaded - [ {self.token_amt} ]    Combo tokens loaded - [ {self.combo_amt} ]    Proxies loaded - [ {self.prx_amt} ]    Main token state - [ {main_token_state} ]'.center(self.size)}
{f''.center(self.size)}
{f'  [ 28 ] - Poll spammer (#)   [ 35 ] - Account nuker         [ 42 ] - Invite maker       [ 49 ] - WB spammer     '.center(self.size)}
{f'  [ 29 ] - Poll voter (#)     [ 36 ] - Log out               [ 43 ] - Mass ban           [ 50 ] - WB editor      '.center(self.size)} 
{f'  [ 30 ] - Everywheare sender [ 37 ] - Log in                [ 44 ] - Mass kick          [ 51 ] - WB deleater    '.center(self.size)}
{f'  [ 31 ] - Message spy        [ 38 ] - Fake acc deleate      [ 45 ] - Mass unban         [ 52 ] - None           '.center(self.size)}
{f'  [ 32 ] - Channel perm check [ 39 ] - Change status         [ 46 ] - Server mass report [ 53 ] - None           '.center(self.size)}
{f'  [ 33 ] - None               [ 40 ] - None                  [ 47 ] - Anti ban           [ << ] - Previous page  '.center(self.size)}
{f'  [ 34 ] - None               [ 41 ] - None                  [ 48 ] - None               [ >> ] - Next page      '.center(self.size)}
'''
        
        for x in ['-', 'None', '*', '#', '!']:
            menu2 = menu2.replace(x, f'{cmd().b}{x}{cmd().r}')

        print(menu2)

    def options(self, options):
        for x in ['~>']:
            options = options.replace(x, f'{cmd().r}{x}{cmd().b}')
        print(f'{cmd().b}{options}')
    
    def not_yet(self):
        cmd().log('CORE', 'This feautre is not made yet')
        return

    def log(self, main, contents):
        print(f'{cmd().r}[{cmd().b}{main}{cmd().r}] {cmd().r}~>{cmd().b} {contents}')

    def inplog(self, main, contents):
        input(f'{cmd().r}[{cmd().b}{main}{cmd().r}] {cmd().r}~>{cmd().b} {contents}')

    def ask(self, main):
        return input(f'{cmd().r}[{cmd().b}{main}{cmd().r}] {cmd().r}~>{cmd().b} ')
    
    def askyn(self, main):
        inp = input(f'{cmd().r}[{cmd().b}{main}{cmd().r}]{cmd().b} (y/n) {cmd().r}~>{cmd().b} ')
        if inp == 'y':
            return True
        else:
            return False
        
    def good(self, token, main, status, response=None):
        if response:
            response = f'({response})'
            try:
                response = json.loads(response)['message']
            except:
                response = response

        if not response:
            response = ''
        
        try:
            token = f'{token[:30]}{cmd().r}***{cmd().b}'
        except:
            if not token:
                token = 'Unknown'
            else:
                token = token

        print(f'{cmd().b}[{self.date}]{cmd().r} {cmd().g}[{main} ~> {status}] {cmd().b}~>{cmd().r} {token} {cmd().b} {response}')

    def bad(self, token, main, status, response):
        if cfg().moreinfo():
            if response:
                response = f'({response})'
                try:
                    response = json.loads(response)['message']
                except:
                    response = response

        try:
            token = f'{token[:30]}{cmd().r}***{cmd().b}'
        except:
            if not token:
                token = 'Unknown'
            else:
                token = token

        print(f'{cmd().b}[{self.date}]{cmd().r} {cmd().r}[{main} ~> {status}] {cmd().b}~>{cmd().r} {token} {cmd().b} {response}')

    def captha(self, token, status):
        try:
            token = f'{token[:30]}{cmd().r}***{cmd().b}'
        except:
            if not token:
                token = 'Unknown'
            else:
                token = token

        print(f'{cmd().b}[{self.date}]{cmd().c} {cmd().c}[HCaptcha ~> {status}] {cmd().b}~>{cmd().r} {token} {cmd().b} | Could be prob prevented if u used paid :money:')

    def ratelimit(self, token, status, jresponse=None):
        if jresponse:
            ratelimit = float(jresponse['retry_after'])
        else:
            ratelimit = 'N/A'

        try:
            token = f'{token[:30]}{cmd().r}***{cmd().b}'
        except:
            if not token:
                token = 'Unknown'
            else:
                token = token

        print(f'{cmd().b}[{cmd().date}]{cmd().r} {cmd().y}[Ratelimited ~> {status}] {cmd().b}~>{cmd().r} {token} {cmd().b} {ratelimit}s')

    def title(self, content):
        os.system(f'title {content}')

    def cls(self):
        os.system('cls')

    def preare(self, module):
        cmd().cls()
        cmd().banner()
        cmd().title(f'{main_name} - {module}')

    def dbg(self, var='', var1='', var2='', var3=''):
        if cfg().debug():
            print(f'DEBUG: {var} {var1} {var2} {var3}')

    def paid():
        cmd().log('CORE', 'This feature is paid only! | buy at https://dsc.gg/vanadium')


# region END CMD

os.system('cls')
os.system(f'title {main_name}')



class files:
    def folders():
        folders = [
            'data', 
            'data\\scrapes',
            'data\\scrapes\\guilds',
            'data\\debug',
            'data\\message_spy'
        ]
        for folder in folders:
            try:
                if not os.path.exists(folder):
                    os.mkdir(folder)
            except Exception as e:
                try:
                    cmd().log('FILES', f'FOLDER ({folder}) CREATION ERROR: {e}')
                except Exception as e:
                    print(f'FILE ERROR: {e}')

    def cfg():
        if not os.path.exists('config.jsonc'):
            with open('config.jsonc', 'w', encoding='utf-8') as f:
                f.write("""
{
    "DEBUG": false, // Made just for me dont use
    "Proxies": false,  // Most free proxies wont work on discord, remember!
    "Onliner on func": false, // Token onliner when a module is ran
    "RPC": true, // Onlined tokens will have a vanadium RPC
    "Preffer combos": false, // Will prefer to use the combo tokens instead of just tokens (input combos to data/combo_tokens.txt)
    "More info mode": false, // If the code is diffrent than OK (succes) the log will show the full respone text
                        
    "Main acc token": "" // Used for features wthat need high perms like massban/masskick so u can input ur token with these perms by simply putting main inside of the token filed
}
    """)
            os.startfile('config.jsonc')
    def other():
        files = [
            'tokens.txt', 
            'proxies.txt',
            'combo_tokens.txt',
            'names.txt'
        ]
        for file in files:
            try:
                if not os.path.exists(file):
                    with open(f'data\\{file}', 'a', encoding='utf-8') as f:
                        f.close()
            except Exception as e:
                try:
                    cmd().log('FILES', f'FILE ({file}) CREATION ERROR: {e}')
                except Exception as e:
                    print(f'FILE ERROR: {e}')
                time.sleep(5)
                sys.exit()

    def write_names():
        with open('data\\names.txt', 'r', encoding='utf-8') as f:
            username_count = sum(1 for l in f)
        if username_count < 50000:
            r = requests.get(
                'https://raw.githubusercontent.com/R3CI/Resources/main/names'
            )
            if r.status_code == 200:
                with open('data\\names.txt', 'w', encoding='utf-8') as f:
                    f.write(r.text)
            else:
                cmd().inplog('Failed to get usernames for names.txt, some features may be broken')

    def write_names():
        with open('data\\names.txt', 'r', encoding='utf-8') as f:
            username_count = sum(1 for l in f)
        if username_count < 50000:
            cmd().log('FILES', 'Getting usernames...')
            r = requests.get(
                'https://raw.githubusercontent.com/R3CI/Resources/main/names'
            )
            if r.status_code == 200:
                with open('data\\names.txt', 'w', encoding='utf-8') as f:
                    f.write(r.text)
                cmd().log('FILES', 'Wrote usernames')
            else:
                cmd().inplog('FILES', 'Failed to get usernames for names.txt, some features may be broken')
    
    def backup_tokens(tokens):
        cmd().log('FILES', 'Backing up tokens')
        with open('data\\token_backup.txt', 'w') as f:
            for token in tokens:
                f.write(token + '\n')
        cmd().log('FILES', 'Backedup tokens')

    def del_dbg():
        for filename in os.listdir('data\\debug'):
            filepath = os.path.join('data\\debug', filename)
            try:
                if os.path.isfile(filepath):
                    os.remove(filepath)
                    cmd().log('FILES', f'Deleated {filepath}')
            except Exception as e:
                cmd().log('FILES', f'Could not delete {filepath}')

    def write_avatar():
        if not os.path.exists('data\\avatar.png'):
            cmd().log('FILES', 'Downloading avatar...')

            r = requests.get('https://raw.githubusercontent.com/R3CI/Resources/main/avatar.png')

            if r.status_code == 200:
                with open(f'data\\avatar.png', 'wb') as f:
                    f.write(r.content)
            else:
                cmd().inplog('FILES', 'Failed to get usernames for names.txt, some features may be broken')

    def run():
        files.cfg()
        files.folders()
        files.other()
        files.write_names()
        files.write_avatar()
        files.del_dbg()

files.run()
cmd().log('FILES', 'Did all file stuff')

class cfg:
    def __init__(self):
        with open('config.jsonc', 'r') as f:
            try:
                config_contents = ''
                for line in f:
                    config_contents += line.split('//', 1)[0]
                config_contents = re.sub(r'/\*[\s\S]*?\*/', '', config_contents)
                self.cfg = json.loads(config_contents)
            except json.JSONDecodeError as e:
                cmd().log('CONFIG', e)
                self.cfg = {}

    def debug(self):
        return self.cfg['DEBUG']  

    def proxies(self):
        return self.cfg['Proxies']

    def online(self):
        return self.cfg['Onliner on func']

    def rpc(self):
        return self.cfg['RPC']
    
    def prefer_combo_tokens(self):
        return self.cfg['Preffer combos']   

    def moreinfo(self):
        return self.cfg['More info mode']

    def main_token(self):
        return self.cfg['Main acc token']

cmd().log('CONFIG', 'Reading config...')


cmd().cls()
cmd().title(main_name)
    
class thread:
    def multi(thread_amt, func, tokens, *args):
        threads = []
        for _ in range(int(thread_amt)):
            for token in tokens:
                t = threading.Thread(target=func, args=(token,) + args)
                t.start()
                threads.append(t)
        for thread in threads:
            thread.join()

    def single(func, tokens, *args):
        threads = []
        for token in tokens:
            t = threading.Thread(target=func, args=(token,) + args)
            t.start()
            threads.append(t)
        for thread in threads:
            thread.join()

    def multi_c(thread_amt, func, *args):
        combos = get.combos()
        threads = []
        for _ in range(int(thread_amt)):
            for combo in combos:
                t = threading.Thread(target=func, args=combo + args)
                t.start()
                threads.append(t)
        for thread in threads:
            thread.join()

    def single_c(func, *args):
        combos = get.combos()
        threads = []
        for combo in combos:
            t = threading.Thread(target=func, args=combo + args[1:])
            t.start()
            threads.append(t)
        for thread in threads:
            thread.join()


class get:
    def cookies():
        r = requests.get(
            "https://discord.com/"
        )
        if r.status_code == 200:
            cookies = '; '.join([f"{cookie.name}={cookie.value}" for cookie in r.cookies]) + '; locale=en-US'
        else:
            cmd().dbg(r.status_code, r.text)
            cookies = get.fake_cookies()
        return cookies
    
    def fake_cookies():
        def func(length):
            return ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        
        return f'__dcfduid={func(32)}; __sdcfduid={func(96)}; __cfruid={func(51)}; _cfuvid={func(75)}; locale=en-US'
    
    def tokens():
        if not cfg().prefer_combo_tokens():
            with open(f'data\\tokens.txt', 'r') as f:
                return f.read().splitlines()
        else:
            combos = []
            with open(f'data\\combo_tokens.txt', 'r') as f:
                lines = f.read().splitlines()
                for line in lines:
                    parts = line.strip().split(':')
                    
                    if len(parts) >= 3:
                        token = parts[2]
                        combos.append(token)
                    else:
                        cmd().log('TOKEN READER', 'Invalid combo format! it should be email:pass:token')
                        time.sleep(5)
                        sys.exit()
            return combos         
        
    def combos():
        combos = []
        with open(f'data\\combo_tokens.txt', 'r') as f:
            lines = f.read().splitlines()
            for line in lines:
                parts = line.strip().split(':')
                if len(parts) >= 3:
                    email = parts[0]
                    password = parts[1]
                    token = parts[2]
                    combos.append((email, password, token))
                else:
                    cmd().log('TOKEN READER', 'Invalid combo format! it should be email:pass:token')
        return combos
    
    def combo_tokens():
        combos = []
        with open(f'data\\combo_tokens.txt', 'r') as f:
            lines = f.read().splitlines()
            for line in lines:
                parts = line.strip().split(':')
                
                if len(parts) >= 3:
                    token = parts[2]
                    combos.append(token)
                else:
                    cmd().log('TOKEN READER', 'Invalid combo format! it should be email:pass:token')
                    time.sleep(5)
                    sys.exit()
        return combos  
        
    def proxies():
        with open(f'data\\proxies.txt', 'r') as f:
            return f.read().splitlines()
    
    def nonce():
        return str((int(time.mktime(datetime.now().timetuple())) * 1000 - 1420070400000) * 4194304)

    def timestamp():
        timestamp = "{:.0f}".format(time.time() * 1000)
        return timestamp
    
    def string(length):
        random_string = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))
        return random_string
    
    def fingerprint():
        r = requests.get('https://discord.com/api/v9/experiments')
        if r.status_code == 200:
            return r.json()['fingerprint']
        else:
            return f'{[random.randint(1, 100) for _ in range(19)]}.{get.string(27)}'



# region HEADERS



chrome_version = random.randint(115, 120)
class cowfarm:
    def __init__(self):
        self.ua = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9042 Chrome/120.0.6099.291 Electron/28.2.10 Safari/537.36'
        self.xsup = 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDQyIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDUiLCJvc19hcmNoIjoieDY0IiwiYXBwX2FyY2giOiJpYTMyIiwic3lzdGVtX2xvY2FsZSI6ImVuLUdCIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV09XNjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIGRpc2NvcmQvMS4wLjkwNDIgQ2hyb21lLzEyMC4wLjYwOTkuMjkxIEVsZWN0cm9uLzI4LjIuMTAgU2FmYXJpLzUzNy4zNiIsImJyb3dzZXJfdmVyc2lvbiI6IjI4LjIuMTAiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjoyODc2NjUsIm5hdGl2ZV9idWlsZF9udW1iZXIiOjQ2NjY5LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsLCJkZXNpZ25faWQiOjB9'
        cmd().log('HEADERS', 'Getting cookies...')
        self.cookies = get.cookies()
        cmd().log('HEADERS', f'Got cookies ~> {self.cookies[:75]}{cmd().r}***{cmd().b}')
        cmd().log('HEADERS', 'Getting fingerprint...')
        self.fingerprint = get.fingerprint()
        cmd().log('HEADERS', f'Got fingerprint ~> {self.fingerprint[:50]}{cmd().r}***{cmd().b}')


    def get(self, token=None, data=None, fingerprint=False):
        headers = {
            "Accept": "*/*",
            "Accept-language": "en-GB,pl;q=0.9",
            "Authorization": token,
            "Cookie": self.cookies,
            "Origin": "https://discord.com",
            "Sec-Ch-Ua": f'"Not_A Brand";v="8", "Chromium";v="{chrome_version}"',
            "Sec-Ch-Ua-Platform": '"Windows',
            "User-agent": self.ua,
            "X-Discord-Locale": "en-US",
            "X-Discord-Timezone": "Europe/Warsaw",
            "X-Fingerprint": self.fingerprint,
            "X-Super-Properties": self.xsup
        }
        if token is None:
            headers.pop("Authorization", None)
        if data is None:
            headers.pop("Content-Length", None)
        if not fingerprint:
            headers.pop("X-Fingerprint", None)

        return headers

headers = cowfarm()

bl_guilds = ['1218958297558679702', '1157405821450338334']
bl_channels = []
bl_ids = []

def get_user_id(token):
    global bl_ids
    r = requests.get(
        f"https://discord.com/api/v9/users/@me",
        headers=headers.get(token),
    )
    if r.status_code == 200:
        bl_ids.append(r.json()['id'])
        cmd().log('BLACKLIST', f'Blackisted id for {cmd().b}{token[:30]}{cmd().r}***{cmd().b} {r.json()["id"]}')
    else:
        cmd().log('BLACKLIST', f'Failed to blacklist id for {cmd().b}{token[:30]}{cmd().r}***{cmd().b}')

thread.single(get_user_id, get.tokens())

# region SESSION


def session():
    session = tls_client.Session(
        client_identifier=f'chrome_{chrome_version}', random_tls_extension_order=True
    )
    return session

# region MAIN TOKEN STUFF
main_token_state = 'PAID ONLY'

# region TOOL


class tool:
    def paid():
        cmd().log('CORE', 'This feature is paid only! | buy at https://dsc.gg/vanadium')

    def check_wb(wb):
        r = requests.head(wb).status_code
        if r != 200:
            return False
        else:
            return True

    def link_transform(url):
        if 'https://discord.com/channels/' in url:
            url = url.replace('https://discord.com/channels/', '')
        elif 'https://canary.discord.com/channels/' in url:
            url = url.replace('https://canary.discord.com/channels/', '')

        parts = url.split('/')
        guildid = parts[0]
        channelid = parts[1]
        messageid = parts[2]
        return guildid, channelid, messageid

    def rpc():
        return
    
    def get_user_id(token):
        ss = session()
        r = ss.get(
            f"https://discord.com/api/v9/users/@me",
            headers=headers.get(token),
        )
        cmd().dbg('CHECKER', r.status_code, r.text)
        if r.status_code == 200:
            return r.json()['id']
        else:
            return None

    def inside_guild(guildid, specific_token=None):
        if not specific_token:
            cmd().log('TOKENS', f'Getting tokens that are isnide of the guild {guildid}')
            inside = []
            tokens = get.tokens()
            for token in tokens:
                ss = session()
                try:
                    r = ss.get(
                        f"https://discord.com/api/v9/guilds/{guildid}",
                        headers=headers.get(token)
                    )

                    if r.status_code == 200:
                        inside.append(token)  
                except:
                    pass

            return inside
        else:
            cmd().log('TOKENS', f'Checking if {token[:30]}{cmd().r}***{cmd().b} is inside of the guild {guildid}')
            ss = session()
            try:
                r = ss.get(
                    f"https://discord.com/api/v9/guilds/{guildid}",
                    headers=headers.get(token)
                )

                if r.status_code == 200:
                    return True
                else:
                    return False
            except:
                return False  

    def channel_acces(channelid, specific_token=None):
        if not specific_token:
            cmd().log('TOKENS', f'Getting tokens that have acces to the channel {channelid}')
            inside = []
            tokens = get.tokens()
            for token in tokens:
                ss = session()
                try:
                    r = ss.get(
                        f"https://discord.com/api/v9/channels/{channelid}/messages?limit=50",
                        headers=headers.get(token)
                    )

                    if r.status_code == 200:
                        inside.append(token)  
                except:
                    pass

            return inside
        else:
            cmd().log('TOKENS', f'Checking if {token[:30]}{cmd().r}***{cmd().b} has acces to the channel {channelid}')
            ss = session()
            try:
                r = ss.get(
                    f"https://discord.com/api/v9/channels/{channelid}/messages?limit=50",
                    headers=headers.get(token)
                )

                if r.status_code == 200:
                    return True
                else:
                    return False
            except:
                return False 
    
    def online(token):
        ws = websocket.WebSocket()
        ws.connect('wss://gateway.discord.gg/?v=9&encoding=json')
        ws.send(
            json.dumps({
            "op": 2,
            "d": {
                "token": token,
                "capabilities": 8189,
                "properties": {
                    "os": "Windows",
                    "browser": "Chrome",
                    "device": "",
                    "system_locale": "en-US",
                    "browser_user_agent": headers.ua,
                    "browser_version": "111.0.0.0",
                    "os_version": "10",
                    "referrer": "",
                    "referring_domain": "",
                    "referrer_current": "",
                    "referring_domain_current": "",
                    "release_channel": "stable",
                    "client_build_number": 199933,
                    "client_event_source": None,
                    "design_id": 0
                },
                "presence": {
                    "status": random.choice(["online", "idle", "dnd"]),
                    "since": 0,
                    "activities": [{
                        "name": "Custom Status",
                        "type": 4,
                        "state": main_name,
                        "emoji": "💣"
                    }],
                    "afk": False
                },
                "compress": False,
                "client_state": {
                    "guild_versions": {},
                    "highest_last_message_id": "0",
                    "read_state_version": 0,
                    "user_guild_settings_version": -1,
                    "user_settings_version": -1,
                    "private_channels_version": "0",
                    "api_code_version": 0
                }
            }
        }))

    class guild_manager:
        def main():
            cmd().preare('Guild manager')
            cmd().options('''
01 ~> Joiner
02 ~> Leaver
03 ~> Guild checker
04 ~> Mass leave 
05 ~> Back
''')
            c = cmd().ask('CHOICE')
            if c == '1':
                tool.guild_manager.joiner.main()
            elif c == '2':
                tool.guild_manager.leaver.main()
            elif c == '3':
                tool.guild_manager.guild_checker.main()
            elif c == '4':
                cmd().paid()
            elif c == '5':
                return
            else:
                cmd().log('GUILD MANAGER', 'Invalid option')



        class joiner:
            def join(token, invite_regex):
                cmd().dbg('JOINING:', token)
                guildid, guildname = tool.guild_manager.joiner.get_name_and_id(invite_regex)
                cmd().dbg('GUILDID:', guildid, 'GUILDNAME:', guildname)
                if guildid in bl_guilds:
                    cmd().log('JOINER', 'Nah really? Trying to join the main server?? Thats crazyyy')
                    return     

                payload = {
                    "session_id": uuid.uuid4().hex
                }
                ss = session()
                r = ss.post(
                    f"https://discord.com/api/v9/invites/{invite_regex}",
                    json=payload,
                    headers=headers.get(token, payload)
                )

                cmd().dbg('JOINER', r.status_code, r.text)
                if r.status_code == 200:
                    cmd().good(token, f'Joined {guildname}', r.status_code)
                    
                elif r.status_code == 400:
                    cmd().captha(token, r.status_code)

                elif r.status_code == 429:
                    cmd().ratelimit(token, r.status_code, r.json())
                    time.sleep(float(r.json()['retry_after']))
                    tool().guild_manager.joiner.join(token, invite_regex)

                elif r.status_code == 403:
                    if 'code' in r.json() and r.json()['code'] == 40007:
                        cmd().bad(token, 'Banned', r.status_code, r.text)
                    else:
                        cmd().bad(token, 'Locked', r.status_code, r.text)

                elif r.status_code == 401:
                    cmd().bad(token, 'Unauthorized', r.status_code, r.text)

                else:   
                    cmd().bad(token, 'Other', r.status_code, r.text)

            def get_name_and_id(invite_regex):
                ss = session()
                r = ss.get(
                    f"https://discord.com/api/v9/invites/{invite_regex}?inputValue={invite_regex}&with_counts=true&with_expiration=true",
                )
                cmd().dbg('NAME + ID GETTER', r.status_code, r.text)
                if r.status_code == 200: 
                    data = r.json()['guild']
                    return r.json()['guild_id'], data['name']
                else:
                    return None, None  
        
            def check_invite(invite_regex):
                ss = session()
                r = ss.get(
                    f"https://discord.com/api/v9/invites/{invite_regex}?inputValue={invite_regex}&with_counts=true&with_expiration=true",
                )
                cmd().dbg('CHECK INVITE', r.status_code, r.text)
                if r.status_code == 200: 
                    return True
                else:
                    return False

            def main():
                cmd().preare('Guild manager/Joiner')
                invite = cmd().ask('INVITE')
                match = re.search(r'(?:(?:http:\/\/|https:\/\/)?discord\.gg\/|discordapp\.com\/invite\/|discord\.com\/invite\/)?([a-zA-Z0-9-]+)', invite)
                if match: invite =  match.group(1)
                invite_regex = invite
                while not tool.guild_manager.joiner.check_invite(invite):
                    cmd().log('JOINER', 'Invalid invite')
                    invite = cmd().ask('INVITE')
                    match = re.search(r'(?:(?:http:\/\/|https:\/\/)?discord\.gg\/|discordapp\.com\/invite\/|discord\.com\/invite\/)?([a-zA-Z0-9-]+)', invite)
                    if match: invite =  match.group(1)
                    invite_regex = invite
                cmd().log('JOINER', 'Valid invite')

                if cfg().online(): thread.single(tool.online, get.tokens())
                thread.single(tool.guild_manager.joiner.join, get.tokens(), invite_regex)

        class leaver:
            def leave(token, guildid):
                payload = {
                    "lurking": False,
                }
                ss = session()
                r = ss.delete(
                    f"https://discord.com/api/v9/users/@me/guilds/{guildid}",
                    json=payload,
                    headers=headers.get(token, payload)
                )
                cmd().dbg('LEAVER', r.status_code, r.text)
                if r.status_code == 204:
                    cmd().good(token, 'Left', r.status_code)

                elif r.status_code == 400:
                    cmd().captha(token, r.status_code)

                elif r.status_code == 429:
                    cmd().ratelimit(token, r.status_code, r.json())
                    time.sleep(float(r.json()['retry_after']))
                    tool.guild_manager.leaver.leave(token, guildid)

                elif r.status_code == 403:
                    cmd().bad(token, 'Locked', r.status_code, r.text)

                elif r.status_code == 404:
                    cmd().bad(token, 'Not in guild', r.status_code, r.text)

                elif r.status_code == 401:
                    cmd().bad(token, 'Unauthorized', r.status_code, r.text)

                else:   
                    cmd().bad(token, 'Other', r.status_code, r.text)

            def main():
                cmd().preare('Guild manager/Leaver')
                guildid = cmd().ask('GUILD ID')
                if cfg().online(): thread.single(tool.online, get.tokens())
                thread.single(tool.guild_manager.leaver.leave, get.tokens(), guildid)

        class guild_checker:
            def check_guilds(token, guildid):
                ss = session()
                r = ss.get(
                    f"https://discord.com/api/v9/guilds/{guildid}",
                    headers=headers.get(token)
                )
                cmd().dbg('GUILD CHECKER', r.status_code, r.text)
                if r.status_code == 200:
                    cmd().good(token, 'Found', r.status_code)

                elif r.status_code == 400:
                    cmd().captha(token, r.status_code)

                elif r.status_code == 429:
                    cmd().ratelimit(token, r.status_code, r.json())
                    time.sleep(float(r.json()['retry_after']))
                    tool.guild_manager.guild_checker.check_guilds(token, guildid)

                elif r.status_code == 403:
                    if 'code' in r.json() and r.json()['code'] == 50001:
                        cmd().bad(token, 'Not found', r.status_code, r.text)

                    else:
                        cmd().bad(token, 'Locked', r.status_code, r.text)
                        
                elif r.status_code == 404:
                    cmd().bad(token, 'Not found', r.status_code, r.text)

                elif r.status_code == 401:
                    cmd().bad(token, 'Unauthorized', r.status_code, r.text)

                else:   
                    cmd().bad(token, 'Other', r.status_code, r.text)

            def main():
                guildid = cmd().ask('GUILD ID')
                if cfg().online(): thread.single(tool.online, get.tokens())
                thread.single(tool.guild_manager.guild_checker.check_guilds, get.tokens(), guildid)

    class checker:      
        def check(token):
            ss = session()
            r = ss.get(
                f"https://discord.com/api/v9/users/@me",
                headers=headers.get(token),
            )

            state = ss.get(
                'https://discord.com/api/v9/users/@me/library',
                headers=headers.get(token)
            ).status_code

            cmd().dbg('CHECKER', state, r.text)
            if state == 200:
                mfa = r.json()['mfa_enabled']
                ev = r.json()['verified']
                email = r.json()['email']
                phone = r.json()['phone']
                nitro = 'NITRO PAID ONLY'
                if mfa:
                    mfa = f'{cmd().g}[MFA]'
                else:
                    mfa = f'{cmd().r}[MFA]'

                if ev:
                    ev = f'{cmd().g}[EV]'
                else:
                    ev = f'{cmd().r}[EV]'

                if phone:
                    phone = f'{cmd().g}[PHONE]'
                else:
                    phone = f'{cmd().r}[PHONE]'
                
                if email:
                    domain = email.split("@")[-1]
                else:
                    domain = ''
                cmd().good(token, 'UNLOCKED', state, f'{mfa} {ev} ~> {domain} {phone} {nitro}{cmd().b}')
                return True, token

            elif state == 403:
                cmd().bad(token, 'Locked', state, r.text)
            
            elif state == 401:
                cmd().bad(token, 'Invalid', state, r.text)

            elif state == 429:
                cmd().ratelimit(token, state, r.json())
                time.sleep(float(r.json()['retry_after']))
                tool.checker.check(token)

            elif state == 401:
                cmd().bad(token, 'Unauthorized', state, r.text)
            
            else:
                cmd().bad(token, 'Invalid', state, r.text)

            return False, token

        def check_token(token, keep):
            valid, token = tool.checker.check(token)

            if keep:
                if valid:
                    with open(f'data\\tokens.txt', 'a') as f:
                        f.write(token + '\n')

        def check_combo(email, password, token, keep):
            valid, token = tool.checker.check(token)

            if keep:
                if valid:
                    with open(f'data\\combo_tokens.txt', 'a') as f:
                        f.write(f'{email}:{password}:{token}' + '\n')


        def main():
            cmd().preare('Checker')
            tokenfile = 'data\\combo_tokens.txt' if cfg().prefer_combo_tokens() else 'data\\tokens.txt'
            dupes = cmd().askyn('REMOVE DUPLICATES')
            keep = cmd().askyn('KEEP VALID ONLY')
            if dupes:
                with open(tokenfile, 'r') as f:
                    lines = set(f.readlines())

                with open(tokenfile, 'w') as f:
                    f.writelines(line.strip() + '\n' for line in lines)
                    
            if keep:
                if cfg().prefer_combo_tokens():
                    cmd().log('CHECKER', 'Combo mode is selected, tokens will be saved to combo_tokens.txt')
                else:
                    cmd().log('CHECKER', 'Token mode is selected, tokens will be saved to tokens.txt')

            tokens = get.tokens()
            files.backup_tokens(tokens)
            if keep:
                open(tokenfile, 'w')

            if cfg().online(): thread.single(tool.online, tokens)
            if cfg().prefer_combo_tokens():
                thread.single_c(tool.checker.check_combo, get.tokens(), keep)
            else:
                thread.single(tool.checker.check_token, tokens, keep)
    
    class spammer:
        def send_messages(token, message, guildid, channelid):
            while True:
                ss = session()
                new_message = tool.spammer.replace(message)
                payload = {
                    "content": new_message,
                }
                r = ss.post(
                    f"https://discord.com/api/v9/channels/{channelid}/messages",
                    headers=headers.get(token, payload),
                    json=payload
                )
                cmd().dbg('SZPAMMER', r.status_code, r.text)

                if r.status_code == 200:
                    cmd().good(token, 'Sent', r.status_code)
                    continue

                elif r.status_code == 400:
                    if 'code' in r.json() and r.json()['code'] == 200000:
                        cmd().bad(token, 'Too many pings', r.status_code, r.text)
                    else:
                        cmd().captha(token, r.status_code)
                    break
                elif r.status_code == 429:
                    cmd().ratelimit(token, r.status_code, r.json())
                    time.sleep(float(r.json()['retry_after']))
                    continue

                elif r.status_code == 401:
                    cmd().bad(token, 'Invalid', r.status_code), r.text
                    break
                
                elif r.status_code == 403:
                    if 'code' in r.json() and r.json()['code'] == 50001:
                        cmd().bad(token, 'No acces', r.status_code, r.text)
                    else:
                        cmd().bad(token, 'Locked', r.status_code, r.text)
                    break

                elif r.status_code == 401:
                    cmd().bad(token, 'Unauthorized', r.status_code, r.text)
                    break

                else:   
                    cmd().bad(token, 'Other', r.status_code, r.text)
                    break

        def random_string(x):
            return ''.join(random.choices(string.ascii_letters + string.digits, k=x))
        
        def get_emojis():
            if not os.path.exists('data\\emojis.txt'):
                emojis = []
                def extract(text):
                    emoji_pattern = re.compile('['
                                        u'\U0001F600-\U0001F64F'
                                        u'\U0001F300-\U0001F5FF'
                                        u'\U0001F680-\U0001F6FF'
                                        u'\U0001F1E0-\U0001F1FF'
                                        u'\U00002702-\U000027B0'
                                        u'\U000024C2-\U0001F251'
                                        ']+', flags=re.UNICODE)
                    return emoji_pattern.findall(text)
                
                for url in [
                    'https://emojis.wiki/smileys-and-emotion-category/',
                    'https://emojis.wiki/people-and-body-category/',
                    'https://emojis.wiki/animals-and-nature-category/',
                    'https://emojis.wiki/food-and-drink-category/',
                    'https://emojis.wiki/travel-and-places-category/',
                    'https://emojis.wiki/activities-category/',
                    'https://emojis.wiki/objects-category/',
                    'https://emojis.wiki/symbols-category/',
                    'https://emojis.wiki/holidays/'
                ]:
                    cmd().log('SPAMMER', f'Getting emojis from {url}...')
                    r = requests.get(url)
                    emojis.extend(extract(r.text))
                
                with open('data\\emojis.txt', 'w', encoding='utf-8') as f:
                    for emoji in emojis:
                        f.write(emoji + '\n')

        def random_emojis(x):
            if not os.path.exists('data\\emojis.txt'):
                tool.spammer.get_emojis()

            with open('data\\emojis.txt', 'r', encoding='utf-8') as f:
                emojis = [line.strip() for line in f if re.match(r'[\U0001F000-\U0001F9FF]', line)]
            
            return ''.join(random.choices(emojis, k=x))

        def replace(text):
            def replace_func(match):
                command, value = match.group(1, 2)
                if command == 'str':
                    return tool.spammer.random_string(int(value))
                elif command == 'emoji':
                    return tool.spammer.random_emojis(int(value))
                else:
                    return match.group(0)

            return re.sub(r'\((str|emoji)=(\d+)\)', replace_func, text)          

        def main():
            cmd().preare('Spammer')
            thread_amt = cmd().ask('THREADS')
            channelid = cmd().ask('CHANNEL ID')
            cmd().log('SPAMMER TTS', 'TTS IS PAID ONLY')
            cmd().options('''
(ping=10) ~> Pings 10 people (PAID ONLY)
(emoji=5) ~> Adds 5 random emojis to the message
(str=15) ~> Adds 15 random letters/numbers to the message
EXAMPLE ~> Raided (ping=5) real (str=100) sigmaer (emoji=11)
''')
            message = cmd().ask('MESSAGE')
            if '(ping=' in message:
                cmd().paid()
            guildid = None

            if '(emoji=' in message:
                if not os.path.exists('data\\emojis.txt'):
                    cmd().log('SPAMMER', 'Emojis not saved, getting them...')
                    tool.spammer.get_emojis()
        

            tokens = tool.channel_acces(channelid)
            if cfg().online(): thread.single(tool.online, tokens)
            thread.multi(thread_amt, tool.spammer.send_messages, tokens, message, guildid, channelid)

    class bypasses:
        def main():
            cmd().preare('Bypasses')
            cmd().options('''
01 ~> Reactor
02 ~> Button clicker (PAID)
03 ~> Rule bypass
04 ~> Onboard bypass (PAID)
05 ~> Restorecord (Non captcha only) (PAID)
06 ~> Back
''')
            c = cmd().ask('CHOICE')
            if c == '1':
                tool.bypasses.reactor.main()
            elif c == '2':
                cmd().paid()
            elif c == '3':
                tool.bypasses.rule_accept.main()
            elif c == '4':
                cmd().paid()
            elif c == '5':
                cmd().paid()
            elif c == '6':
                return
            else:
                cmd().log('Bypasses', 'Invalid option')

        class reactor:
            def react(token, messagelink, reaction):
                ss = session()
                guildid, channelid, messageid = tool.link_transform(messagelink)
                cmd().dbg(guildid, channelid, messageid)
                r = ss.put(
                    f"https://discord.com/api/v9/channels/{channelid}/messages/{messageid}/reactions/{reaction}/%40me?location=Message&type=0",
                    headers=headers.get(token)
                )
                cmd().dbg('REACT', r.status_code, r.text)
                if r.status_code == 204:
                    cmd().good(token, f'Reacted', r.status_code,)

                elif r.status_code == 400:
                    if 'code' in r.json() and r.json()['code'] == 10014:
                        cmd().bad(token, 'Unknown emoji', r.status_code, r.text)
                    else:
                        cmd().captha(token, r.status_code)

                elif r.status_code == 429:
                    cmd().ratelimit(token, r.status_code, r.json())
                    time.sleep(float(r.json()['retry_after']))
                    tool.bypasses.reactor.react(token, messagelink, reaction)

                elif r.status_code == 403:
                    if 'code' in r.json() and r.json()['code'] == 30010:
                        cmd().bad(token, 'Max reactions', r.status_code, r.text)
                    else:
                        cmd().bad(token, 'Locked', r.status_code, r.text)

                elif r.status_code == 401:
                    cmd().bad(token, 'Unauthorized', r.status_code, r.text)

                else:   
                    cmd().bad(token, 'Other', r.status_code, r.text)

            def get_reactions(messagelink):
                guildid, channelid, messageid = tool.link_transform(messagelink)
                cmd().dbg(guildid, channelid, messageid)
                got = False
                tokens = tool.inside_guild(guildid)
                reactions_list = []
                for token in tokens:
                    if not got:
                        ss = session()
                        r = ss.get(
                            f"https://discord.com/api/v9/channels/{channelid}/messages?limit=50",
                            headers=headers.get(token),
                        )
                        cmd().dbg('GET REACTS', r.status_code, r.text)
                        if r.status_code == 200:
                            got = True
                            for message in r.json():
                                if message['id'] == messageid:
                                    reactions = message['reactions']
                                    for reacts in reactions:
                                        if reacts:
                                            emoji_name = reacts['emoji'].get('name', '')
                                            emoji_count = reacts.get('count', 0)
                                            reactions_list.append(f'{emoji_name}:{emoji_count}')
                return reactions_list

            def main():
                cmd().preare('Bypasses/Reactor')
                messagelink = cmd().ask('MESSAGE LINK')
                guildid, channelid, messageid = tool.link_transform(messagelink)
                cmd().dbg(guildid, channelid, messageid)
                tokens = tool.channel_acces(channelid)
                reactions = tool.bypasses.reactor.get_reactions(messagelink)
                cmd().dbg(reactions)
                
                if not reactions:
                    cmd().log('REACTOR', 'No emojis were found')
                    return
                
                for i, reaction in enumerate(reactions, start=1):
                    reactname, reactamt = reaction.split(":")
                    print(f'{cmd().b}{i}{cmd().r} ~> {cmd().b} {reactname}  Amount{cmd().r} ~> {cmd().b} {reactamt}')

                try:
                    selected_index = int(cmd().ask("CHOICE")) - 1
                    if 0 <= selected_index < len(reactions):
                        selected_reaction = reactions[selected_index].split(":")[0]
                        if cfg().online(): thread.single(tool.online, tokens)
                        thread.single(tool.bypasses.reactor.react, tokens, messagelink, selected_reaction)
                    else:
                        cmd().log('REACTOR', 'Not a valid option')
                except ValueError:
                    cmd().log('REACTOR', 'Not a valid option')
                    return 
                
        class rule_accept:
            def get_rule_info(tokens, guildid):
                found = False
                for token in tokens:
                    if not found:
                        ss = session()
                        r = ss.get(
                            f"https://discord.com/api/v9/guilds/{guildid}/member-verification",
                            headers=headers.get(token)
                        ) 
                        
                        if r.status_code == 200:
                            found = True
                            return r.json()
                        else:
                            continue
                
                if not found:
                    return None


            def accept(token, guildid, data):
                ss = session()
                payload = {
                    "version": data["version"],
                    "form_fields": [
                        {
                            "field_type": field["field_type"],
                            "label": field["label"],
                            "description": field["description"],
                            "automations": field["automations"],
                            "required": field["required"],
                            "values": field["values"],
                            "response": True
                        } for field in data["form_fields"]
                    ]
                }
                r = ss.put(
                    f"https://discord.com/api/v9/guilds/{guildid}/requests/@me",
                    headers=headers.get(token, payload),
                    json=payload
                )
                cmd().dbg('ACCEPT RULES', r.status_code, r.text)
                if r.status_code == 201:
                    cmd().good(token, 'Accepted', r.status_code)
                
                elif r.status_code == 400:
                    cmd().captha(token, r.status_code)

                elif r.status_code == 429:
                    cmd().ratelimit(token, r.status_code, r.json())
                    time.sleep(float(r.json()['retry_after']))
                    tool.bypasses.rule_accept.accept(token, guildid)

                elif r.status_code == 403:
                    cmd().bad(token, 'Locked', r.status_code, r.text)

                elif r.status_code == 401:
                    cmd().bad(token, 'Unauthorized', r.status_code, r.text)

                else:   
                    cmd().bad(token, 'Other', r.status_code, r.text)
        
            def main():
                cmd().preare('Bypasses/Rule bypass')
                guildid = cmd().ask('GUILD ID')
                tokens = tool.inside_guild(guildid)
                data = tool.bypasses.rule_accept.get_rule_info(tokens, guildid)
                if data == None:
                    cmd().log('RULE BYPASS', 'Failed to get data about rules...')
                    return
                if cfg().online(): thread.single(tool.online, tokens)
                thread.single(tool.bypasses.rule_accept.accept, tokens, guildid, data)

    class combo_to_token:
        def main():
            combo_tokens = get.combo_tokens()
            if not cfg().prefer_combo_tokens():
                tokens = get.tokens()
            with open('data\\tokens.txt', 'w') as f:
                if tokens:
                    for token in tokens:
                        f.write(f'{token}' + '\n')
                for token in combo_tokens:
                    f.write(f'{token}' + '\n')

    class onliner:
        def online(token):
            def recieve():
                r = ws.recv()
                if r:
                    return json.loads(r)

            def send(request):
                ws.send(json.dumps(request))
            
            def heartbeat(interval):
                while True:
                    time.sleep(interval)
                    payload = {
                        'op': 1,
                        'd': 'null'
                    }
                    send(payload)

            ws = websocket.WebSocket()
            ws.connect('wss://gateway.discord.gg/?v=9&encoding=json')
            event = recieve()

            interval = event['d']['heartbeat_interval'] / 1000
            cmd().good(token, f'Got interval ~> {interval}', 'None')
            cmd().dbg('GOT INTERVAL ON:', token, interval)
            threading.Thread(target=heartbeat, args=interval).start()
            cmd().dbg('STARTED HEARTBEAT THREAD ON', token)

            tool.change_status.change(token, 'WjEKCAoGb25saW5lEiEKH/Cfm5EgZGlzY29yZC5nZy9odERGTjU4OXhhIPCfm5EaAggB')
            ws.send(
                json.dumps({
                "op": 2,
                "d": {
                    "token": token,
                    "capabilities": 8189,
                    "properties": {
                        "os": "Windows",
                        "browser": "Chrome",
                        "device": "",
                        "system_locale": "en-US",
                        "browser_user_agent": headers.ua,
                        "browser_version": "111.0.0.0",
                        "os_version": "10",
                        "referrer": "",
                        "referring_domain": "",
                        "referrer_current": "",
                        "referring_domain_current": "",
                        "release_channel": "stable",
                        "client_build_number": 199933,
                        "client_event_source": None,
                        "design_id": 0
                    },
                    "presence": {
                        "status": random.choice(["online", "idle", "dnd"]),
                        "since": 0,
                        "activities": [{
                            "name": "Custom Status",
                            "type": 4,
                            "state": main_name,
                            "emoji": "💣"
                        }],
                        "afk": False
                    },
                    "compress": False,
                    "client_state": {
                        "guild_versions": {},
                        "highest_last_message_id": "0",
                        "read_state_version": 0,
                        "user_guild_settings_version": -1,
                        "user_settings_version": -1,
                        "private_channels_version": "0",
                        "api_code_version": 0
                    }
                }
            }))
            cmd().good(token, 'Onlined', 'None')
            event = recieve()
            if event:
                pass
            else:
                event = 'NO EVENT RECIEVED'
            cmd().dbg(event)

        def main():
            cmd().preare('Onliner')
            thread.single(tool.onliner.online, get.tokens())

    class humanizer:
        def add_avatar(token):
            with open('data\\avatar.png', 'rb') as f:
                avatar = f.read()
            ss = session()
            payload = {
                    "avatar": f"data:image/png;base64,{(base64.b64encode(avatar).decode('utf-8'))}"
            } 
            r = ss.patch(
                "https://discord.com/api/v9/users/@me",
                headers=headers.get(token, payload),
                json=payload
            )
            cmd().dbg('AVATAR ADDER', r.status_code, r.text)
            if r.status_code == 200:
                cmd().good(token, 'Avatar added', r.status_code)

            elif r.status_code == 400:
                cmd().captha(token, r.status_code)

            elif r.status_code == 429:
                cmd().ratelimit(token, r.status_code, r.json())
                time.sleep(float(r.json()['retry_after']))
                tool.humanizer.add_avatar(token)

            elif r.status_code == 403:
                cmd().bad(token, 'Locked', r.status_code, r.text)

            elif r.status_code == 401:
                cmd().bad(token, 'Unauthorized', r.status_code, r.text)

            else:   
                cmd().bad(token, 'Other', r.status_code, r.text)

        def add_bio(token):
            ss = session()
            r = requests.post(
                'https://api.kanye.rest/',
            )
            if r.status_code == 200:
                bio = r.json()['quote']
            else:
                bio = 'Not siure'
            
            payload = {
                "bio": bio
            }

            r = ss.patch(
                "https://discord.com/api/v9/users/%40me/profile",
                headers=headers.get(token, payload),
                json=payload,
            )

            cmd().dbg('BIO ADDER', r.status_code, r.text)
            if r.status_code == 200:
                cmd().good(token, f'Bio added', r.status_code,)

            elif r.status_code == 400:
                cmd().captha(token, r.status_code)

            elif r.status_code == 429:
                cmd().ratelimit(token, r.status_code, r.json())
                time.sleep(float(r.json()['retry_after']))
                tool.humanizer.add_bio(token)

            elif r.status_code == 401:
                cmd().bad(token, 'Unauthorized', r.status_code, r.text)

            elif r.status_code == 403:
                cmd().bad(token, 'Locked', r.status_code, r.text)

            else:   
                cmd().bad(token, 'Other', r.status_code, r.text)

        
        def change_display(token):
            ss = session()
            with open('data\\names.txt', 'r', encoding='utf-8') as f:
                names = f.read().splitlines()
            payload = {
                "global_name": random.choice(names)
            }
            r = ss.patch(
                "https://discord.com/api/v9/users/@me",
                headers=headers.get(token, payload),
                json=payload
            )
            cmd().dbg('DISPLAY CHANGER', r.status_code, r.text)
            if r.status_code == 200:
                cmd().good(token, 'Display changed', r.status_code)

            elif r.status_code == 400:
                cmd().captha(token, r.status_code)

            elif r.status_code == 429:
                cmd().ratelimit(token, r.status_code, r.json())
                time.sleep(float(r.json()['retry_after']))
                tool.humanizer.change_display(token)

            elif r.status_code == 403:
                cmd().bad(token, 'Locked', r.status_code, r.text)

            elif r.status_code == 401:
                cmd().bad(token, 'Unauthorized', r.status_code, r.text)

            else:   
                cmd().bad(token, 'Other', r.status_code, r.text)

        def add_squad(token):
            ss = session()
            payload = {
                "house_id":random.randint(1, 3)
            }

            r = ss.post(
                "https://discord.com/api/v9/hypesquad/online",
                headers=headers.get(token, payload),
                json=payload,
            )

            cmd().dbg('HYPE ADDER', r.status_code, r.text)
            if r.status_code == 204:
                cmd().good(token, f'Squad added', r.status_code,)

            elif r.status_code == 400:
                cmd().captha(token, r.status_code)

            elif r.status_code == 429:
                cmd().ratelimit(token, r.status_code, r.json())
                time.sleep(float(r.json()['retry_after']))
                tool.humanizer.add_squad(token)

            elif r.status_code == 401:
                cmd().bad(token, 'Unauthorized', r.status_code, r.text)

            elif r.status_code == 403:
                cmd().bad(token, 'Locked', r.status_code, r.text)

            else:   
                cmd().bad(token, 'Other', r.status_code, r.text)

        def add_pron(token):
            ss = session()
            prons = [
                "he/him",
                "she/her",
                "they/them",
                "xe/xem",
                "ze/zir",
                "it/its",
                "e/em",
                "per/pers",
                "ve/ver",
                "ey/em",
                "hir/hirs",
                "thon/thon",
                "fae/faer",
                "ae/aer",
                "ne/nem",
                "ne/nir",
                "ve/vis",
                "ae/aer",
                "hu/hum",
                "jee/jem",
                "kit/kits",
                "ley/ler",
                "loop/loops",
                "mo/mos",
                "na/na",
                "ou/ous",
                "vana/dium",
                'disc\ord',
                'ret/ard',
                'own/ed'
            ]
            payload = {
                "pronouns": random.choice(prons)
            }

            r = ss.patch(
                "https://discord.com/api/v9/users/%40me/profile",
                headers=headers.get(token, payload),
                json=payload,
            )

            cmd().dbg('PRON ADDER', r.status_code, r.text)
            if r.status_code == 200:
                cmd().good(token, f'Pron added', r.status_code,)

            elif r.status_code == 400:
                cmd().captha(token, r.status_code)

            elif r.status_code == 429:
                cmd().ratelimit(token, r.status_code, r.json())
                time.sleep(float(r.json()['retry_after']))
                tool.humanizer.enable_dev(token)

            elif r.status_code == 401:
                cmd().bad(token, 'Unauthorized', r.status_code, r.text)

            elif r.status_code == 403:
                cmd().bad(token, 'Locked', r.status_code, r.text)

            else:   
                cmd().bad(token, 'Other', r.status_code, r.text)

        def enable_dev(token):
            ss = session()
            payload = {"settings":"agQIARAB"}

            r = ss.patch(
                "https://discord.com/api/v9/users/@me/settings-proto/1",
                headers=headers.get(token, payload),
                json=payload,
            )
            cmd().dbg('DEVMODE ENABLER', r.status_code, r.text)
            if r.status_code == 200:
                cmd().good(token, f'Devmode enabled', r.status_code,)

            elif r.status_code == 400:
                cmd().captha(token, r.status_code)

            elif r.status_code == 429:
                cmd().ratelimit(token, r.status_code, r.json())
                time.sleep(float(r.json()['retry_after']))
                tool.humanizer.add_pron(token)

            elif r.status_code == 401:
                cmd().bad(token, 'Unauthorized', r.status_code, r.text)

            elif r.status_code == 403:
                cmd().bad(token, 'Locked', r.status_code, r.text)

            else:   
                cmd().bad(token, 'Other', r.status_code, r.text)

        def main():
            cmd().preare('Humanizer')
            tokens = get.tokens()
            if cfg().online(): thread.single(tool.online, tokens)
            thread.single(tool.humanizer.add_avatar, tokens)
            thread.single(tool.humanizer.change_display, tokens)
            thread.single(tool.humanizer.add_bio, tokens)
            thread.single(tool.humanizer.add_pron, tokens)
            thread.single(tool.humanizer.add_squad, tokens)

    class bio_changer:
        def add_bio(token, bio):
            ss = session()
            
            payload = {
                "bio": bio
            }

            r = ss.patch(
                "https://discord.com/api/v9/users/%40me/profile",
                headers=headers.get(token, payload),
                json=payload,
            )

            cmd().dbg('BIO ADDER', r.status_code, r.text)
            if r.status_code == 200:
                cmd().good(token, f'Added', r.status_code,)

            elif r.status_code == 400:
                cmd().captha(token, r.status_code)

            elif r.status_code == 429:
                cmd().ratelimit(token, r.status_code, r.json())
                time.sleep(float(r.json()['retry_after']))
                tool.bio_changer.add_bio(token)

            elif r.status_code == 403:
                cmd().bad(token, 'Locked', r.status_code, r.text)

            elif r.status_code == 401:
                cmd().bad(token, 'Unauthorized', r.status_code, r.text)

            else:   
                cmd().bad(token, 'Other', r.status_code, r.text)
            
        def main():
            cmd().preare('Bio changer')
            bio = cmd().ask('BIO')
            if cfg().online(): thread.single(tool.online, get.tokens())
            thread.single(tool.bio_changer.add_bio, get.tokens(), bio)

    class display_changer:
        def change_display(token, display):
            ss = session()
            
            payload = {
                "global_name": display
            }

            r = ss.patch(
                "https://discord.com/api/v9/users/@me",
                headers=headers.get(token, payload),
                json=payload,
            )

            cmd().dbg('DISPLAY CHANGER', r.status_code, r.text)
            if r.status_code == 200:
                cmd().good(token, f'Changed', r.status_code,)

            elif r.status_code == 400:
                cmd().captha(token, r.status_code)

            elif r.status_code == 429:
                cmd().ratelimit(token, r.status_code, r.json())
                time.sleep(float(r.json()['retry_after']))
                tool.display_changer.change_display(token)

            elif r.status_code == 403:
                cmd().bad(token, 'Locked', r.status_code, r.text)

            elif r.status_code == 401:
                cmd().bad(token, 'Unauthorized', r.status_code, r.text)

            else:   
                cmd().bad(token, 'Other', r.status_code, r.text)

        def main():
            cmd().preare('Display changer')
            display = cmd().ask('DISPLAY')
            if cfg().online(): thread.single(tool.online, get.tokens())
            thread.single(tool.display_changer.change_display, get.tokens(), display)

    class avatar_changer:
        def change_avatar(token, path):
            with open(path, 'rb') as f:
                avatar = f.read()
            ss = session()
            payload = {
                "avatar": f"data:image/png;base64,{(base64.b64encode(avatar).decode('utf-8'))}"
            }
            r = ss.patch(
                "https://discord.com/api/v9/users/@me",
                headers=headers.get(token, payload),
                json=payload
            )
            cmd().dbg('AVATAR CHANGER', r.status_code, r.text)
            if r.status_code == 200:
                cmd().good(token, 'Changed', r.status_code)

            elif r.status_code == 400:
                cmd().captha(token, r.status_code)

            elif r.status_code == 429:
                cmd().ratelimit(token, r.status_code, r.json())
                time.sleep(float(r.json()['retry_after']))
                tool.avatar_changer.change_avatar(token)

            elif r.status_code == 403:
                cmd().bad(token, 'Locked', r.status_code, r.text)

            elif r.status_code == 401:
                cmd().bad(token, 'Unauthorized', r.status_code, r.text)

            else:   
                cmd().bad(token, 'Other', r.status_code, r.text)        

        def main():
            cmd().preare('Avatar changer')
            root = tk.Tk()
            root.withdraw()
            path = filedialog.askopenfilename()
            if cfg().online(): thread.single(tool.online, get.tokens())
            thread.single(tool.avatar_changer.change_avatar, get.tokens(), path)       

    class reaction_bomber:
        def react(token, messagelink):
            while True: 
                ss = session()
                guildid, channelid, messageid = tool.link_transform(messagelink)
                cmd().dbg(guildid, channelid, messageid)
                with open('data\\emojis.txt', 'r', encoding='utf-8') as f:
                    emojis = [line.strip() for line in f if re.match(r'[\U0001F000-\U0001F9FF]', line)]
                reaction = random.choice(emojis)
                r = ss.put(
                    f"https://discord.com/api/v9/channels/{channelid}/messages/{messageid}/reactions/{reaction}/%40me?location=Message&type=0",
                    headers=headers.get(token)
                )
                cmd().dbg('REACT BOMBER', r.status_code, r.text)
                if r.status_code == 204:
                    cmd().good(token, f'Reacted', r.status_code,)
                    continue

                elif r.status_code == 400:
                    if 'code' in r.json() and r.json()['code'] == 10014:
                        cmd().bad(token, 'Unknown emoji', r.status_code, r.text)
                    else:
                        cmd().captha(token, r.status_code)
                    continue

                elif r.status_code == 429:
                    cmd().ratelimit(token, r.status_code, r.json())
                    time.sleep(float(r.json()['retry_after']))
                    continue

                elif r.status_code == 403:
                    if 'code' in r.json() and r.json()['code'] == 30010:
                        cmd().bad(token, 'Max reactions', r.status_code, r.text)
                    else:
                        cmd().bad(token, 'Locked', r.status_code, r.text)
                    break

                elif r.status_code == 401:
                    cmd().bad(token, 'Unauthorized', r.status_code, r.text)
                    break

                else:   
                    cmd().bad(token, 'Other', r.status_code, r.text)  
                    break    

        def main():
            cmd().preare('Reaction bomber')
            messagelink = cmd().ask('MESSAGE LINK')
            thread_amt = cmd().ask('THREADS')
            guildid, channelid, messageid = tool.link_transform(messagelink)
            tokens = tool.channel_acces(guildid)
            if cfg().online(): thread.single(tool.online, tokens)
            thread.multi(thread_amt, tool.reaction_bomber.react, tokens, messagelink)   
    
    class mass_report:
        def report(token, messagelink, reason):
            guildid, channelid, messageid = tool.link_transform(messagelink)
            cmd().dbg(guildid, channelid, messageid)
            while True:
                ss = session()
                if reason == 'age':
                    payload = {
                        "version": "1.0",
                        "variant": "4",
                        "language": "en",
                        "breadcrumbs": [3,29,39,74],
                        "elements": {},
                        "channel_id": channelid,
                        "message_id": messageid,
                        "name": "message"
                    }
                elif reason == 'selfharm':
                    payload = {
                        "version": "1.0",
                        "variant": "4",
                        "language": "en",
                        "breadcrumbs": [3,29,41,75],
                        "elements": {},
                        "channel_id": channelid,
                        "message_id": messageid,
                        "name": "message"
                    } 
                elif reason == 'drugs':
                    payload = {
                        "version": "1.0",
                        "variant": "4",
                        "language": "en",
                        "breadcrumbs": [3,29,71],
                        "elements": {},
                        "channel_id": channelid,
                        "message_id": messageid,
                        "name": "message"
                    }
                elif reason == 'fraud':
                    payload = {
                        "version": "1.0",
                        "variant": "4",
                        "language": "en",
                        "breadcrumbs": [3,29,68,107],
                        "elements": {},
                        "channel_id": channelid,
                        "message_id": messageid,
                        "name": "message"
                    }  
                elif reason == 'inpersona':
                    payload = {
                        "version": "1.0",
                        "variant": "4",
                        "language": "en",
                        "breadcrumbs": [3,29,68,104],
                        "elements": {},
                        "channel_id": channelid,
                        "message_id": messageid,
                        "name": "message"
                    }  
                elif reason == 'harrasment':
                    payload = {
                        "version": "1.0",
                        "variant": "4",
                        "language": "en",
                        "breadcrumbs": [3,24,49],
                        "elements": {},
                        "channel_id": channelid,
                        "message_id": messageid,
                        "name": "message"
                    }  
                elif reason == 'expose':
                    payload = {
                        "version": "1.0",
                        "variant": "4",
                        "language": "en",
                        "breadcrumbs": [3,28,25],
                        "elements": {
                            "pii_select": [
                                "physical_address",
                                "phone_info",
                                "email_address",
                                "credit_info",
                                "legal_name",
                                "ip_address",
                                "revenge_porn",
                                "face_pic"
                            ]
                        },
                        "channel_id": channelid,
                        "message_id": messageid,
                        "name":"message"
                    }       
                else:                                     
                    payload = {
                        "version": "1.0",
                        "variant": "4",
                        "language": "en",
                        "breadcrumbs": [3,29,39,74],
                        "elements": {},
                        "channel_id": channelid,
                        "message_id": messageid,
                        "name": "message"
                    }
                r = ss.post(
                    f"https://discord.com/api/v9/reporting/message",
                    headers=headers.get(token, payload),
                    json=payload
                )
                cmd().dbg('MASS REPORT', r.status_code, r.text)
                if r.status_code == 200:
                    cmd().good(token, f'Reported', r.status_code)
                    continue

                elif r.status_code == 400:
                    cmd().captha(token, r.status_code)
                    continue

                elif r.status_code == 429:
                    cmd().ratelimit(token, r.status_code, r.json())
                    time.sleep(float(r.json()['retry_after']))
                    continue

                elif r.status_code == 403:
                    cmd().bad(token, 'Locked', r.status_code, r.text)
                    break

                elif r.status_code == 401:
                    cmd().bad(token, 'Unauthorized', r.status_code, r.text)
                    break

                else:   
                    cmd().bad(token, 'Other', r.status_code, r.text)
                    break

        def main():
            cmd().preare('Mass report')
            cmd().options('''
1 ~> Age
2 ~> Self harm
3 ~> Drugs
4 ~> Fraud
5 ~> Inpersonation
6 ~> Harrasment
7 ~> Exposing information
''')
            choice = cmd().ask('CHOICE')
            if choice == '1':
                reason = 'age'
            elif choice == '2':
                reason = 'selfharm'
            elif choice == '3':
                reason = 'drugs'
            elif choice == '4':
                reason = 'fraud'
            elif choice == '5':
                reason = 'inpersona'
            elif choice == '6':
                reason = 'harrasment'
            elif choice == '7':
                reason = 'expose'
            messagelink = cmd().ask('MESSAGE LINK')
            thread_amt = cmd().ask('THREADS')
            if cfg().online(): thread.single(tool.online, get.tokens())
            thread.multi(thread_amt, tool.mass_report.report, get.tokens(), messagelink, reason)  
            
    class thread_spammer:
        def create(token, channelid, name):
                while True:
                    ss = session()                                         
                    payload = {
                        "name": name,
                        "type": 11,
                        "auto_archive_duration": 4320,
                        "location": "Thread Browser Toolbar"
                    }
                    r = ss.post(
                        f"https://discord.com/api/v9/channels/{channelid}/threads",
                        headers=headers.get(token, payload),
                        json=payload
                    )
                    cmd().dbg('THREAD SPAMMMER', r.status_code, r.text)
                    if r.status_code == 200:
                        cmd().good(token, f'Created', r.status_code)
                        continue

                    elif r.status_code == 400:
                        cmd().captha(token, r.status_code)
                        continue

                    elif r.status_code == 429:
                        cmd().ratelimit(token, r.status_code, r.json())
                        time.sleep(float(r.json()['retry_after']))
                        continue

                    elif r.status_code == 403:
                        if 'code' in r.json() and r.json()['code'] == 50001:
                            cmd().bad(token, 'No acces', r.status_code, r.text)
                        else:
                            cmd().bad(token, 'Locked', r.status_code, r.text)
                        break

                    elif r.status_code == 401:
                        cmd().bad(token, 'Unauthorized', r.status_code, r.text)
                        break

                    else:   
                        cmd().bad(token, 'Other', r.status_code, r.text)
                        break

        def main():
            cmd().preare('Thread spammer')
            channelid = cmd().ask('CHANNEL ID')
            name = cmd().ask('NAME')
            thread_amt = cmd().ask('THREADS')
            tokens = tool.channel_acces(channelid)
            if cfg().online(): thread.single(tool.online, tokens)
            thread.multi(thread_amt, tool.thread_spammer.create, tokens, channelid, name)
    
    class friender:
        def send(token, username):
            ss = session()                                       
            payload = {
                'username': username, 
                'discriminator': None
            }
            r = ss.post(
                f"https://discord.com/api/v9/users/@me/relationships",
                headers=headers.get(token, payload),
                json=payload
            )
            cmd().dbg('FRIENDER', r.status_code, r.text)
            if r.status_code == 204 or r.status_code == 200:
                cmd().good(token, f'Friended', r.status_code)

            elif r.status_code == 400:
                try:
                    if 'code' in r.json() and r.json()['code'] == 80003:
                        cmd().bad(token, 'Cant self friend', r.status_code, r.text)
                    else:
                        cmd().captha(token, r.status_code)
                except:
                    cmd().bad(token, 'Other', r.status_code, r.text)

            elif r.status_code == 429:
                cmd().ratelimit(token, r.status_code, r.json())
                time.sleep(float(r.json()['retry_after']))
                tool.friender.send(token, username)

            elif r.status_code == 403:
                cmd().bad(token, 'Locked', r.status_code, r.text)

            elif r.status_code == 401:
                cmd().bad(token, 'Unauthorized', r.status_code, r.text)

            else:   
                cmd().bad(token, 'Other', r.status_code, r.text)

        def main():
            cmd().preare('Friender')
            username = cmd().ask('USERNAME')
            if cfg().online(): thread.single(tool.online, get.tokens())
            thread.single(tool.friender.send, get.tokens(), username)

    class vc_joiner:
        def connect_vc(token, channelid, guildid):
            try:
                ws = websocket.WebSocket()
                ws.connect("wss://gateway.discord.gg/?v=9&encoding=json")
                ws.send(json.dumps({
                    "op": 2,
                    "d": {
                        "token": token,
                        "properties": {
                            "$os": "windows",
                            "$browser": "Discord",
                            "$device": "desktop"
                        }
                    }
                }))

                ws.send(json.dumps({
                    "op": 4,
                    "d": {
                        "guild_id": guildid,
                        "channel_id": channelid,
                        "self_mute": False,
                        "self_deaf": False
                    }
                }))

                ws.close()
            except Exception as e:
                cmd().dbg(e)

        def main():
            cmd().preare('VC joiner')
            channelid = cmd().ask('CHANNEL ID')
            guildid = cmd().ask('GUILD ID')
            tokens = tool.channel_acces(channelid)
            if cfg().online(): thread.single(tool.online, tokens)
            thread.single(tool.vc_joiner.connect_vc, tokens, channelid, guildid)

    class vc_spammer:
        def get_sounds(token):
            ss = session()
            r = ss.get(
                "https://discord.com/api/v9/soundboard-default-sounds",
                headers=headers.get(token)
            )
            cmd().dbg(r.text, r.status_code)
            return r.json()
        
        def spam(token, channelid, guildid, sounds):
            while True:
                ss = session()
                sound = random.choice(sounds)
                name = sound['name']
                payload = {
                    "emoji_id": None,
                    "emoji_name": sound['emoji_name'],
                    "sound_id": sound['sound_id'],
                }
                r = ss.post(
                    f"https://discord.com/api/v9/channels/{channelid}/send-soundboard-sound",
                    headers=headers.get(token, payload),
                    json=payload
                )
                cmd().dbg('SOUNDBOARD SPAM', r.status_code, r.text)
                if r.status_code == 204:
                    cmd().good(token, f'Soundboarded {name}', r.status_code)
                    continue

                elif r.status_code == 400:
                    cmd().captha(token, r.status_code)
                    continue

                elif r.status_code == 429:
                    cmd().ratelimit(token, r.status_code, r.json())
                    time.sleep(float(r.json()['retry_after']))
                    continue

                elif r.status_code == 403:
                    if 'code' in r.json() and r.json()['code'] == 50168:
                        tool.vc_spammer.connect_vc(token, channelid, guildid)
                        continue
                    else:
                        cmd().bad(token, 'Locked', r.status_code, r.text)
                        break

                elif r.status_code == 401:
                    cmd().bad(token, 'Unauthorized', r.status_code, r.text)

                else:
                    cmd().bad(token, 'Other', r.status_code, r.text)
                    break


        def connect_vc(token, channelid, guildid):
            try:
                ws = websocket.WebSocket()
                ws.connect("wss://gateway.discord.gg/?v=9&encoding=json")
                ws.send(json.dumps({
                    "op": 2,
                    "d": {
                        "token": token,
                        "properties": {
                            "$os": "windows",
                            "$browser": "Discord",
                            "$device": "desktop"
                        }
                    }
                }))

                ws.send(json.dumps({
                    "op": 4,
                    "d": {
                        "guild_id": guildid,
                        "channel_id": channelid,
                        "self_mute": False,
                        "self_deaf": False
                    }
                }))

                cmd().good(token, 'Connected to VC', None)
            except Exception as e:
                cmd().dbg(e)

        def main():
            cmd().preare('VC spammer')
            channelid = cmd().ask('CHANNEL ID')
            guildid = cmd().ask('GUILD ID')
            thread_amt = cmd().ask('THREADS')
            tokens = tool.channel_acces(channelid)
            sounds = tool.vc_spammer.get_sounds(random.choice(tokens))
            if cfg().online(): thread.single(tool.online, tokens)
            thread.single(tool.vc_spammer.connect_vc, tokens, channelid, guildid)  
            thread.multi(thread_amt, tool.vc_spammer.spam, tokens, channelid, guildid, sounds)

    class mass_pin:
        def get_message_ids(token, channelid):
            ss = session()
            r = ss.get(
                f"https://discord.com/api/v9/channels/{channelid}/messages",
                headers=headers.get(token)
            )
            cmd().dbg(r.text, r.status_code)
            if r.status_code == 200:
                return [entry['id'] for entry in r.json()]
            else:
                return None
        
        def pin(token, channelid):
            messageids = tool.mass_pin.get_message_ids(token, channelid)
            if not messageids:
                cmd().bad(token, 'No messages found', None, None)
            while True:
                messageid = random.choice(messageids)
                ss = session()
                r = ss.put(
                    f"https://discord.com/api/v9/channels/{channelid}/pins/{messageid}",
                    headers=headers.get(token)
                )
                cmd().dbg('MASS PIN', r.status_code, r.text)
                if r.status_code == 204:
                    cmd().good(token, f'Pinned', r.status_code)
                    continue

                elif r.status_code == 400:
                    cmd().captha(token, r.status_code)
                    continue

                elif r.status_code == 429:
                    cmd().ratelimit(token, r.status_code, r.json())
                    time.sleep(float(r.json()['retry_after']))
                    continue

                elif r.status_code == 403:
                    cmd().bad(token, 'Locked', r.status_code, r.text)
                    break

                elif r.status_code == 401:
                    cmd().bad(token, 'Unauthorized', r.status_code, r.text)
                    break
                else:
                    cmd().bad(token, 'Other', r.status_code, r.text)
                    break


        def main():
            cmd().preare('Mass pin')
            channelid = cmd().ask('CHANNEL ID')
            thread_amt = cmd().ask('THREADS')
            tokens = tool.channel_acces(channelid)
            if cfg().online(): thread.single(tool.online, tokens)
            thread.multi(thread_amt, tool.mass_pin.pin, tokens, channelid)

    class mass_respond:  
        def respond(token, messagelink, message):
            guildid, channelid, messageid = tool.link_transform(messagelink)
            payload = {
            "content": message,
            "message_reference": {
                "guild_id": guildid,
                "channel_id": channelid,
                "message_id": messageid
            }
            }
            while True:
                ss = session()
                r = ss.post(
                    f"https://discord.com/api/v9/channels/{channelid}/messages",
                    headers=headers.get(token, payload),
                    json=payload
                )
                cmd().dbg('MASS RESPOND', r.status_code, r.text)
                if r.status_code == 200:
                    cmd().good(token, f'Responded', r.status_code)
                    continue

                elif r.status_code == 400:
                    cmd().captha(token, r.status_code)
                    break

                elif r.status_code == 429:
                    cmd().ratelimit(token, r.status_code, r.json())
                    time.sleep(float(r.json()['retry_after']))
                    continue

                elif r.status_code == 403:
                    cmd().bad(token, 'Locked', r.status_code, r.text)
                    break

                elif r.status_code == 401:
                    cmd().bad(token, 'Unauthorized', r.status_code, r.text)
                    break

                else:
                    cmd().bad(token, 'Other', r.status_code, r.text)
                    break


        def main():
            cmd().preare('Mass respond')
            messagelink = cmd().ask('MESAGE LINK')
            message = cmd().ask('MESSAGE')
            thread_amt = cmd().ask('THREADS')
            guildid, channelid, messageid = tool.link_transform(messagelink)
            tokens = tool.channel_acces(channelid)
            if cfg().online(): thread.single(tool.online, tokens)
            thread.multi(thread_amt, tool.mass_respond.respond, tokens, messagelink, message)
    
    class acc_nuker:
        def get_dms(token):
            channel_ids = []
            ss = session()
            r = ss.get(
                'https://discord.com/api/v9/users/@me/channels',
                headers=headers.get(token)
            ) 
            if r.status_code == 200:
                for dm in r.json():
                    channel_ids.append(dm['id'])

            return channel_ids

        def get_friends(token):
            user_ids = []
            ss = session()
            r = ss.get(
                'https://discord.com/api/v9/users/@me/relationships',
                headers=headers.get(token)
            ) 
            if r.status_code == 200:
                for friend in r.json():
                    user_ids.append(friend['user']['id'])

            return user_ids
        
        def get_guilds(token):
            guild_ids = []
            ss = session()
            r = ss.get(
                'https://discord.com/api/v9/users/@me/guilds',
                headers=headers.get(token)
            ) 
            if r.status_code == 200:
                for guild in r.json():
                    guild_ids.append(guild['id'])

            return guild_ids
        
        def close_dm(token, channelid):
            ss = session()
            r = ss.delete(
                f"https://discord.com/api/v9/channels/{channelid}",
                headers=headers.get(token)
            )
            cmd().dbg('CLOSE DM', r.status_code, r.text)
            if r.status_code == 200:
                cmd().good(token, f'Closed DM', r.status_code)

            elif r.status_code == 400:
                cmd().captha(token, r.status_code)

            elif r.status_code == 429:
                cmd().ratelimit(token, r.status_code, r.json())
                time.sleep(float(r.json()['retry_after']))
                tool.acc_nuker.close_dm(token, channelid)

            elif r.status_code == 403:
                cmd().bad(token, 'Locked', r.status_code, r.text)

            elif r.status_code == 401:
                cmd().bad(token, 'Unauthorized', r.status_code, r.text)

            else:
                cmd().bad(token, 'Other', r.status_code, r.text)


        def leave_server(token, guildid):
            payload = {
                "lurking": False,
            }
            ss = session()
            r = ss.delete(
                f"https://discord.com/api/v9/users/@me/guilds/{guildid}",
                json=payload,
                headers=headers.get(token, payload)
            )
            cmd().dbg('LEAVER', r.status_code, r.text)
            if r.status_code == 204:
                cmd().good(token, 'Left guild', r.status_code)

            elif r.status_code == 400:
                cmd().captha(token, r.status_code)

            elif r.status_code == 429:
                cmd().ratelimit(token, r.status_code, r.json())
                time.sleep(float(r.json()['retry_after']))
                tool.acc_nuker.leave_server(token, guildid)

            elif r.status_code == 403:
                cmd().bad(token, 'Locked', r.status_code, r.text)

            elif r.status_code == 404:
                cmd().bad(token, 'Not in guild', r.status_code, r.text)

            elif r.status_code == 401:
                cmd().bad(token, 'Unauthorized', r.status_code, r.text)

            else:   
                cmd().bad(token, 'Other', r.status_code, r.text)

        def unfriend(token, userid):
            ss = session()
            r = ss.delete(
                f"https://discord.com/api/v9/users/@me/relationships/{userid}",
                headers=headers.get(token)
            )
            cmd().dbg('UNFRIENDER', r.status_code, r.text)
            if r.status_code == 204:
                cmd().good(token, 'Unfriended', r.status_code)

            elif r.status_code == 400:
                cmd().captha(token, r.status_code)

            elif r.status_code == 429:
                cmd().ratelimit(token, r.status_code, r.json())
                time.sleep(float(r.json()['retry_after']))
                tool.acc_nuker.unfriend(token, userid)

            elif r.status_code == 403:
                cmd().bad(token, 'Locked', r.status_code, r.text)

            elif r.status_code == 404:
                cmd().bad(token, 'Not in guild', r.status_code, r.text)

            elif r.status_code == 401:
                cmd().bad(token, 'Unauthorized', r.status_code, r.text)

            else:   
                cmd().bad(token, 'Other', r.status_code, r.text)

        def change_lang(token):
            ss = session()
            payload = {
                "settings": "YhMKBAoCaGkSCwiI//////////8B"
            }
            r = ss.patch(
                f"https://discord.com/api/v9/users/@me/settings-proto/1",
                headers=headers.get(token, payload),
                json=payload
            )
            cmd().dbg('CHANGE THEME', r.status_code, r.text)
            if r.status_code == 200:
                cmd().good(token, f'Changed lang to hindi', r.status_code)

            elif r.status_code == 400:
                cmd().captha(token, r.status_code)

            elif r.status_code == 429:
                cmd().ratelimit(token, r.status_code, r.json())
                time.sleep(float(r.json()['retry_after']))
                tool.acc_nuker.change_lang(token)

            elif r.status_code == 403:
                cmd().bad(token, 'Locked', r.status_code, r.text)

            elif r.status_code == 401:
                cmd().bad(token, 'Unauthorized', r.status_code, r.text)

            else:
                cmd().bad(token, 'Other', r.status_code, r.text)

        def change_theme(token):
            ss = session()
            payload = {
                "settings" :"agYIAhABGgA="
            }
            r = ss.patch(
                f"https://discord.com/api/v9/users/@me/settings-proto/1",
                headers=headers.get(token, payload),
                json=payload
            )
            cmd().dbg('CHANGE THEME', r.status_code, r.text)
            if r.status_code == 200:
                cmd().good(token, f'Changed theme to white', r.status_code)

            elif r.status_code == 400:
                cmd().captha(token, r.status_code)

            elif r.status_code == 429:
                cmd().ratelimit(token, r.status_code, r.json())
                time.sleep(float(r.json()['retry_after']))
                tool.acc_nuker.change_theme(token)

            elif r.status_code == 403:
                cmd().bad(token, 'Locked', r.status_code, r.text)

            elif r.status_code == 401:
                cmd().bad(token, 'Unauthorized', r.status_code, r.text)

            else:
                cmd().bad(token, 'Other', r.status_code, r.text)

        def log_out(token):
            ss = session()
            r = ss.patch(
                f"https://discord.com/api/v9/auth/logout",
                headers=headers.get(token)
            )
            cmd().dbg('LOG OUT', r.status_code, r.text)
            if r.status_code == 204:
                cmd().good(token, f'Logged out', r.status_code)

            elif r.status_code == 400:
                cmd().captha(token, r.status_code)

            elif r.status_code == 429:
                cmd().ratelimit(token, r.status_code, r.json())
                time.sleep(float(r.json()['retry_after']))
                tool.acc_nuker.log_out(token)

            elif r.status_code == 403:
                cmd().bad(token, 'Locked', r.status_code, r.text)

            elif r.status_code == 401:
                cmd().bad(token, 'Unauthorized', r.status_code, r.text)

            else:
                cmd().bad(token, 'Other', r.status_code, r.text)

        def do(token, logout=False):
            friend_ids = tool.acc_nuker.get_friends(token)
            dm_ids = tool.acc_nuker.get_dms(token)
            guild_ids = tool.acc_nuker.get_guilds(token)

            tool.acc_nuker.change_lang(token)
            tool.acc_nuker.change_theme(token)

            for friend_id in friend_ids:
                tool.acc_nuker.unfriend(token, friend_id)

            for dm_id in dm_ids:
                tool.acc_nuker.close_dm(token, dm_id)

            for guild_id in guild_ids:
                tool.acc_nuker.leave_server(token, guild_id)

            if logout:
                tool.acc_nuker.log_out(token)

        def main():
            cmd().preare('Account nuker')
            cmd().options('''
01 ~> Single token
02 ~> All tokens loaded (MAY LOCK IF U USE TOO MANY TOKENS)
03 ~> Back
''')
            choice = cmd().ask('CHOICE')
            if choice == '1':
                tkn = cmd().ask('TOKEN')
                if tkn == 'main':
                    tkn = cfg().main_token()
                tokens = [tkn]
            elif choice == '2':
                tokens = get.tokens()
            elif choice == '3':
                return
            else:
                return
            
            log_out = cmd().askyn('Log out after nuke? (WILL MAKE THE TOKEN INVALID AND NOT USABLE)')
                    
            if cfg().online(): thread.single(tool.online, tokens)
            thread.single(tool.acc_nuker.do, tokens, log_out)

    class log_out:
        def log_out(token):
            ss = session()
            r = ss.patch(
                f"https://discord.com/api/v9/auth/logout",
                headers=headers.get(token)
            )
            cmd().dbg('LOG OUT', r.status_code, r.text)
            if r.status_code == 204:
                cmd().good(token, f'Logged out', r.status_code)

            elif r.status_code == 400:
                cmd().captha(token, r.status_code)

            elif r.status_code == 429:
                cmd().ratelimit(token, r.status_code, r.json())
                time.sleep(float(r.json()['retry_after']))
                tool.log_out.log_out(token)

            elif r.status_code == 403:
                cmd().bad(token, 'Locked', r.status_code, r.text)

            elif r.status_code == 401:
                cmd().bad(token, 'Unauthorized', r.status_code, r.text)

            else:
                cmd().bad(token, 'Other', r.status_code, r.text)


        def main():
            cmd().preare('Log out')
            if not cmd().askyn('THIS WILL MAKE UR TOKENS INVALID AND USABLE DO U WANT TO CONTINUE?'):
                return
            cmd().options('''
01 ~> Single token
02 ~> All tokens loaded
03 ~> Back
''')
            choice = cmd().ask('CHOICE')
            if choice == '1':
                tkn = cmd().ask('TOKEN')
                if tkn == 'main':
                    tkn = cfg().main_token()
                tokens = [tkn]
            elif choice == '2':
                tokens = get.tokens()
            elif choice == '3':
                return
            else:
                return
                    
            if cfg().online(): thread.single(tool.online, tokens)
            thread.single(tool.log_out.log_out, tokens) 
    
    class change_status:
        def change(token, mode):
            ss = session()
            payload = {
                "settings": mode
            }
            r = ss.patch(
                "https://discord.com/api/v9/users/@me/settings-proto/1",
                headers=headers.get(token, payload),
                json=payload
            )
            cmd().dbg('STATUS CHANGER', r.status_code, r.text)
            if r.status_code == 200:
                cmd().good(token, 'Changed status', r.status_code)

            elif r.status_code == 400:
                cmd().captha(token, r.status_code)

            elif r.status_code == 429:
                cmd().ratelimit(token, r.status_code, r.json())
                time.sleep(float(r.json()['retry_after']))
                tool.change_status.change(token, mode)

            elif r.status_code == 403:
                cmd().bad(token, 'Locked', r.status_code, r.text)

            elif r.status_code == 401:
                cmd().bad(token, 'Unauthorized', r.status_code, r.text)

            else:   
                cmd().bad(token, 'Other', r.status_code, r.text)

        def main():
            cmd().preare('Change status')
            cmd().options('''
01 ~> Online
02 ~> AFK (idle)
03 ~> DND
04 ~> Offline
''')
            choice = cmd().ask('CHOICE') 
            if choice == '1':
                mode = "WjEKCAoGb25saW5lEiEKH/Cfm5EgZGlzY29yZC5nZy9odERGTjU4OXhhIPCfm5EaAggB"
            elif choice == '2':
                mode = "Wi8KBgoEaWRsZRIhCh/wn5uRIGRpc2NvcmQuZ2cvaHRERk41ODl4YSDwn5uRGgIIAQ=="
            elif choice == '3':
                mode = "Wi4KBQoDZG5kEiEKH/Cfm5EgZGlzY29yZC5nZy9odERGTjU4OXhhIPCfm5EaAggB"
            elif choice == '4':
                mode = "WjQKCwoJaW52aXNpYmxlEiEKH/Cfm5EgZGlzY29yZC5nZy9odERGTjU4OXhhIPCfm5EaAggB"
            else:
                mode = "WjEKCAoGb25saW5lEiEKH/Cfm5EgZGlzY29yZC5nZy9odERGTjU4OXhhIPCfm5EaAggB"
            if cfg().online(): thread.single(tool.online, get.tokens())
            thread.single(tool.change_status.change, get.tokens(), mode)


    class invite_maker:
        def make_invite(token, channelid):
            while True:
                age = random.randint(1000, 604800)
                uses = random.randint(0, 100)
                temp = random.choice(['True', 'False'])
                ss = session()
                payload = {
                    "max_age": age,
                    "max_uses": uses,
                    "target_type": None,
                    "temporary": temp,
                }
                r = ss.post(
                    f"https://discord.com/api/v9/channels/{channelid}/invites",
                    headers=headers.get(token),
                    json=payload
                )
                cmd().dbg('INVITE MAKER', r.status_code, r.text)
                if r.status_code == 200:
                    cmd().good(token, f'Made invite ({r.json()["code"]})', r.status_code)
                    continue

                elif r.status_code == 400:
                    cmd().captha(token, r.status_code)
                    break

                elif r.status_code == 429:
                    cmd().ratelimit(token, r.status_code, r.json())
                    time.sleep(float(r.json()['retry_after']))
                    tool.invite_maker.make_invite(token, channelid)
                    continue

                elif r.status_code == 403:
                    cmd().bad(token, 'Locked', r.status_code, r.text)
                    break

                elif r.status_code == 401:
                    cmd().bad(token, 'Unauthorized', r.status_code, r.text)
                    break

                else:
                    cmd().bad(token, 'Other', r.status_code, r.text)
                    break


        def main():
            cmd().preare('Invite maker')
            channelid = cmd().ask('CHANNEL ID')
            tokens = tool.channel_acces(channelid)
            if cfg().online(): thread.single(tool.online, tokens)
            thread.single(tool.invite_maker.make_invite, tokens, channelid) 

    class mass_unban:
        def get_bans(token, guildid):
            ids = []
            ss = session()
            r = ss.get(
                f"https://discord.com/api/v9/guilds/{guildid}/bans",
                headers=headers.get(token)
            )
            cmd().dbg('GET BANS', r.status_code, r.text)
            if r.status_code == 200:
                for user in r.json():
                    ids.append(user['user']['id'])

            elif r.status_code == 400:
                cmd().captha(token, r.status_code)

            elif r.status_code == 403:
                if 'code' in r.json() and r.json()['code'] == 50013:
                    cmd().bad(token, 'No perms', r.status_code, r.text)
                else:
                    cmd().bad(token, 'Locked', r.status_code, r.text)

            elif r.status_code == 401:
                cmd().bad(token, 'Unauthorized', r.status_code, r.text)

            else:
                cmd().bad(token, 'Other', r.status_code, r.text)             
                    
            return ids

        def unban(token, guildid, userid):
            ss = session()
            r = ss.delete(
                f"https://discord.com/api/v9/guilds/{guildid}/bans/{userid}",
                headers=headers.get(token)
            )
            cmd().dbg('MASS UNBAN', r.status_code, r.text)
            if r.status_code == 204:
                cmd().good(token, f'Unbanned {userid}', r.status_code)

            elif r.status_code == 400:
                cmd().captha(token, r.status_code)

            elif r.status_code == 429:
                cmd().ratelimit(token, r.status_code, r.json())
                time.sleep(float(r.json()['retry_after']))
                tool.mass_unban.unban(token, guildid, userid)

            elif r.status_code == 403:
                if 'code' in r.json() and r.json()['code'] == 50013:
                    cmd().bad(token, 'No perms', r.status_code, r.text)
                else:
                    cmd().bad(token, 'Locked', r.status_code, r.text)

            elif r.status_code == 401:
                cmd().bad(token, 'Unauthorized', r.status_code, r.text)

            else:
                cmd().bad(token, 'Other', r.status_code, r.text)

        def do(token, userids, guildid):
            tokens = [token]
            cmd().dbg('USERIDS:', userids)
            for userid in userids:
                cmd().dbg('CHOSEN TO UNBAN:', userid)
                thread.single(tool.mass_unban.unban, tokens, guildid, userid)

        def main():
            cmd().preare('Mass unban')
            token = cmd().ask('TOKEN (ACCOUNT TOKEN NOT BOT TOKEN)')
            if token == 'main':
                token = cfg().main_token()
            tokens = [token]
            guildid = cmd().ask('GUILD ID')
            userids = tool.mass_unban.get_bans(token, guildid)

            if cfg().online(): thread.single(tool.online, tokens)
            thread.single(tool.mass_unban.do, tokens, userids, guildid) 


    class server_massreport:
        def report(token, guildid, userid):
            ss = session()
            r = ss.post(
                f"https://discord.com/api/v9/reporting/guild",
                headers=headers.get(token)
            )
            cmd().dbg('MASS UNBAN', r.status_code, r.text)
            if r.status_code == 204:
                cmd().good(token, f'Unbanned {userid}', r.status_code)

            elif r.status_code == 400:
                cmd().captha(token, r.status_code)

            elif r.status_code == 429:
                cmd().ratelimit(token, r.status_code, r.json())
                time.sleep(float(r.json()['retry_after']))
                tool.mass_unban.unban(token, guildid, userid)

            elif r.status_code == 403:
                if 'code' in r.json() and r.json()['code'] == 50013:
                    cmd().bad(token, 'No perms', r.status_code, r.text)
                else:
                    cmd().bad(token, 'Locked', r.status_code, r.text)

            elif r.status_code == 401:
                cmd().bad(token, 'Unauthorized', r.status_code, r.text)

            else:
                cmd().bad(token, 'Other', r.status_code, r.text)
                
        def main():
            cmd().preare('Server massreport')
            cmd().log('SERVER MASS REPORT', 'Sorry i tried to make it analyzing it from mobile but i could not due to os issues i will make this feature when its possible to report servers on desktop (i have the api endpoint but every report option has a diff payload)')
            return
        
    class wb_spammer:
        def send(wb, message, name, tts):
            while True:
                payload = {
                    "content": message,
                    "username": name,
                    "tts": tts
                }
                ss = session()
                r = ss.post(
                    wb,
                    json=payload,
                )
                cmd().dbg('WB SEND', r.status_code, r.text)
                if r.status_code == 204:
                    cmd().good(wb, 'Sent', r.status_code)
                    continue

                elif r.status_code == 429:
                    cmd().ratelimit(wb, r.status_code, r.json())
                    time.sleep(float(r.json()['retry_after']))
                    tool.wb_spammer.send(wb, message, name)
                    continue

                else:   
                    cmd().bad(wb, 'Other', r.status_code, r.text) 
                    break


        def main():
            cmd().preare('Webhook spammer')
            wb = cmd().ask('WEBHOOK')

            while not tool.check_wb(wb):
                cmd().log('WB SPAMMER', 'Invalid webhook')
                wb = cmd().ask('WEBHOOK')
            cmd().log('WB SPAMMER', 'Valid webhook')

            msg = cmd().ask('MESSAGE')
            customname = cmd().askyn('CUSTOM NAME')
            if customname:
                name = cmd().ask('NAME')
            else:
                name = None
            tts = cmd().askyn('USE TTS')
            thrd_amt = cmd().ask('THREADS')
            
            threads = []
            for _ in range(int(thrd_amt)):
                t = threading.Thread(target=tool.wb_spammer.send, args=(wb, msg, name, tts))
                t.start()
                threads.append(t)
            for thread in threads:
                thread.join()  


    class wb_editor:
        def username(wb, name):
            payload = {
                "name": name,
            }
            ss = session()
            r = ss.patch(
                wb,
                json=payload,
            )
            cmd().dbg('WB EDIT USERNAME', r.status_code, r.text)
            if r.status_code == 200:
                cmd().good(wb, 'Updated username', r.status_code)


            elif r.status_code == 429:
                cmd().ratelimit(wb, r.status_code, r.json())
                time.sleep(float(r.json()['retry_after']))
                tool.wb_editor.username(wb, name)

            else:   
                cmd().bad(wb, 'Other', r.status_code, r.text) 

        def avatar(wb, filepath):
            with open(filepath, "rb") as f:
                image = base64.b64encode(f.read()).decode("utf-8")
            payload = {
                "avatar": f"data:image/png;base64,{image}"
            }
            r = requests.patch(
                wb,
                json=payload,
                headers = {"Content-Type": "application/json"}
            )

            cmd().dbg('WB EDIT AVATAR', r.status_code, r.text)

            if r.status_code == 200:
                cmd().good(wb, 'Updated avatar', r.status_code)

            elif r.status_code == 429:
                cmd().ratelimit(wb, r.status_code, r.json())
                time.sleep(float(r.json()['retry_after']))
                tool.wb_editor.avatar(wb, filepath)

            else:
                cmd().bad(wb, 'Other', r.status_code, r.text)


        def main():
            cmd().preare('Webhook editor')
            wb = cmd().ask('WEBHOOK')

            while not tool.check_wb(wb):
                cmd().log('WB EDITOR', 'Invalid webhook')
                wb = cmd().ask('WEBHOOK')
            cmd().log('WB EDITOR', 'Valid webhook')

            cmd().options("""
01 ~> Username
02 ~> Avatar
03 ~> Back
""")
            choice = cmd().ask('CHOICE')
            if choice == '1':
                name = cmd().ask('USERNAME')
                tool.wb_editor.username(wb, name)

            elif choice == '2':
                root = tk.Tk()
                root.withdraw()
                filepath = filedialog.askopenfilename()
                tool.wb_editor.avatar(wb, filepath)

            else:
                return
            
    class wb_deleater:
        def delete(wb):
            r = requests.delete(
                wb,
            )
            cmd().dbg('WB DELETE', r.status_code, r.text)
            if r.status_code == 204:
                cmd().good(wb, 'Deleted', r.status_code)

            elif r.status_code == 429:
                cmd().ratelimit(wb, r.status_code, r.json())
                time.sleep(float(r.json()['retry_after']))
                tool.wb_deleater.delete(wb)

            else:
                cmd().bad(wb, 'Other', r.status_code, r.text)


        def main():
            cmd().preare('Webhook deleter')
            wb = cmd().ask('WEBHOOK')
            while not tool.check_wb(wb):
                cmd().log('WB DELETER', 'Invalid webhook')
                wb = cmd().ask('WEBHOOK')
            cmd().log('WB DELETER', 'Valid webhook')
            tool.wb_deleater.delete(wb)

# region OPTIONS



while __name__ == '__main__':
    cmd().cls()
    cmd().title(main_name)
    cmd().menu()

    if cfg().proxies():
        cmd().inplog('CONFIG', 'Proxies are supported in paid only! Turn them off inside of the config')

    c = input(f'{cmd().r}~> {cmd().b}')
    c = re.sub(r'[^0-9<>]+', '', c)
    c = re.sub(r'(>+)', '>>', c)
    c = re.sub(r'(<+)', '<<', c)
    options = {
        '1': tool.guild_manager.main,
        '2': tool.checker.main,
        '3': tool.spammer.main,
        '4': tool.bypasses.main,
        '5': tool.paid,
        '6': tool.combo_to_token.main,
        '7': tool.onliner.main,
        '8': tool.humanizer.main,
        '9': tool.bio_changer.main,
        '10': tool.paid,
        '11': tool.display_changer.main,
        '12': tool.avatar_changer.main,
        '13': tool.paid,
        '14': tool.paid,
        '15': tool.reaction_bomber.main,
        '16': tool.paid,
        '17': tool.paid,
        '18': tool.mass_report.main,
        '19': tool.paid,
        '20': tool.thread_spammer.main,
        '21': tool.paid,
        '22': tool.friender.main,
        '23': tool.vc_joiner.main,
        '24': tool.vc_spammer.main,
        '25': tool.mass_pin.main,
        '26': tool.mass_respond.main,
        '27': tool.paid,
    }

    if c in options:
        cmd().cls(); cmd().banner()
        options[c]()
        cmd().inplog('CORE', 'Finished the task! Enter to continue')
        cmd().cls()
    elif c == '>>':
        cmd().cls()
        cmd().menu2()
        c = input(f'{cmd().r}~> {cmd().b}')
        c = re.sub(r'[^0-9<>]+', '', c)
        c = re.sub(r'(>+)', '>>', c)
        c = re.sub(r'(<+)', '<<', c)
        options = {
            '28': tool.paid,
            '29': tool.paid,
            '30': tool.paid,
            '31': tool.paid,
            '32': tool.paid,
            '35': tool.acc_nuker.main,
            '36': tool.log_out.main,
            '37': tool.paid,
            '38': tool.paid,
            '39': tool.change_status.main,
            '42': tool.invite_maker.main,
            '43': tool.paid,
            '44': tool.paid,
            '45': tool.mass_unban.main,
            '46': tool.server_massreport.main,
            '47': tool.paid,
            '49': tool.wb_spammer.main,
            '50': tool.wb_editor.main,
            '51': tool.wb_deleater.main
        }
        if c in options:
            cmd().cls(); cmd().banner()
            options[c]()
            cmd().inplog('CORE', 'Finished the task! Enter to continue')
            cmd().cls()
        elif c == '<<':
            pass
        else: 
            cmd().log('CORE', 'Invalid option')
            time.sleep(2)
            cmd().cls()
    else: 
        cmd().log('CORE', 'Invalid option')
        time.sleep(2)
        cmd().cls()
        
# bro dont skid
