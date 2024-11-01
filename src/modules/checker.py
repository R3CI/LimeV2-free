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
            log.info('Checker', f'{token[:30]}... >> Valid')

        elif 'retry_after' in state.text:
            limit = state.json()['retry_after']
            log.warn('Checker', f'{token[:30]}... >> Limited for {limit}s')
            time.sleep(float(limit))
            self.check(token)

        elif 'You need to verify' in state.text:
            log.critical('Checker', f'{token[:30]}... >> LOCKED')

        else:
            error = log.errordatabase(state.text)
            log.error('Checker', error)

    
    def main(self):
        thread(
            files().getthreads(),
            self.check,
            files().gettokens(),
            []
        )
