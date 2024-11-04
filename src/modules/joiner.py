from src import *
from src.plugins.log import *
from src.plugins.ui import *
from src.discord import *
from src.plugins.client import client
from src.plugins.threads import * 
from src.plugins.files import *

class joiner:
    def __init__(self):
        self.vanity = False
        self.invite = None
        self.serverid = None
        self.servername = None
        self.invchannelid = None
        self.invchanneltype = None

    def join(self, token):
        cl = client(token)

        payload = {
            'session_id': uuid.uuid4().hex,
        }

        xcontent = {
            'location': 'Join Guild',
            'location_guild_id': self.serverid,
            'location_channel_id': self.invchannelid,
            'location_channel_type': self.invchanneltype
        }
        xcontent = json.dumps(xcontent)
        xcontent = xcontent.encode('utf-8')
        xcontent = base64.b64encode(xcontent).decode('utf-8')

        cl.headers['X-Context-Properties'] = xcontent
        cl.headers['Authorization'] = token

        r = cl.sess.post(
            f'https://discord.com/api/v9/invites/{self.invite}',
            headers=cl.headers,
            cookies=cl.cookies,
            json=payload
        )

        log.dbg('Joiner', r.text, r.status_code)

        if r.status_code == 200:
            log.info('Joiner', f'{token[:30]}... >> Joined >> {self.servername} ({self.serverid}) (discord.gg/{self.invite})')

        elif 'retry_after' in r.text:
            limit = r.json()['retry_after']
            log.warn('Joiner', f'{token[:30]}... >> Limited for {limit}s')
            time.sleep(float(limit))
            self.join(token)

        elif 'Cloudflare' in r.text:
            log.warn('Checker', f'{token[:30]}... >> CLOUDFLARE BLOCKED >> Waiting for 5 secs and retrying')
            time.sleep(5)
            self.join(token)

        elif 'captcha_key' in r.text:
            log.hcap('Joiner', f'{token[:30]}... >> HCAPTCHA')

        elif 'You need to verify' in r.text:
            log.critical('Joiner', f'{token[:30]}... >> LOCKED')

        else:
            error = log.errordatabase(r.text)
            log.error('Joiner', error)

    
    def main(self):
        self.invite = ui().ask('Invite')
        self.invite = discord().extract_invite(self.invite)
        invinfo = discord().get_invite_info(self.invite)
        if invinfo.get('guild', {}).get('vanity_url_code', None) is not None:
            self.vanity = True

        #self.invite = invinfo.get('guild', {}).get('vanity_url_code', self.invite)
        self.serverid = invinfo.get('guild', {}).get('id', None)
        self.servername = invinfo.get('guild', {}).get('name', None)
        self.invchannelid = invinfo.get('channel', {}).get('id', None)
        self.invchanneltype = invinfo.get('channel', {}).get('type', None)

        thread(
            files().getthreads(),
            self.join,
            files().gettokens(),
            []
        )