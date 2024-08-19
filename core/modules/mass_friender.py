from core import *
from core.plugins.client import *
from core.discordutils import *
from core.plugins.cmd import *
from core.plugins.ui import *
from core.plugins.threads import *

class mass_friender:
    class add:
        def add(token: str, username: str, csess = None):
            sess, cookies, headers = client.build(token)
            if csess != None: sess = csess

            payload = {
                'username': username,
                'discriminator': None
            }

            r = sess.post(
                f'https://discord.com/api/v9/users/@me/relationships',
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

            if r.status_code == 204:
                log.good('Friended', f'{token[:30]}...')
            
            elif 'code' in resp and resp['code'] == '20028':
                limit = float(r.json()['retry_after'])
                log.liimt(f'{token[:30]}... -> {limit}s')
                time.sleep(limit)
                mass_friender.add.add(token, username, sess)

            elif 'captcha_key' in resp:
                log.hcap(f'{token[:30]}...')

            elif 'You need to verify' in resp:
                log.locked(f'{token[:30]}...')

            else:
                log.fail(resp)

    class remove:
        def remove(token: str, username: str, csess = None):
            sess, cookies, headers = client.build(token)
            if csess != None: sess = csess

            r = sess.delete(
                f'https://discord.com/api/v9/users/@me/relationships/{username}',
                headers=headers,
                cookies=cookies
            )

            log.debug(r.status_code)
            log.debug(r.text)

            try:
                resp = r.json()
            except:
                resp = r.text

            if r.status_code == 204:
                log.good('Unfriended', f'{token[:30]}...')
            
            elif 'code' in resp and resp['code'] == '20028':
                limit = float(r.json()['retry_after'])
                log.liimt(f'{token[:30]}... -> {limit}s')
                time.sleep(limit)
                mass_friender.remove.remove(token, username, sess)

            elif 'captcha_key' in resp:
                log.hcap(f'{token[:30]}...')

            elif 'You need to verify' in resp:
                log.locked(f'{token[:30]}...')

            else:
                log.fail(resp)

    def menu():
        cmd.cls()
        UI().banner()
        UI().make_menu([
            'Mass add', 
            'Mass remove'
        ], True)
        choice = UI().ask('CHOICE')
        
        if choice in ['01', '1']:
            threads = UI().ask('THREADS')
            username = UI().ask('USERNAME')

            tokens = get.tokens()
            log.log('Mass friend add', f'Adding {username} with {len(tokens)} tokens...')

            thread(
                threads,
                mass_friender.add.add,
                tokens,
                [username]
            ).work()

        if choice in ['02', '2']:
            threads = UI().ask('THREADS')
            username = UI().ask('USERNAME')

            tokens = get.tokens()
            log.log('Mass friend add', f'Removing {username} with {len(tokens)} tokens...')

            thread(
                threads,
                mass_friender.remove.remove,
                tokens,
                [username]
            ).work()

        elif choice == '<<':
            log.log('UI', 'Returning')

        else:
            log.log('UI', 'Invalid option')