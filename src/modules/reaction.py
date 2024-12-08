from src import *
from src.plugins.log import *
from src.plugins.ui import *
from src.discord import *
from src.plugins.client import client
from src.plugins.threads import * 
from src.plugins.files import *

class reaction:
    def __init__(self):
        self.serverid = None
        self.channelid = None
        self.messageid = None
        self.reaction = None
        self.dodebypass = False

    def bypass(self, token):
        cl = client(token)
        cl.headers['Authorization'] = token

        r = cl.sess.put(
            f'https://discord.com/api/v9/channels/{self.channelid}/messages/{self.messageid}/reactions/{self.reaction}/@me?location=Message&type=0',
            headers=cl.headers,
            cookies=cl.cookies
        )

        log.dbg('Reaction', r.text, r.status_code)

        if r.status_code == 204:
            log.info('Reaction', f'{token[:30]}... >> Bypassed')

        elif 'retry_after' in r.text:
            limit = r.json()['retry_after']
            log.warn('Reaction', f'{token[:30]}... >> Limited for {limit}s')
            time.sleep(float(limit))
            self.bypass(token)

        elif 'Cloudflare' in r.text:
            log.warn('Reaction', f'{token[:30]}... >> CLOUDFLARE BLOCKED >> Waiting for 5 secs and retrying')
            time.sleep(5)
            self.bypass(token)

        elif 'captcha_key' in r.text:
            log.hcap('Reaction', f'{token[:30]}... >> HCAPTCHA')

        elif 'You need to verify' in r.text:
            log.critical('Reaction', f'{token[:30]}... >> LOCKED')

        else:
            error = log.errordatabase(r.text)
            log.error('Reaction', error)
    
    def debypass(self, token):
        cl = client(token)
        cl.headers['Authorization'] = token

        r = cl.sess.delete(
            f'https://discord.com/api/v9/channels/{self.channelid}/messages/{self.messageid}/reactions/{self.reaction}/@me?location=Message&type=0',
            headers=cl.headers,
            cookies=cl.cookies
        )
    
        log.dbg('De reaction', r.text, r.status_code)

        if r.status_code == 204:
            log.info('De reaction', f'{token[:30]}... >> De reacted')

        elif 'retry_after' in r.text:
            limit = r.json()['retry_after']
            log.warn('De reaction', f'{token[:30]}... >> Limited for {limit}s')
            time.sleep(float(limit))
            self.debypass(token)

        elif 'Cloudflare' in r.text:
            log.warn('De reaction', f'{token[:30]}... >> CLOUDFLARE BLOCKED >> Waiting for 5 secs and retrying')
            time.sleep(5)
            self.bypass(token)

        elif 'captcha_key' in r.text:
            log.hcap('De reaction', f'{token[:30]}... >> HCAPTCHA')

        elif 'You need to verify' in r.text:
            log.critical('De reaction', f'{token[:30]}... >> LOCKED')

        else:
            error = log.errordatabase(r.text)
            log.error('De reaction', error)

    def main(self):
        self.serverid = ui().ask('Server ID')
        self.channelid = ui().ask('Channel ID')
        self.messageid = ui().ask('Message ID')
        self.dodebypass = ui().ask('Do de bypass? (If the tokens alerdy reacted this will also first remove the rection so they get actualy verified again)', True)

        reacts = []
        messages = discord().get_messages(self.channelid, files().gettokens())
        for message in messages:
            if message['id'] == self.messageid:
                for reaction in message['reactions']:
                    emoji_name = reaction['emoji']['name']
                    count = reaction['count']
                    reacts.append((emoji_name, count))
        
        if not reacts:
            log.info('Reaction', 'No reactions found')
            return

        mn = []
        for _, (reactionname, count) in enumerate(reacts, 1):
            mn.append(f'{reactionname} - {count}')

        ui().make_menu(mn)
        selected = int(ui().ask('Choice')) - 1
        self.reaction = reacts[selected][0]

        if self.dodebypass:
            thread(
                files().getthreads(),
                self.debypass,
                files().gettokens(),
                []
            )

        time.sleep(1)

        thread(
            files().getthreads(),
            self.bypass,
            files().gettokens(),
            []
        )
