from src import *
from src.plugins.log import *
from src.plugins.ui import *
from src.dchelper import *
from src.plugins.client import client
from src.plugins.threads import * 
from src.plugins.files import *

class pron_changer:
    def __init__(self):
        self.newpron = None

    def change(self, token):
        cl = client(token)
        cl.headers['Authorization'] = token

        payload = {
            'pronouns': self.newpron
        }

        r = cl.sess.patch(
            f'https://discord.com/api/v9/users/@me/profile',
            headers=cl.headers,
            cookies=cl.cookies,
            json=payload
        )

        log.dbg('Pron changer', r.text, r.status_code)

        if r.status_code == 200:
            log.info('Pron changer', f'{token[:30]}... >> Changed to >> {self.newpron}')

        elif 'retry_after' in r.text:
            limit = r.json()['retry_after']
            log.warn('Pron changer', f'{token[:30]}... >> Limited for {limit}s')
            time.sleep(float(limit))
            self.change(token)

        elif 'Cloudflare' in r.text:
            log.warn('Pron changer', f'{token[:30]}... >> CLOUDFLARE BLOCKED >> Waiting for 5 secs and retrying')
            time.sleep(5)
            self.change(token)

        elif 'captcha_key' in r.text:
            log.hcap('Pron changer', f'{token[:30]}... >> HCAPTCHA')

        elif 'You need to verify' in r.text:
            log.critical('Pron changer', f'{token[:30]}... >> LOCKED')

        else:
            error = log.errordatabase(r.text)
            log.error('Pron changer', error)
    
    def main(self):
        self.newpron = ui().ask('New pron')

        thread(
            files.getthreads(),
            self.change,
            files.gettokens(),
            []
        )