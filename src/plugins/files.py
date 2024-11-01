from src import *
from src.plugins.log import *

class files:
    def __init__(self):
        self.settings_version = 1.0
        self.newest_settings = {
            'version': self.settings_version,
            'advanced-mode': True,
            'threads': 10,
            'proxies': False
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
        with open('input\\tokens.txt', 'r') as f:
            tokens = f.read().splitlines()
        
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
