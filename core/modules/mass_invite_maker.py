from core import *
from core.plugins.client import *
from core.discordutils import *
from core.plugins.cmd import *
from core.plugins.ui import *
from core.plugins.threads import *

class mass_invite_maker:
    def make_inv(token: str, channelid: str, csess = None):
            sess, cookies, headers = client.build(token)
            if csess != None: sess = csess

            while True:
                age = random.randint(1000, 604800)
                uses = random.randint(0, 100)
                temp = random.choice(['True', 'False'])

                payload = {
                    'max_age': age,
                    'max_uses': uses,
                    'target_type': None,
                    'temporary': temp,
                }

                r = sess.post(
                    f'https://discord.com/api/v9/channels/{channelid}/invites',
                    headers=headers,
                    cookies=cookies,
                    json=payload
                )

                log.debug(r.status_code)
                log.debug(r.text)

                try:
                    resp = r.json()
                except:
                    resp = r.text

                if r.status_code == 200:
                    log.good('Made invite', f'{token[:30]}...')
                    continue
                
                elif 'code' in resp and resp['code'] == '20028':
                    limit = float(r.json()['retry_after'])
                    log.liimt(f'{token[:30]}... -> {limit}s')
                    time.sleep(limit)
                    continue

                elif 'captcha_key' in resp:
                    log.hcap(f'{token[:30]}...')
                    break

                elif 'You need to verify' in resp:
                    log.locked(f'{token[:30]}...')
                    break

                else:
                    log.fail(resp)
                    break
        

    def menu():
        cmd.cls()
        UI().banner()
        threads = UI().ask('THREADS')
        channelid = UI().ask('CHANNEL ID')
        serverid = UI().ask('SERVER ID')    

        tokens = Discord.get_server_acces_tokens(serverid)

        log.log('Mass invite maker', f'Making invites on {serverid} with {len(tokens)} tokens...')

        thread(
            threads,
            mass_invite_maker.make_inv,
            tokens,
            [channelid]
        ).work()