from core import *
from core.plugins.get import *
from core.plugins.config import cfg

class rpc:
    def __init__(self):
        self.client_id = '1256728209941205182'
        self.large_image = 'main'
        self.rpc = Presence(client_id=self.client_id)
        try:
            self.rpc.connect()
        except:
            pass

    def update(self, details: str):
        try:
            if cfg().rpc():
                self.rpc.update(
                    details=details,
                    state=f'Tokens {get.token_count()} | Proxies {get.proxy_count()}',
                    large_image=self.large_image,
                    buttons = [
                        {'label': 'Get', 'url': 'https://dsc.gg/limetool'},
                    ],
                    start=int(time.time())
                )
            else:
                pass
        except:
            pass

rpc = rpc()
if cfg().rpc():
    rpc.update(details='Loading...')