import os, sys, time
print('Preping... please wait')
if sys.version_info.minor < 10:
    print(f'Ur current version of python ({sys.version_info.major}.{sys.version_info.minor}) is not supported, 3.11.7 is recomended')
    time.sleep(5)
    sys.exit()

try: 
    from colorama import Fore, Back, init; init()
    import requests
    import uuid
    import threading
    import tls_client
    import random
    import websocket
    import json
    import string
    import re
    from datetime import datetime
    import threading
except ModuleNotFoundError:
    print('Some libs ware not found, downloading them now')
    os.system('pip uninstall -y websockets'); os.system('pip uninstall -y websocket')
    for lib in ['websocket-client', 'colorama', 'requests', 'tls-client', 'datetime']:
        print(f'Installing {lib}')
        os.system(f'pip install -q {lib}')
    print('All done! please rerun')
    time.sleep(2.5)
    sys.exit()
except Exception as e:
    input(f'Error while importing {e}')
    time.sleep(2.5)
    sys.exit()

main_name = 'Vanadium V1 - FREE'


class cmd:
    res = Fore.RESET
    r = Fore.RED
    b = Fore.LIGHTBLACK_EX
    m = Fore.MAGENTA
    c = Fore.CYAN
    p = Fore.LIGHTMAGENTA_EX
    g = Fore.GREEN
    y = Fore.YELLOW

    def banner():
        size = os.get_terminal_size().columns
        size = size - 1
        banner = f'''{cmd.r}  
{f'U are currently using the free version, buy full/premium on dsc.gg/vanadium !'.center(size)}
{f'██╗   ██╗ █████╗ ███╗   ██╗ █████╗ ██████╗ ██╗██╗   ██╗███╗   ███╗'.center(size)}
{f'██║   ██║██╔══██╗████╗  ██║██╔══██╗██╔══██╗██║██║   ██║████╗ ████║'.center(size)}
{f'██║   ██║███████║██╔██╗ ██║███████║██║  ██║██║██║   ██║██╔████╔██║'.center(size)} 
{f'╚██╗ ██╔╝██╔══██║██║╚██╗██║██╔══██║██║  ██║██║██║   ██║██║╚██╔╝██║'.center(size)}
{f' ╚████╔╝ ██║  ██║██║ ╚████║██║  ██║██████╔╝██║╚██████╔╝██║ ╚═╝ ██║'.center(size)}
{f'  ╚═══╝  ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═════╝ ╚═╝ ╚═════╝ ╚═╝     ╚═╝'.center(size)}
'''
        print(banner)

    def menu():
        size = os.get_terminal_size().columns
        size = size - 1
        with open(f"data\\tokens.txt", "r") as f:
            token_amt = sum(1 for _ in f)
        with open(f"data\\combo_tokens.txt", "r") as f:
            combo_amt = sum(1 for _ in f)
        with open(f"data\\proxies.txt", "r") as f:
            prx_amt = sum(1 for _ in f)

        menu = f'''{cmd.r}  
{f'U are currently using the free version, buy full/premium on dsc.gg/vanadium !'.center(size)}
{f'██╗   ██╗ █████╗ ███╗   ██╗ █████╗ ██████╗ ██╗██╗   ██╗███╗   ███╗'.center(size)}
{f'██║   ██║██╔══██╗████╗  ██║██╔══██╗██╔══██╗██║██║   ██║████╗ ████║'.center(size)}
{f'██║   ██║███████║██╔██╗ ██║███████║██║  ██║██║██║   ██║██╔████╔██║'.center(size)} 
{f'╚██╗ ██╔╝██╔══██║██║╚██╗██║██╔══██║██║  ██║██║██║   ██║██║╚██╔╝██║'.center(size)}
{f' ╚████╔╝ ██║  ██║██║ ╚████║██║  ██║██████╔╝██║╚██████╔╝██║ ╚═╝ ██║'.center(size)}
{f'  ╚═══╝  ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═════╝ ╚═╝ ╚═════╝ ╚═╝     ╚═╝'.center(size)}
{f'(*) - Combo tokens needed      (#) - Beta feature      (!) - Can be token harming'.center(size)}
{f'Tokens loaded - [ {token_amt} ]      Combo tokens loaded - [ {combo_amt} ]      Proxies loaded - [ {prx_amt} ]'.center(size)}
{f''.center(size)}
{f'  [ 01 ] - Guild managment     [ 08 ] - Token humanizer        [ 15 ] - Reaction bomber     [ 22 ] - Friender (!)     '.center(size)}
{f'  [ 02 ] - Checker (#)         [ 09 ] - Bio changer            [ 16 ] - Spam call           [ 23 ] - VC joiner        '.center(size)} 
{f'  [ 03 ] - Spammer             [ 10 ] - Username changer (*)   [ 17 ] - Mass DM (!)         [ 24 ] - VC spammer       '.center(size)}
{f'  [ 04 ] - Bypasses            [ 11 ] - Display changer        [ 18 ] - Mass report         [ 25 ] - Mass pin         '.center(size)}
{f'  [ 05 ] - Fast raid           [ 12 ] - Avatar changer         [ 19 ] - Button spammer      [ 26 ] - Mass respond     '.center(size)}
{f'  [ 06 ] - Combo to token      [ 13 ] - Server nick changer    [ 20 ] - Thread spammer      [ 27 ] - Join sticker spam'.center(size)}
{f'  [ 07 ] - Onliner             [ 14 ] - Passowrd changer (*)   [ 21 ] - Forum spammer       [ >> ] - Next page        '.center(size)}
'''
        
        for x in ['-', 'None', '*', '#', '!']:
            menu = menu.replace(x, f'{cmd.b}{x}{cmd.r}')

        print(menu)
    
    def menu2():
        size = os.get_terminal_size().columns
        size = size - 1
        with open(f"data\\tokens.txt", "r") as f:
            token_amt = sum(1 for _ in f)
        with open(f"data\\combo_tokens.txt", "r") as f:
            combo_amt = sum(1 for _ in f)
        with open(f"data\\proxies.txt", "r") as f:
            prx_amt = sum(1 for _ in f)

        menu2 = f'''{cmd.r} 
{f'U are currently using the free version, buy full/premium on dsc.gg/vanadium !'.center(size)} 
{f'██╗   ██╗ █████╗ ███╗   ██╗ █████╗ ██████╗ ██╗██╗   ██╗███╗   ███╗'.center(size)}
{f'██║   ██║██╔══██╗████╗  ██║██╔══██╗██╔══██╗██║██║   ██║████╗ ████║'.center(size)}
{f'██║   ██║███████║██╔██╗ ██║███████║██║  ██║██║██║   ██║██╔████╔██║'.center(size)} 
{f'╚██╗ ██╔╝██╔══██║██║╚██╗██║██╔══██║██║  ██║██║██║   ██║██║╚██╔╝██║'.center(size)}
{f' ╚████╔╝ ██║  ██║██║ ╚████║██║  ██║██████╔╝██║╚██████╔╝██║ ╚═╝ ██║'.center(size)}
{f'  ╚═══╝  ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═════╝ ╚═╝ ╚═════╝ ╚═╝     ╚═╝'.center(size)}
{f'(*) - Combo tokens needed      (#) - Beta feature      (!) - Can be token harming'.center(size)}
{f'Tokens loaded - [ {token_amt} ]      Combo tokens loaded - [ {combo_amt} ]      Proxies loaded - [ {prx_amt} ]'.center(size)}
{f''.center(size)}
{f'  [ 28 ] - Poll spammer (#)    [ 35 ] - Account nuker          [ 42 ] - Invite maker         [ 49 ] - Webhook spammer '.center(size)}
{f'  [ 29 ] - Poll voter (#)      [ 36 ] - Log out                [ 43 ] - Server nuker         [ 50 ] - Webhook editor  '.center(size)} 
{f'  [ 30 ] - Everywheare messager[ 37 ] - Log in                 [ 44 ] - Member fetcher       [ 51 ] - Webhook deleater'.center(size)}
{f'  [ 31 ] - Message listener    [ 38 ] - None                   [ 45 ] - None                 [ 52 ] - None            '.center(size)}
{f'  [ 32 ] - None                [ 39 ] - None                   [ 46 ] - None                 [ 53 ] - None            '.center(size)}
{f'  [ 33 ] - None                [ 40 ] - None                   [ 47 ] - None                 [ 54 ] - None            '.center(size)}
{f'  [ 34 ] - None                [ 41 ] - None                   [ 48 ] - None                 [ << ] - Previous page   '.center(size)}
'''
        
        for x in ['-', 'None', '*', '#', '!']:
            menu2 = menu2.replace(x, f'{cmd.b}{x}{cmd.r}')

        print(menu2)

    def options(options):
        for x in ['~>']:
            options = options.replace(x, f'{cmd.r}{x}{cmd.b}')
        print(f'{cmd.b}{options}')

    def not_yet():
        cmd.log('CORE', 'This feautre is not made yet')
        return
    
    def paid():
        cmd.log('CORE', 'This is a paid only feature!')
        return

    def paidc(x):
        cmd.log('CORE', f'{x} is a paid only feature!')
        return

    def date():
        return datetime.now().strftime('%H:%M:%S')

    def log(main, contents):
        print(f'{cmd.r}[{cmd.b}{main}{cmd.r}] {cmd.r}~>{cmd.b} {contents}')

    def inplog(main, contents):
        input(f'{cmd.r}[{cmd.b}{main}{cmd.r}] {cmd.r}~>{cmd.b} {contents}')

    def ask(main):
        return input(f'{cmd.r}[{cmd.b}{main}{cmd.r}] {cmd.r}~>{cmd.b} ')
    
    def askyn(main):
        inp = input(f'{cmd.r}[{cmd.b}{main}{cmd.r}]{cmd.b} (y/n) {cmd.r}~>{cmd.b} ')
        if inp == 'y':
            return True
        else:
            return False
        
    def good(token, main, status, response=None):
        if response:
            response = f'({response})'
            try:
                response = json.loads(response)['message']
            except:
                response = response

        if not response:
            response = ''

        print(f'{cmd.b}[{cmd.date()}]{cmd.r} {cmd.g}[{main} ~> {status}] {cmd.b}~>{cmd.r} {token[:30]}{cmd.r}***{cmd.b} {cmd.b} {response}')

    def bad(token, main, status, response):
        if config.moreinfo():
            if response:
                response = f'({response})'
                try:
                    response = json.loads(response)['message']
                except:
                    response = response

        print(f'{cmd.b}[{cmd.date()}]{cmd.r} {cmd.r}[{main} ~> {status}] {cmd.b}~>{cmd.r} {token[:30]}{cmd.r}***{cmd.b} {cmd.b} {response}')

    def captha(token, status):
        print(f'{cmd.b}[{cmd.date()}]{cmd.c} {cmd.c}[HCaptcha ~> {status}] {cmd.b}~>{cmd.r} {token[:30]}{cmd.r}***{cmd.b} {cmd.b} | This would propably be prevented if u used paid!')

    def ratelimit(token, status, jresponse=None):
        if jresponse:
            ratelimit = float(jresponse['retry_after'])
        else:
            ratelimit = 'N/A'

        print(f'{cmd.b}[{cmd.date()}]{cmd.r} {cmd.y}[Ratelimited ~> {status}] {cmd.b}~>{cmd.r} {token[:30]}{cmd.r}***{cmd.b} {cmd.b} {ratelimit}s')

    def dbg(var='', var1='', var2='', var3=''):
        if config.debug():
            print(f'{cmd.y}!!!DEBUG!!! ~> {var}\n{var1}\n{var2}\n{var3}')

    def title(content):
        os.system(f'title {content}')

    def cls():
        os.system('cls')

    def preare(module):
        cmd.cls()
        cmd.banner()
        cmd.title(f'{main_name} - {module}')

cmd.cls()
cmd.title(main_name)


class files:
    def folders():
        folders = [
            'data', 
            'data\\scrapes',
            'data\\scrapes\\guilds',
        ]
        for folder in folders:
            try:
                if not os.path.exists(folder):
                    os.mkdir(folder)
            except Exception as e:
                print(e)

    def cfg():
        if not os.path.exists('config.jsonc'):
            with open('config.jsonc', 'w') as f:
                f.write("""
{
    "DEBUG": false, // Made just for me dont use if u dont run into problems
    "Proxies": false,  // Most free proxies wont work on discord, remember!
    "Paid solver": false, // Paid solver service (capsolver)
    "Paid solver api key": "Ur-capsolver-api-key", // Capsolver api key
    "Onliner on func": false, // Token onliner when a module is ran
    "Auto free captcha bypass": false, // Free captcha bypass wont work always; if the paid solver is available, it will be preferred
    "RPC": true, // Will auto online all loaded tokens with a vanadium RPC
    "Preffer combos": false, // Will prefer to use the combo tokens instead of just tokens (input combos to data/combo_tokens.txt)
    "More info mode": false // If the code is diffrent than OK (succes) the log will show the full respone text
}
    """)

    def other():
        files = [
            'tokens.txt', 
            'proxies.txt',
            'combo_tokens.txt',
        ]
        for file in files:
            try:
                if not os.path.exists(file):
                    with open(f'data\\{file}', 'a') as f:
                        f.close()
            except Exception as e:
                cmd.log('FILES', e)
                time.sleep(5)
                exit()


    def run():
        files.cfg()
        files.folders()
        files.other()

cmd.log('FILES', 'Doing file stuff...')
files.run()

class cfg:
    try:
        def __init__(self):
            with open('config.jsonc', 'r') as f:
                try:
                    config_contents = ''
                    for line in f:
                        config_contents += line.split('//', 1)[0]
                    config_contents = re.sub(r'/\*[\s\S]*?\*/', '', config_contents)
                    self.cfg = json.loads(config_contents)
                except json.JSONDecodeError as e:
                    cmd.log('CONFIG', e)
                    self.cfg = {}

        def debug(self):
            return self.cfg.get('DEBUG')  

        def proxies(self):
            return self.cfg.get('Proxies')

        def paid_solver(self):
            return self.cfg.get('Paid solver')

        def solver_api_key(self):
            return self.cfg.get('Paid solver api key')

        def online(self):
            return self.cfg.get('Onliner on func')

        def rpc(self):
            return self.cfg.get('RPC')

        def captcha_bypass(self):
            return self.cfg.get('Auto free captcha bypass')
        
        def prefer_combo_tokens(self):
            return self.cfg.get('Preffer combos')   

        def moreinfo(self):
            return self.cfg.get('More info mode')  
    except:
        cmd.log('CONFIG', 'Reading config failed, rerun')
        time.sleep(2.5)
        sys.exit()    

cmd.log('CONFIG', 'Reading config...')
config = cfg()

class thread:
    def multi(thread_amt, func, tokens, *args):
        threads = []
        for _ in range(int(thread_amt)):
            for token in tokens:
                t = threading.Thread(target=func, args=(token,) + args)
                t.start()
                threads.append(t)
        for thread_ in threads:
            thread_.join()

    def single(func, tokens, *args):
        threads = []
        for token in tokens:
            t = threading.Thread(target=func, args=(token,) + args)
            t.start()
            threads.append(t)
        for thread_ in threads:
            thread_.join()

    def multi_c(thread_amt, func, *args):
        combos = get.combos()
        threads = []
        for _ in range(int(thread_amt)):
            for combo in combos:
                t = threading.Thread(target=func, args=combo + args)
                t.start()
                threads.append(t)
        for thread_ in threads:
            thread_.join()

    def single_c(func, *args):
        combos = get.combos()
        threads = []
        for combo in combos:
            t = threading.Thread(target=func, args=combo + args[1:])
            t.start()
            threads.append(t)
        for thread_ in threads:
            thread_.join()


class get:
    def cookies():
        r = requests.get(
            "https://discord.com/"
        )
        if r.status_code == 200:
            cookies = '; '.join([f"{cookie.name}={cookie.value}" for cookie in r.cookies]) + '; locale=en-US'
        else:
            cmd.dbg(r.status_code, r.text)
            cookies = get.fake_cookies()
        return cookies
    
    def fake_cookies():
        def func(length):
            return ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        
        return f'__dcfduid={func(32)}; __sdcfduid={func(32)}; __cfruid={func(40)}; _cfuvid={func(48)}; locale=en-US'
    
    def tokens():
        if not config.prefer_combo_tokens():
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
                        cmd.log('TOKEN READER', 'Invalid combo format! it should be email:pass:token')
                        time.sleep(5)
                        exit()
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
                    cmd.log('TOKEN READER', 'Invalid combo format! it should be email:pass:token')
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
                    cmd.log('TOKEN READER', 'Invalid combo format! it should be email:pass:token')
                    time.sleep(5)
                    exit()
        return combos  
        
    def proxies():
        with open(f'data\\proxies.txt', 'r') as f:
            return f.read().splitlines()
    
    def nonce():
        return str((int(time.mktime(datetime.now().timetuple())) * 1000 - 1420070400000) * 4194304)
    
    def string(length):
        random_string = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))
        return random_string

# still working on making them bypass well :(
chrome_version = random.randint(115, 120)
class HeaderFactoryReal:
    def __init__(self):
        self.ua = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9041 Chrome/120.0.6099.291 Electron/28.2.10 Safari/537.36'
        self.xsup = 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDQxIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDUiLCJvc19hcmNoIjoieDY0IiwiYXBwX2FyY2giOiJpYTMyIiwic3lzdGVtX2xvY2FsZSI6ImVuLUdCIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV09XNjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIGRpc2NvcmQvMS4wLjkwNDEgQ2hyb21lLzEyMC4wLjYwOTkuMjkxIEVsZWN0cm9uLzI4LjIuMTAgU2FmYXJpLzUzNy4zNiIsImJyb3dzZXJfdmVyc2lvbiI6IjI4LjIuMTAiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjoyODQxODcsIm5hdGl2ZV9idWlsZF9udW1iZXIiOjQ2MzU1LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ=='
        cmd.log('HEADERS', 'Getting cookies...')
        self.cookies = get.cookies()

    def calculate(data):
        data = json.dumps(data, separators=(',', ':'))
        return len(data.encode('utf-8'))

    def get(self, token=None, data=None):
        headers = {
            "Accept": "*/*",
            "Accept-language": "en-GB,pl;q=0.9",
            "Authorization": token,
            #"Content-Length": HeaderFactoryReal.calculate(data),
            "Cookie": self.cookies,
            "Origin": "https://discord.com",
            "Sec-Ch-Ua": f'"Not_A Brand";v="8", "Chromium";v="{chrome_version}"',
            "Sec-Ch-Ua-Platform": '"Windows',
            "User-agent": self.ua,
            "X-Discord-Locale": "en-US",
            "X-Discord-Timezone": "Europe/Warsaw",
            "X-Super-Properties": self.xsup
        }
        if token is None:
            headers.pop("Authorization", None)
        if data is None:
            headers.pop("Content-Length", None)

        cmd.dbg(headers)
        return headers

headers = HeaderFactoryReal()

bl_guilds = ['1218958297558679702', '1157405821450338334']
bl_channels = []
bl_ids = []

def get_user_id(token):
    global bl_ids
    cmd.log('BLACKLIST', f'Blacklisting id for {cmd.b}{token[:30]}{cmd.r}***')
    r = requests.get(
        f"https://discord.com/api/v9/users/@me",
        headers=headers.get(token),
    )
    if r.status_code == 200:
        bl_ids.append(r.json()['id'])
    else:
        return

thread.single(get_user_id, get.tokens())


def session():
    session = tls_client.Session(client_identifier=f'chrome_{chrome_version}', random_tls_extension_order=True)
    return session

class tool: 
    def link_transform(url):
        try:
            url = url.replace('https://discord.com/channels/', '')
        except:
            url = url.replace('https://canary.discord.com/channels/', '')
        parts = url.split('/')
        guildid = parts[0]
        channelid = parts[1]
        messageid = parts[2]
        return guildid, channelid, messageid


    def get_user_id(token):
        ss = session()
        r = ss.get(
            f"https://discord.com/api/v9/users/@me",
            headers=headers.get(token),
        )
        cmd.dbg('CHECKER', r.status_code, r.text)
        if r.status_code == 200:
            return r.json()['id']
        else:
            return None

    def inside_guild(guildid, specific_token=None):
        if not specific_token:
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
            cmd.preare('Guild manager')
            cmd.options('''
01 ~> Joiner
02 ~> Leaver
03 ~> Guild checker
04 ~> Mass leave 
05 ~> Back
''')
            c = cmd.ask('CHOICE')
            if c == '1':
                tool.guild_manager.joiner.main()
            elif c == '2':
                tool.guild_manager.leaver.main()
            elif c == '3':
                tool.guild_manager.guild_checker.main()
            elif c == '4':
                tool.guild_manager.mass_leave.main()
            elif c == '5':
                return
            else:
                cmd.log('GUILD MANAGER', 'Invalid option')



        class joiner:
            def join(token, invite_regex):
                guildid, guildname = tool.guild_manager.joiner.get_name_and_id(invite_regex)
                if guildid in bl_guilds:
                    cmd.log('JOINER', 'Nah really? Trying to join the main server?? Thats crazyyy')
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
                cmd.dbg('JOINER', r.status_code, r.text)
                if r.status_code == 200:
                    cmd.good(token, f'Joined {guildname}', r.status_code)
                elif r.status_code == 400:
                    cmd.captha(token, r.status_code)
                elif r.status_code == 429:
                    cmd.ratelimit(token, r.status_code, r.json())
                    time.sleep(float(r.json()['retry_after']))
                    tool.guild_manager.joiner.join(token, invite_regex)
                elif r.status_code == 403:
                    cmd.bad(token, 'Locked', r.status_code, r.text)
                else:   
                    cmd.bad(token, 'Other', r.status_code, r.text)

            def get_name_and_id(invite_regex):
                ss = session()
                r = ss.get(
                    f"https://discord.com/api/v9/invites/{invite_regex}?inputValue={invite_regex}&with_counts=true&with_expiration=true",
                )
                cmd.dbg('NAME + ID GETTER', r.status_code, r.text)
                if not r.status_code == 404: 
                    data = r.json()['guild']
                    return r.json()['guild_id'], data['name']
                else:
                    return None, None  

            def main():
                cmd.preare('Guild manager/Joiner')
                invite = cmd.ask('INVITE')
                match = re.search(r'(?:discord.gg/|discordapp.com/invite/)([a-zA-Z0-9]+)', invite)
                if match: invite =  match.group(1)
                invite_regex = invite
                cmd.dbg('JOINER', invite_regex)
                if config.online(): thread.single(tool.online, get.tokens())
                else:
                    thread.single(tool.guild_manager.joiner.join, get.tokens(), invite_regex)

        class leaver:
            def leave(token, guildid):
                payload = {
                    "lurking": False,
                }
                ss = session()
                r = ss.get(
                    f"https://discord.com/api/v9/users/@me/guilds/{guildid}",
                    json=payload,
                    headers=headers.get(token, payload)
                )
                cmd.dbg('LEAVER', r.status_code, r.text)
                if r.status_code == 204:
                    cmd.good(token, 'Left', r.status_code)
                elif r.status_code == 400:
                    cmd.captha(token, r.status_code)
                elif r.status_code == 429:
                    cmd.ratelimit(token, r.status_code, r.json())
                    time.sleep(float(r.json()['retry_after']))
                    tool.guild_manager.leaver.leave(token, guildid)
                elif r.status_code == 403:
                    cmd.bad(token, 'Locked', r.status_code, r.text)
                elif r.status_code == 404:
                    cmd.bad(token, 'Not in guild', r.status_code, r.text)
                else:   
                    cmd.bad(token, 'Other', r.status_code, r.text)

            def main():
                cmd.preare('Guild manager/Leaver')
                guildid = cmd.ask('GUILD ID')
                if config.online(): thread.single(tool.online, get.tokens())
                thread.single(tool.guild_manager.leaver.leave, get.tokens(), guildid)

        class guild_checker:
            def check_guilds(token, guildid):
                ss = session()
                r = ss.delete(
                    f"https://discord.com/api/v9/guilds/{guildid}",
                    headers=headers.get(token)
                )
                cmd.dbg('GUILD CHECKER', r.status_code, r.text)
                if r.status_code == 200:
                    cmd.good(token, 'Found', r.status_code)
                elif r.status_code == 400:
                    cmd.captha(token, r.status_code)
                elif r.status_code == 429:
                    cmd.ratelimit(token, r.status_code, r.json())
                    time.sleep(float(r.json()['retry_after']))
                    tool.guild_manager.guild_checker.check_guilds(token, guildid)
                elif r.status_code == 403:
                    cmd.bad(token, 'Locked', r.status_code, r.text)
                elif r.status_code == 404:
                    cmd.bad(token, 'Not found', r.status_code, r.text)
                else:   
                    cmd.bad(token, 'Other', r.status_code, r.text)

            def main():
                guildid = cmd.ask('GUILD ID')
                if config.online(): thread.single(tool.online, get.tokens())
                thread.single(tool.guild_manager.guild_checker.check_guilds, get.tokens(), guildid)
        
        class mass_leave:
            def leave(token, guildid, guildname):
                payload = {
                    "lurking": False,
                }
                ss = session()
                r = ss.delete(
                    f"https://discord.com/api/v9/users/@me/guilds/{guildid}",
                    json=payload,
                    headers=headers.get(token, payload)
                )
                cmd.dbg('MASSLEAVE LEAVER', r.status_code, r.text)
                if r.status_code == 204:
                    cmd.good(token, f'Left {guildname}', r.status_code,)
                elif r.status_code == 400:
                    cmd.captha(token, r.status_code)
                elif r.status_code == 429:
                    cmd.ratelimit(token, r.status_code, r.json())
                    time.sleep(float(r.json()['retry_after']))
                    tool.guild_manager.mass_leave.leave(token, guildid, guildname)
                elif r.status_code == 403:
                    cmd.bad(token, 'Locked', r.status_code, r.text)
                elif r.status_code == 404:
                    cmd.bad(token, 'Not in guild', r.status_code, r.text)
                else:   
                    cmd.bad(token, 'Other', r.status_code, r.text)

            def get_guilds(token):
                guilds = []
                ss = session()
                r = ss.get(
                    "https://discord.com/api/v9/users/@me/guilds",
                    headers=headers.get(token),
                )
                cmd.dbg('GUILD GETTER', r.status_code, r.text)
                if r.status_code == 200:
                    for guild in r.json():
                        guild_id = guild['id']
                        guild_name = guild['name']
                        guilds.append({'id': guild_id, 'name': guild_name})
                    return guilds, r.status_code, r.text
                else:
                    return None, r.status_code, r.text
                
            def main():
                cmd.preare('Guild manager/Mass leave')
                if config.online(): thread.single(tool.online, get.tokens())
                for token in get.tokens():
                    guilds, status, text = tool.guild_manager.mass_leave.get_guilds(token)
                    text = json.loads(text)['message']
                    if not guilds:
                        cmd.log('MASS LEAVER', f'Failed to fetch guilds for {token[:30]}{cmd.r}***{cmd.b} ({status}) ({text})')
                        return
                    for guild_info in guilds:
                        tool.guild_manager.mass_leave.leave(token, guild_info['id'], guild_info['name']) 

    class checker:      
        def check_token(token, keep):
            valid = False
            ss = session()
            r = ss.get(
                f"https://discord.com/api/v9/users/@me",
                headers=headers.get(token),
            )
            cmd.dbg('CHECKER', r.status_code, r.text)
            if r.status_code == 200:
                mfa = r.json()['mfa_enabled']
                ev = r.json()['verified']
                email = r.json()['email']
                phone = r.json()['phone']
                if mfa:
                    mfa = f'{cmd.g}[MFA]'
                else:
                    mfa = f'{cmd.r}[MFA]'
                if ev:
                    ev = f'{cmd.g}[EV]'
                else:
                    ev = f'{cmd.r}[EV]'
                if phone:
                    phone = f'{cmd.g}[PHONE]'
                else:
                    phone = f'{cmd.r}[PHONE]'
                cmd.good(token, 'UNLOCKED', r.status_code, f'{mfa} {ev} {phone}{cmd.b}')
                valid = True

            elif r.status_code == 403:
                cmd.bad(token, 'Locked', r.status_code, r.text)
            
            elif r.status_code == 401:
                cmd.bad(token, 'Invalid', r.status_code, r.text)

            elif r.status_code == 429:
                cmd.ratelimit(token, r.status_code, r.json())
                time.sleep(float(r.json()['retry_after']))
                tool.checker.check_token(token, keep)

            if keep:
                if valid:
                    with open(f'data\\tokens.txt', 'a') as f:
                        f.write(token + '\n')

        def check_combo(email, passw, token, keep):
            valid = False
            ss = session()
            r = ss.get(
                f"https://discord.com/api/v9/users/@me",
                headers=headers.get(token),
            )
            cmd.dbg('CHECKER', r.status_code, r.text)
            if r.status_code == 200:
                mfa = r.json()['mfa_enabled']
                ev = r.json()['verified']
                email = r.json()['email']
                phone = r.json()['phone']
                if mfa:
                    mfa = f'{cmd.g}[MFA]'
                else:
                    mfa = f'{cmd.r}[MFA]'
                if ev:
                    ev = f'{cmd.g}[EV]'
                else:
                    ev = f'{cmd.r}[EV]'
                if phone:
                    phone = f'{cmd.g}[PHONE]'
                else:
                    phone = f'{cmd.r}[PHONE]'
                cmd.good(token, 'UNLOCKED', r.status_code, f'{mfa} {ev} {phone}{cmd.b}')
                valid = True

            elif r.status_code == 403:
                cmd.bad(token, 'Locked', r.status_code, r.text)
            
            elif r.status_code == 401:
                cmd.bad(token, 'Invalid', r.status_code, r.text)

            elif r.status_code == 429:
                cmd.ratelimit(token, r.status_code, r.json())
                time.sleep(float(r.json()['retry_after']))
                tool.checker.check_token(token, keep)
            
            else:
                cmd.bad(token, 'Invalid', r.status_code, r.text)

            if keep:
                if valid:
                    with open(f'data\\combo_tokens.txt', 'a') as f:
                        f.write(f'{email}:{passw}:{token}' + '\n')


        def main():
            cmd.preare('Checker')
            dupes = cmd.askyn('REMOVE DUPLICATES')
            keep = cmd.askyn('KEEP VALID ONLY')
            if dupes:
                filename = 'data\\combo_tokens.txt' if config.prefer_combo_tokens() else 'data\\tokens.txt'
                with open(filename, 'r') as f:
                    lines = set(f.readlines())

                with open(filename, 'w') as f:
                    f.writelines(line.strip() + '\n' for line in lines)
            if keep:
                if config.prefer_combo_tokens():
                    cmd.log('CHECKER', 'Combo mode is selected, tokens will be saved to combo_tokens.txt (COMBO CHECKS ARE NOT THREADED)')
                else:
                    cmd.log('CHECKER', 'Token mode is selected, tokens will be saved to tokens.txt')
            tokens = get.tokens()
            if config.prefer_combo_tokens():
                with open('data\\combo_tokens.txt', 'r') as f:
                    combos = f.read().splitlines()
            filename = 'data\\combo_tokens.txt' if config.prefer_combo_tokens() else 'data\\tokens.txt'
            if keep:
                open(filename, 'w')
            if config.online(): thread.single(tool.online, get.tokens())
            if config.prefer_combo_tokens():
                for combo in combos:
                    email, passw, token = combo.strip().split(':')
                    tool.checker.check_combo(email, passw, token)
            else:
                thread.single(tool.checker.check_token, tokens, keep)
    
    class spammer:
        def send_messages(token, message, channelid):
            while True:
                ss = session()
                new_message = tool.spammer.replace(message)
                new_message = f'{new_message}'
                payload = {
                    "content": new_message
                }
                r = ss.post(
                    f"https://discord.com/api/v9/channels/{channelid}/messages",
                    headers=headers.get(token, payload),
                    json=payload
                )
                cmd.dbg('SZPAMMER', r.status_code, r.text)
                if r.status_code == 200:
                    cmd.good(token, 'Sent', r.status_code)
                    continue
                elif r.status_code == 400:
                    cmd.captha(token, r.status_code)
                    continue
                elif r.status_code == 429:
                    cmd.ratelimit(token, r.status_code, r.json())
                    time.sleep(float(r.json()['retry_after']))
                    cmd.dbg(float(r.json()['retry_after']))
                    continue
                elif r.status_code == 401:
                    cmd.bad(token, 'Invalid', r.status_code), r.text
                    break
                elif r.status_code == 403:
                    cmd.bad(token, 'Locked', r.status_code, r.text)
                    break
                else:   
                    cmd.bad(token, 'Other', r.status_code, r.text)
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
                    cmd.log('SPAMMER', f'Getting emojis from {url}...')
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
            cmd.preare('Spammer')
            thread_amt = cmd.ask('THREADS')
            guildid = cmd.ask('GUILD ID')
            channelid = cmd.ask('CHANNEL ID')
            cmd.options('''
(ping=10) ~> Pings 10 people
(emoji=5) ~> Adds 5 random emojis to the message
(str=15) ~> Adds 15 random letters/numbers to the message
EXAMPLE ~> Raided (ping=5) real (str=100) sigmaer (emoji=11)
''')
            message = cmd.ask('MESSAGE')
            if '(ping=' in message:
                cmd.paidc('MASSPING')
                return
            if '(emoji=' in message:
                if not os.path.exists('data\\emojis.txt'):
                    cmd.log('SPAMMER', 'Emojis not saved, getting them...')
                    tool.spammer.get_emojis()
            tokens = tool.channel_acces(channelid)
            if config.online(): thread.single(tool.online, get.tokens())
            thread.multi(thread_amt, tool.spammer.send_messages, tokens, message, channelid)

    class bypasses:
        def main():
            cmd.preare('Bypasses')
            cmd.options('''
01 ~> Reactor
02 ~> Button clicker
03 ~> Onboard bypass
04 ~> Restorecord
05 ~> Back
''')
            c = cmd.ask('CHOICE')
            if c == '1':
                cmd.paid()
            elif c == '2':
                cmd.paid()
            elif c == '3':
                cmd.not_yet()
            elif c == '4':
                cmd.paid()
            elif c == '5':
                return
            else:
                cmd.log('Bypasses', 'Invalid option')

    class combo_to_token:
        def main():
            combo_tokens = get.combo_tokens()
            if not config.prefer_combo_tokens():
                tokens = get.tokens()
            with open('data\\tokens.txt', 'w') as f:
                if tokens:
                    for token in tokens:
                        f.write(f'{token}' + '\n')
                for token in combo_tokens:
                    f.write(f'{token}' + '\n')

    class onliner:
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
            cmd.good(token, 'Onlined', 'None')

        def main():
            thread.single(tool.onliner.online, get.tokens())

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
                    cmd.dbg('THREAD SPAMMMER', r.status_code, r.text)
                    if r.status_code == 200:
                        cmd.good(token, f'Created', r.status_code)
                        continue
                    elif r.status_code == 400:
                        cmd.captha(token, r.status_code)
                        continue
                    elif r.status_code == 429:
                        cmd.ratelimit(token, r.status_code, r.json())
                        time.sleep(float(r.json()['retry_after']))
                        continue
                    elif r.status_code == 403:
                        cmd.bad(token, 'Locked', r.status_code, r.text)
                        break
                    else:   
                        cmd.bad(token, 'Other', r.status_code, r.text)
                        break

        def main():
            cmd.preare('Thread spammer')
            channelid = cmd.ask('CHANNEL ID')
            name = cmd.ask('NAME')
            thread_amt = cmd.ask('THREADS')
            tokens = tool.channel_acces(channelid)
            if config.online(): thread.single(tool.online, get.tokens())
            thread.multi(thread_amt, tool.thread_spammer.create, tokens, channelid, name)

    class forum_spammer:
        def create(token, channelid, name, message):
                while True:
                    ss = session()                                         
                    payload = {
                        "name": name,
                        "auto_archive_duration": 4320,
                        "applied_tags": [],
                        "message":{
                            "content": message
                        }
                    }
                    r = ss.post(
                        f"https://discord.com/api/v9/channels/{channelid}/threads?use_nested_fields=true",
                        headers=headers.get(token, payload),
                        json=payload
                    )
                    cmd.dbg('FORUM SPAMMMER', r.status_code, r.text)
                    if r.status_code == 200:
                        cmd.good(token, f'Created', r.status_code)
                        continue
                    elif r.status_code == 400:
                        cmd.captha(token, r.status_code)
                        continue
                    elif r.status_code == 429:
                        cmd.ratelimit(token, r.status_code, r.json())
                        time.sleep(float(r.json()['retry_after']))
                        continue
                    elif r.status_code == 403:
                        cmd.bad(token, 'Locked', r.status_code, r.text)
                        break
                    else:   
                        cmd.bad(token, 'Other', r.status_code, r.text)
                        break

        def main():
            cmd.preare('Forum spammer')
            channelid = cmd.ask('CHANNEL ID')
            name = cmd.ask('NAME')
            message = cmd.ask('MESSAGE')
            thread_amt = cmd.ask('THREADS')
            tokens = tool.channel_acces(channelid)
            if config.online(): thread.single(tool.online, get.tokens())
            thread.multi(thread_amt, tool.forum_spammer.create, tokens, channelid, name, message)

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

            except Exception as e:
                cmd.dbg(e)

        def main():
            cmd.preare('VC joiner')
            channelid = cmd.ask('CHANNEL ID')
            guildid = cmd.ask('GUILD ID')
            tokens = tool.channel_acces(channelid)
            if config.online(): thread.single(tool.online, get.tokens())
            thread.single(tool.vc_joiner.connect_vc, tokens, channelid, guildid)

    class vc_spammer:

        def get_sounds(token):
            ss = session()
            r = ss.get(
                "https://discord.com/api/v9/soundboard-default-sounds",
                headers=headers.get(token)
            )
            cmd.dbg(r.text, r.status_code)
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
                cmd.dbg('SOUNDBOARD SPAM', r.status_code, r.text)
                if r.status_code == 204:
                    cmd.good(token, f'Soundboarded {name}', r.status_code)
                    continue
                elif r.status_code == 400:
                    cmd.captha(token, r.status_code)
                    continue
                elif r.status_code == 429:
                    cmd.ratelimit(token, r.status_code, r.json())
                    time.sleep(float(r.json()['retry_after']))
                    continue
                elif r.status_code == 403:
                    if 'code' in r.json() and r.json()['code'] == 50168:
                        tool.vc_spammer.connect_vc(token, channelid, guildid)
                        continue
                    else:
                        cmd.bad(token, 'Locked', r.status_code, r.text)
                        break

                else:
                    cmd.bad(token, 'Other', r.status_code, r.text)
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

                cmd.good(token, 'Connected to VC', None)
            except Exception as e:
                cmd.dbg(e)

        def main():
            cmd.preare('VC spammer')
            channelid = cmd.ask('CHANNEL ID')
            guildid = cmd.ask('GUILD ID')
            thread_amt = cmd.ask('THREADS')
            tokens = tool.channel_acces(channelid)
            sounds = tool.vc_spammer.get_sounds(random.choice(tokens))
            if config.online(): thread.single(tool.online, get.tokens())
            thread.single(tool.vc_spammer.connect_vc, tokens, channelid, guildid)  
            thread.multi(thread_amt, tool.vc_spammer.spam, tokens, channelid, guildid, sounds)

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
                cmd.dbg('MASS RESPOND', r.status_code, r.text)
                if r.status_code == 200:
                    cmd.good(token, f'Responded', r.status_code)
                    continue
                elif r.status_code == 400:
                    cmd.captha(token, r.status_code)
                    continue
                elif r.status_code == 429:
                    cmd.ratelimit(token, r.status_code, r.json())
                    time.sleep(float(r.json()['retry_after']))
                    continue
                elif r.status_code == 403:
                    cmd.bad(token, 'Locked', r.status_code, r.text)
                    break

                else:
                    cmd.bad(token, 'Other', r.status_code, r.text)
                    break


        def main():
            cmd.preare('Mass respond')
            messagelink = cmd.ask('MESAGE LINK')
            message = cmd.ask('MESSAGE')
            thread_amt = cmd.ask('THREADS')
            guildid, channelid, messageid = tool.link_transform(messagelink)
            tokens = tool.channel_acces(channelid)
            if config.online(): thread.single(tool.online, get.tokens())
            thread.multi(thread_amt, tool.mass_respond.respond, tokens, messagelink, message)

while __name__ == '__main__':
    cmd.cls()
    cmd.title(main_name)
    cmd.menu()
    
    if config.captcha_bypass():
        cmd.paidc('CAPTCHA BYPASS')
        time.sleep(3)
        sys.exit()

    if config.proxies():
        cmd.paidc('PROXIES')
        time.sleep(3)
        sys.exit()

    if config.paid_solver():
        cmd.paidc('PAID SOLVER')
        time.sleep(3)
        sys.exit()

    c = input(f'{cmd.r}~> {cmd.b}')
    options = {
        '1': tool.guild_manager.main,
        '2': tool.checker.main,
        '3': tool.spammer.main,
        '4': tool.bypasses.main,
        '5': cmd.paid,
        '6': tool.combo_to_token.main,
        '7': tool.onliner.main,
        '8': cmd.paid,
        '9': cmd.paid,
        '10': cmd.paid,
        '11': cmd.paid,
        '12': cmd.paid,
        '13': cmd.paid,
        '14': cmd.paid,
        '15': cmd.paid,
        '16': cmd.paid,
        '17': cmd.paid,
        '18': cmd.paid,
        '19': cmd.paid,
        '20': tool.thread_spammer.main,
        '21': tool.forum_spammer.main,
        '22': cmd.paid,
        '23': tool.vc_joiner.main,
        '24': tool.vc_spammer.main,
        '25': cmd.paid,
        '26': tool.mass_respond.main,
        '27': cmd.paid
    }

    if c in options:
        cmd.cls(); cmd.banner()
        options[c]()
        cmd.log('CORE', 'If u like the free version make sure to vouch at #vouches in https://dsc.gg/vanadium')
        cmd.inplog('CORE', 'Finished the task! Enter to continue')
        cmd.cls()
    elif c == '>>':
        cmd.menu2()
        cmd.not_yet()
        time.sleep(2)
    else: 
        cmd.log('CORE', 'Invalid option')
        time.sleep(2)
        cmd.cls()
        

# bro dont skid
