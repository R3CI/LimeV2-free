from src import *
from src.plugins.log import *

class files:
    def __init__(self):
        self.settings_version = 2.0
        self.newest_settings = {
            'version': self.settings_version,
            'advanced-mode': False,
            'threads': 10,
            'proxies': False,
            'usesolver': False,
            'solvertype (can use: csolver)': '',
            'solverapikey': ''
        }

        self.dirs = [
            'input',
            'output',
            'output\\scrapes',
            'output\\scrapes\\ids',
            'output\\scrapes\\usernames',
        ]
        self.files = [
            'settings.json',
            'input\\tokens.txt',
            'input\\proxies.txt',

            'output\\errors.txt',
            'output\\output.txt',
            'output\\debug.txt'
        ]

        self.check()
        if not self.check_settings_update():
            self.update_settings()
        
        if self.getsolverapikey() or self.getsolverstatus():
            log.info('Files', f'Solver support is PAID ONLY')

        if self.getproxystatus():       
            log.info('Files', 'Proxy support is PAID ONLY')

        #if not self.getproxies() and self.getproxystatus():
        #    messagebox.showerror('Info', 'Proxies ware enabled inside of settings.json but none are inside of input\\proxies.txt the code will not work properly please input proxies or disable proxies in settings.json')

        #if not self.getsolverapikey() and self.getsolverstatus():
        #    messagebox.showerror('Info', 'Solver is enabled inside of settings.json and u have not provided the api key inside of settings.json please provide the api key or disable solver in settings.json')

        if not self.gettokens():
            messagebox.showerror('Info', 'U did not input any tokens into input\\tokens.txt please input them in! (NOT DISCORD BOT TOKENS ACTUAL ACCOUNT TOKENS) run /tokens command on my server to get more info')

    def check(self):
        for dir in self.dirs:
            if not os.path.exists(dir):
                os.mkdir(dir)

        for file in self.files:
            if not os.path.exists(file):
                with open(file, 'w'):
                    pass
                    
    def check_settings_update(self):
        with open('settings.json', 'r+') as f:
            content = f.read().strip()
            if not content:
                json.dump(self.newest_settings, f, indent=4)
                time.sleep(0.3)
            setts = json.loads(content)
            if float(setts['version']) != float(self.settings_version):
                return False
            return True

    def update_settings(self):
        with open('settings.json', 'r') as f:
            setts = json.load(f)

        if setts['version'] != self.settings_version:
            for key, value in self.newest_settings.items():
                if key == 'version':
                    setts[key] = value
                elif key in setts:
                    continue
                else:
                    setts[key] = value 

            with open('settings.json', 'w') as f:
                json.dump(setts, f, indent=4)
        else:
            pass

    def gettokens(self):
        tokens = []
        with open('input\\tokens.txt', 'r') as f:
            tokens_ = f.read().splitlines()
        
        for token_ in tokens_:
            token = ''.join(c for c in token_ if c in set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_. '))
            tokens.append(token)

        random.shuffle(tokens)
        log.dbg('Files', tokens)
        return tokens

    def getproxies(self):
        with open('input\\proxies.txt', 'r') as f:
            proxies = f.read().splitlines()
        
        random.shuffle(proxies)
        log.dbg('Files', proxies)
        return proxies
    
    def getthreads(self):
        with open('settings.json', 'r') as f:
            setts = json.load(f)['threads']
        return setts

    def getsolverapikey(self):
        with open('settings.json', 'r') as f:
            setts = json.load(f)['solverapikey']
        return setts

    def getproxystatus(self):
        with open('settings.json', 'r') as f:
            setts = json.load(f)['proxies']
        return setts
    
    def getsolvertype(self):
        with open('settings.json', 'r') as f:
            setts = json.load(f)['solvertype (can use: csolver)']
        return setts

    def getsolverstatus(self):  
        with open('settings.json', 'r') as f:
            setts = json.load(f)['usesolver']
        return setts

files = files()