from src import *
from src.plugins.log import *
from src.plugins.ui import *
from src.discord import *
from src.plugins.client import client
from src.plugins.threads import * 
from src.plugins.files import *

class checker:
    def __init__(self):
        self.serverid = None
        self.valids = []

    def check(self, token):
        cl = client(token)
        cl.headers['Authorization'] = token

        state = cl.sess.get(
            'https://discord.com/api/v9/users/@me/library',
            headers=headers,
            cookies=cookies
        )

        log.dbg('Checker', state.text, state.status_code)

        if state.status_code == 200:
            log.info('Checker', f'{token[:30]}... >> Valid >> Token info is paid only')
            self.valids.append(token)

        elif 'retry_after' in state.text:
            limit = state.json()['retry_after']
            log.warn('Checker', f'{token[:30]}... >> Limited for {limit}s')
            time.sleep(float(limit))
            self.check(token)

        elif 'Cloudflare' in state.text:
            log.warn('Checker', f'{token[:30]}... >> CLOUDFLARE BLOCKED >> Waiting for 5 secs and retrying')
            time.sleep(5)
            self.check(token)

        elif 'captcha_key' in state.text:
            log.hcap('Checker', f'{token[:30]}... >> HCAPTCHA')

        elif 'You need to verify' in state.text:
            log.critical('Checker', f'{token[:30]}... >> LOCKED')

        else:
            error = log.errordatabase(state.text)
            log.error('Checker', error)

    
    def main(self):
        savevalid = ui().ask('Save only valids', True)
        thread(
            files().getthreads(),
            self.check,
            files().gettokens(),
            []
        )

        if savevalid:
            with open('input\\tokens.txt', 'w') as f:
                for token in self.valids:
                    f.write(f'{token}\n')