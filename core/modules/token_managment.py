from core import *
from core.plugins.client import *
from core.discordutils import *
from core.plugins.cmd import *
from core.plugins.ui import *
from core.plugins.threads import *

class token_managment:
    class checker:
        def check(token: str):
            sess, cookies, headers = client.build(token)
            info = sess.get(
                'https://discord.com/api/v9/users/@me',
                headers=headers,
                cookies=cookies
            )

            state = sess.get(
                'https://discord.com/api/v9/users/@me/library',
                headers=headers,
                cookies=cookies
            )

            try:
                resp = state.json()
            except:
                resp = state.text

            if state.status_code == 200:
                log.good('VALID', f'{token[:30]}... (SKIPPING INFO ABT THE TOKEN AS IT IS PAID ONLY)')
                with open('data\\tokens.txt', 'a') as f:
                    f.write(f'{token}\n')

            elif 'code' in resp and resp['code'] == '20028':
                limit = float(state.json()['retry_after'])
                log.liimt(f'{token[:30]}... -> {limit}s')
                time.sleep(limit)
                token_managment.checker.check(token)

            elif 'captcha_key' in resp:
                log.hcap(f'{token[:30]}...')

            elif 'You need to verify' in resp:
                log.locked(f'{token[:30]}...')

            else:
                log.fail(resp)

    class combototoken:
        def convert(token: str, combopath):
            tkns = []
            with open (combopath, 'r') as f:
                for line in f:
                    parts = line.strip().split(':')
                    if len(parts) == 3:
                        tkns.append(parts[2])

            with open('data\\tokens.txt', 'a') as f:
                for token in tkns:
                    f.write(f'{token}\n')

    class nuker:
        def leave(
                token: str, 
                serverid: str,
                name: str,
                csess = None
            ):
            sess, cookies, headers = client.build(token)
            if csess != None: sess = csess

            payload = {
                'lurking': False,
            }

            r = sess.delete(
                f'https://discord.com/api/v9/users/@me/guilds/{serverid}',
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
                log.good('Left', f'{token[:30]}... -> {name} -> {serverid}')
            
            elif 'code' in resp and resp['code'] == '20028':
                limit = float(r.json()['retry_after'])
                log.liimt(f'{token[:30]}... -> {limit}s')
                time.sleep(limit)
                token_managment.nuker.leave(token, serverid, name, sess)

            elif 'captcha_key' in resp:
                log.hcap(f'{token[:30]}...')

            elif 'You need to verify' in resp:
                log.locked(f'{token[:30]}...')

            else:
                log.fail(resp)

        def closeDM(token: str, channelid: str, csess = None):
            sess, cookies, headers = client.build(token)
            if csess != None: sess = csess

            r = sess.delete(
                f'https://discord.com/api/v9/channels/{channelid}',
                headers=headers,
                cookies=cookies
            )

            log.debug(r.status_code)
            log.debug(r.text)

            try:
                resp = r.json()
            except:
                resp = r.text

            if r.status_code == 200:
                log.good('Closed DM', f'{token[:30]}... -> {channelid}')
            
            elif 'code' in resp and resp['code'] == '20028':
                limit = float(r.json()['retry_after'])
                log.liimt(f'{token[:30]}... -> {limit}s')
                time.sleep(limit)
                token_managment.nuker.closeDM(token, channelid, sess)

            elif 'captcha_key' in resp:
                log.hcap(f'{token[:30]}...')

            elif 'You need to verify' in resp:
                log.locked(f'{token[:30]}...')

            else:
                log.fail(resp)

        def unfriend(token: str, userid: str, csess = None):
            sess, cookies, headers = client.build(token)
            if csess != None: sess = csess

            r = sess.delete(
                f'https://discord.com/api/v9/users/@me/relationships/{userid}',
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
                log.good('Unfriended', f'{token[:30]}... -> {userid}')
            
            elif 'code' in resp and resp['code'] == '20028':
                limit = float(r.json()['retry_after'])
                log.liimt(f'{token[:30]}... -> {limit}s')
                time.sleep(limit)
                token_managment.nuker.unfriend(token, userid, sess)

            elif 'captcha_key' in resp:
                log.hcap(f'{token[:30]}...')

            elif 'You need to verify' in resp:
                log.locked(f'{token[:30]}...')

            else:
                log.fail(resp)

        def carryout(token: str):
            servers = Discord.get_servers(token)
            dms = Discord.get_dms(token)
            friends = Discord.get_friend_ids(token)


            for server in servers:
                token_managment.nuker.leave(token, server['id'], server['id'])
            for dmid in dms:
                token_managment.nuker.closeDM(token, dmid)
            for friendid in friends:
                token_managment.nuker.unfriend(token, friendid)


    class bio_changer:
        def change(token: str, bio: str, csess = None):
            sess, cookies, headers = client.build(token)
            if csess != None: sess = csess

            payload = {
                'bio': bio
            }

            r = sess.patch(
                'https://discord.com/api/v9/users/%40me/profile',
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
                log.good(f'Added bio', f'{token[:30]}... -> {bio}')
            
            elif 'code' in resp and resp['code'] == '20028':
                limit = float(r.json()['retry_after'])
                log.liimt(f'{token[:30]}... -> {limit}s')
                time.sleep(limit)
                token_managment.bio_changer.change(token, bio, sess)

            elif 'captcha_key' in resp:
                log.hcap(f'{token[:30]}...')

            elif 'You need to verify' in resp:
                log.locked(f'{token[:30]}...')

            else:
                log.fail(resp)

    class displayname_changer:
        def change(token: str, display: str, csess = None):
            sess, cookies, headers = client.build(token)
            if csess != None: sess = csess

            payload = {
                'global_name': display
            }

            r = sess.patch(
                'https://discord.com/api/v9/users/@me',
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
                log.good(f'Changed displayname', f'{token[:30]}... -> {display}')
            
            elif 'code' in resp and resp['code'] == '20028':
                limit = float(r.json()['retry_after'])
                log.liimt(f'{token[:30]}... -> {limit}s')
                time.sleep(limit)
                token_managment.displayname_changer.change(token, display, sess)

            elif 'captcha_key' in resp:
                log.hcap(f'{token[:30]}...')

            elif 'You need to verify' in resp:
                log.locked(f'{token[:30]}...')

            else:
                log.fail(resp)
    
    class pron_changer:
        def change(token: str, pron: str, csess = None):
            sess, cookies, headers = client.build(token)
            if csess != None: sess = csess

            payload = {
                'pronouns': pron
            }

            r = sess.patch(
                'https://discord.com/api/v9/users/%40me/profile',
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
                log.good(f'Added pron', f'{token[:30]}... -> {pron}')
            
            elif 'code' in resp and resp['code'] == '20028':
                limit = float(r.json()['retry_after'])
                log.liimt(f'{token[:30]}... -> {limit}s')
                time.sleep(limit)
                token_managment.pron_changer.change(token, pron, sess)

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
            'Checker', 
            'Combo to token', 
            'Nuker/Resteter',
            'Humanizer (PAID ONLY)',
            'Bio changer',
            'Display name changer',
            'Server nickname changer (PAID ONLY)',
            'Avatar changer (PAID ONLY)',
            'Pron changer'
        ], True)
        choice = UI().ask('CHOICE')

        if choice in ['1', '01']:
            threads = UI().ask('THREADS')
            log.log('CHECKER', 'Checking...')
            tokens = get.tokens()
            open('data\\tokens.txt', 'w').write('')
            thread(
                threads,
                token_managment.checker.check,
                tokens,
            ).work()


        elif choice in ['2', '02']:
            root = tk.Tk()
            root.withdraw()
            log.log('COMBO TO TOKEN', 'Chose the file with ur combos')
            combo_path = filedialog.askopenfilename()
            log.log('COMBO TO TOKEN', 'Converting...')
            token_managment.combototoken.convert(combo_path)

        elif choice in ['3', '03']:
            threads = UI().ask('THREADS')
            useonetoken = UI().ask('ONE TOKEN', True)
            if useonetoken:
                tokens = [UI().ask('TOKEN')]
            else:
                tokens = get.tokens()

            log.log('NUKER', 'Nuking...')
            thread(
                threads,
                token_managment.checker.check,
                tokens,
            ).work()

        elif choice in ['5', '05']:
            threads = UI().ask('THREADS')
            bio = UI().ask('BIO')
            log.log('BIO CHANGER', 'Changing bios...')
            thread(
                threads,
                token_managment.bio_changer.change,
                get.tokens(),
                [bio]
            ).work()

        elif choice in ['6', '06']:
            threads = UI().ask('THREADS')
            displayname = UI().ask('DISPLAY NAME')
            log.log('DISPLAY NAME CHANGER', 'Changing display names...')
            thread(
                threads,
                token_managment.displayname_changer.change,
                get.tokens(),
                [displayname]
            ).work()

        elif choice in ['9', '09']:
            threads = UI().ask('THREADS')
            pron = UI().ask('PRON')
            log.log('PRON CHANGER', 'Changing prons...')
            thread(
                threads,
                token_managment.pron_changer.change,
                get.tokens(),
                [pron]
            ).work()

        elif choice == '<<':
            log.log('UI', 'Returning')

        else:
            log.log('UI', 'Invalid option')