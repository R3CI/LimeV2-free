from src import *
from src.plugins.log import *
from src.plugins.ui import *
from src.discord import *
from src.plugins.client import client
from src.plugins.threads import * 
from src.plugins.files import *

class leaver:
    def __init__(self):
        self.serverid = None

    def leave(self, token):
        cl = client(token)

        payload = {
            'lurking': False,
        }

        cl.headers['Authorization'] = token

        r = cl.sess.delete(
            f'https://discord.com/api/v9/users/@me/guilds/{self.serverid}',
            headers=cl.headers,
            cookies=cl.cookies,
            json=payload
        )

        log.dbg('Leaver', r.text, r.status_code)

        if r.status_code == 200:
            log.info('Leaver', f'{token[:30]}... >> Left >> {self.serverid}')

        elif 'retry_after' in r.text:
            limit = r.json()['retry_after']
            log.warn('Leaver', f'{token[:30]}... >> Limited for {limit}s')
            time.sleep(float(limit))
            self.leave(token)

        elif 'captcha_key' in r.text:
            log.hcap('Leaver', f'{token[:30]}... >> HCAPTCHA')

        elif 'You need to verify' in r.text:
            log.critical('Leaver', f'{token[:30]}... >> LOCKED')

        else:
            error = log.errordatabase(r.text)
            log.error('Leaver', error)

    
    def main(self):
        self.serverid = ui().ask('Server ID')

        tokens = discord().get_server_acceses(self.serverid, files().gettokens())
        if not tokens:
            log.info('Leaver', 'Seems like none of the tokens are in the server (or the check failed)', True, False)   

        thread(
            files().getthreads(),
            self.leave,
            tokens,
            []
        )