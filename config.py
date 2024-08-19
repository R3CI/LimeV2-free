from core import *
from core import __CFG_VERSION__
from core.plugins.log import *

class tomlshit:
    def parse_toml(lines):
        config = {}
        current_section = None

        for line in lines:
            line = line.strip()
            if line.startswith('[') and line.endswith(']'):
                current_section = line[1:-1]
                config[current_section] = {}
            elif '=' in line and current_section:
                key, value = line.split('=', 1)
                key = key.strip()
                value = value.split('#', 1)[0].strip()
                if value.lower() in ('true', 'false'):
                    value = value.lower() == 'true'
                elif value.isdigit():
                    value = int(value)
                else:
                    value = value.strip('"')
                config[current_section][key] = value

        return config

class cfg_util:
    def __init__(self):
        self.newestdata = {
            'main': {
                'use proxies': False,
                'use rpc': True
            },
            'headers': {
                'mode': 'Desktop',
                'custom user agent': '',
                'custom xsuper props': '',
            },
            'dev': {
                'cfg version': '1.0',
            }
        }

        self.comments = {
            'main.use proxies': 'If you want to use this, put your proxies inside of data/proxies.txt (99% OF FREE PROXIES ARE BLOCKED BY DISCORD)',
            'main.use rpc': 'Shows the module you are using, amount of tokens and proxies (main account not tokens)',
            'headers.mode': 'You can use Desktop, Mobile, Browser (ONLY DESKTOP SUPPORTED ATM)',
            'headers.custom user agent': 'Not needed at all but if you for some reason want to have a custom one you can',
            'headers.custom xsuper props': 'Same as with custom user agent'
        }

        if not os.path.exists('config.toml') or os.path.getsize('config.toml') == 0:
            self.write()

        self.config =  open('config.toml', 'r')
        self.config = tomlshit.parse_toml(self.config.readlines())

        log.log('CONFIG', 'Checking config version...')
        if float(self.config['dev']['cfg version']) < float(__CFG_VERSION__):
            self.update()

    def write(self):
        with open('config.toml', 'w') as f:
            for section, params in self.newestdata.items():
                f.write(f'[{section}]\n')
                for param, value in params.items():
                    comment_key = f'{section}.{param}'
                    comment = self.comments.get(comment_key, '')
                    if isinstance(value, str):
                        value = f'"{value}"'
                    f.write(f'{param} = {value}  # {comment}\n')
                f.write('\n')
    
    def update(self):
        with open('config.toml', 'r') as f:
            lines = f.readlines()
            self.config = tomlshit.parse_toml(lines)

            for section, params in self.newestdata.items():
                if section not in self.config:
                    self.config[section] = {}
                for param, value in params.items():
                    self.config[section].setdefault(param, value)

            f = open('config.toml', 'w')
            for section, params in self.config.items():
                f.write(f'[{section}]\n')
                for param, value in params.items():
                    comment_key = f'{section}.{param}'
                    comment = self.comments.get(comment_key, '')
                    if isinstance(value, str):
                        value = f'"{value}"'
                    f.write(f'{param} = {value}  # {comment}\n')
                f.write('\n')

        log.log('CONFIG', 'Updated config to the newest version! Please check the config and set the new values to what u like', inp=True)

class cfg:
    def __init__(self):
        self.config = open('config.toml', 'r')
        self.config = tomlshit.parse_toml(self.config.readlines())

    def useprx(self) -> bool:
        return self.config['main']['use proxies']

    def rpc(self) -> bool:
        return self.config['main']['use rpc']
    
    def headermode(self) -> str:
        return self.config['headers']['mode']

    def customua(self) -> str:
        return self.config['headers']['custom user agent']
    
    def customxsup(self) -> str:
        return self.config['headers']['custom xsuper props']

    def rpc(self) -> bool:
        return self.config['main']['use rpc']

    def cfgversion(self) -> bool:
        return self.config['dev']['version']

cfg_util()
