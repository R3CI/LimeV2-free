import re
from src import *
from src.plugins.log import *
from src.plugins.ui import *
from src.discord import *
from src.plugins.client import client
from src.plugins.threads import * 
from src.plugins.files import *

class message_spammer:
    def __init__(self):
        self.serverid = None
        self.channelid = None
        self.basemsg = None
        self.tts = False
        self.ids = []

    def replacer(self, match):
        tag, number = match.group(1), match.group(2)
        if tag == 'emoji':
            return discord().getemojis(int(number))
        elif tag == 'str':
            return discord().getstr(int(number))
        return ''

    def replace_tags(self, text):
        return re.sub(r'\[\[(str|ping|emoji)=(\d+)\]\]|\[\[.*?\]\]', self.replacer, text)

    def send(self, token):
        cl = client(token)
        while True:
            message = self.replace_tags(self.basemsg)
            if isinstance(message, list):
                message = ' '.join(message)

            payload = {
                'mobile_network_type': 'unknown',
                'content': message,
                'nonce': discord().getsnowflake(),
                'tts': self.tts,
                'flags': 0
            }

            cl.headers['Authorization'] = token
            r = cl.sess.post(
                f'https://discord.com/api/v9/channels/{self.channelid}/messages',
                headers=cl.headers,
                cookies=cl.cookies,
                json=payload
            )

            log.dbg('Message spammer', r.text, r.status_code)

            if r.status_code == 200:
                log.info('Message spammer', f'{token[:30]}... >> In >> {self.channelid}')
                continue

            elif 'retry_after' in r.text:
                limit = r.json()['retry_after']
                log.warn('Message spammer', f'{token[:30]}... >> Limited for {limit}s')
                time.sleep(float(limit))
                continue

            elif 'Cloudflare' in r.text:
                log.warn('Message spammer', f'{token[:30]}... >> CLOUDFLARE BLOCKED >> Waiting for 5 secs and retrying')
                time.sleep(5)
                continue

            elif 'captcha_key' in r.text:
                log.hcap('Message spammer', f'{token[:30]}... >> HCAPTCHA')
                break

            elif 'You need to verify' in r.text:
                log.critical('Message spammer', f'{token[:30]}... >> LOCKED')
                break
            
            else:
                error = log.errordatabase(r.text)
                log.error('Message spammer', error)
                break

    def main(self):
        self.channelid = ui().ask('Channel ID')
        self.serverid = ui().ask('Server ID')
        self.tts = ui().ask('TTS (reads off the messages for everyone in that channel but the tokens need permissions for it and it is very unlike)', True)
        log.info('Message spammer', 'Tags that you can use [[ping=10]] [[str=10]] [[emoji=10]]', False, False)   
        log.info('Message spammer', 'An example of what you would type now Raided [[ping=10]] [[str=10]] [[emoji=10]]', False, False)  
        log.info('Message spammer', 'Remembr the number after = is fully custom you could do 100 or 33 whatever u want', False, False)   
        log.info('Message spammer', 'ping is paid only!!!', False, False)   
        self.basemsg = ui().ask('Message') 

        thread(
            files().getthreads(),
            self.send,
            files().gettokens(),
            []
        )
