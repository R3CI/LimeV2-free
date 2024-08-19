from core import *
from core.plugins.client import *
from core.discordutils import *
from core.plugins.cmd import *
from core.plugins.ui import *
from core.plugins.threads import *
from core.plugins.utils import *

class webhook_menu:
    class spammer:
        def spam(webhook: str, message: str, name: str, tts: bool, csess = None):
            sess, cookies, headers = client.build(None)
            if csess != None: sess = csess

            while True:
                payload = {
                    'content': message,
                    'username': name,
                    'tts': tts
                }

                r = sess.post(
                    webhook,
                    headers=headers,
                    cookies=cookies,
                    json=payload,
                )

                webhook_ = webhook.split('/')[-1]

                log.debug(r.status_code)
                log.debug(r.text)

                try:
                    resp = r.json()
                except:
                    resp = r.text

                if r.status_code == 204:
                    log.good('Sent', f'{webhook_[:30]}...')
                    continue
                
                elif 'code' in resp and resp['code'] == '20028':
                    limit = float(r.json()['retry_after'])
                    log.liimt(f'{webhook_[:30]}... -> {limit}s')
                    time.sleep(limit)
                    continue    

                elif 'captcha_key' in resp:
                    log.hcap(f'{webhook_[:30]}...')
                    break

                elif 'You need to verify' in resp:
                    log.locked(f'{webhook_[:30]}...')
                    break

                else:
                    log.fail(resp)  
                    break
    
    class getinfo:
        def getinfo(webhook: str, csess = None):
            sess, cookies, headers = client.build(None)
            if csess != None: sess = csess

            r = sess.get(
                webhook,
                headers=headers,
                cookies=cookies,
            )

            log.debug(r.status_code)
            log.debug(r.text)

            try:
                resp = r.json()
            except:
                resp = r.text

            webhook_ = webhook.split('/')[-1]
            if r.status_code == 200:
                log.good('Got info', f'{webhook_[:30]}...')
                thong = f'''
Username -> {r.json()["name"]}
ID -> {r.json()["id"]}
Server ID -> {r.json()["guild_id"]}
Channel ID -> {r.json()["channel_id"]}
'''
                print(Colorate.Horizontal(Colors.green_to_white, thong))
            
            elif 'code' in resp and resp['code'] == '20028':
                limit = float(r.json()['retry_after'])
                log.liimt(f'{webhook_[:30]}... -> {limit}s')
                time.sleep(limit)  
                webhook_menu.getinfo.getinfo(webhook, sess)

            elif 'captcha_key' in resp:
                log.hcap(f'{webhook_[:30]}...')

            elif 'You need to verify' in resp:
                log.locked(f'{webhook_[:30]}...')

            else:
                log.fail(resp)    


    class change_username:    
        def change(webhook: str, name: str, csess = None):
            sess, cookies, headers = client.build(None)
            if csess != None: sess = csess

            payload = {
                'name': name,
            }

            r = sess.post(
                webhook,
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

            webhook_ = webhook.split('/')[-1]
            if r.status_code == 200:
                log.good('Changed', f'{webhook_[:30]}... -> {name}')
            
            elif 'code' in resp and resp['code'] == '20028':
                limit = float(r.json()['retry_after'])
                log.liimt(f'{webhook_[:30]}... -> {limit}s')
                time.sleep(limit)  
                webhook_menu.change_username.change(webhook, sess)

            elif 'captcha_key' in resp:
                log.hcap(f'{webhook_[:30]}...')

            elif 'You need to verify' in resp:
                log.locked(f'{webhook_[:30]}...')

            else:
                log.fail(resp)    

    class change_avatar:    
        def change(webhook: str, path: str, csess = None):
            sess, cookies, headers = client.build(None)
            if csess != None: sess = csess

            with open(path, 'rb') as f:
                avatar = f.read()

            payload = {
                'avatar': f'data:image/png;base64,{(base64.b64encode(avatar).decode("utf-8"))}'
            }

            r = sess.post(
                webhook,
                headers={
                    'Content-Type': 'application/json'
                },
                cookies=cookies,
                json=payload
            )

            log.debug(r.status_code)
            log.debug(r.text)

            try:
                resp = r.json()
            except:
                resp = r.text

            webhook_ = webhook.split('/')[-1]
            if r.status_code == 200:
                log.good('Changed', f'{webhook_[:30]}...')
            
            elif 'code' in resp and resp['code'] == '20028':
                limit = float(r.json()['retry_after'])
                log.liimt(f'{webhook_[:30]}... -> {limit}s')
                time.sleep(limit)  
                webhook_menu.change_avatar.change(webhook, sess)

            elif 'captcha_key' in resp:
                log.hcap(f'{webhook_[:30]}...')

            elif 'You need to verify' in resp:
                log.locked(f'{webhook_[:30]}...')

            else:
                log.fail(resp)  



    def menu():
        cmd.cls()
        UI().banner()
        UI().make_menu([
            'Spammer', 
            'Info fetcher', 
            'Username changer',
            'Avatar changer',
            'Deleter'
        ], True)
        choice = UI().ask('CHOICE')
        
        if choice in ['01', '1']:
            threads = UI().ask('THREADS')
            webhook = UI().ask('WEBHOOK')
            username = UI().ask('USERNAME')
            message = UI().ask('MESSAGE')
            tts = UI().ask('TTS (ANNOYING ASF)', True)

            log.log('WEBHOOK SPAMMER', 'Spamming webhook...')

            thread(
                threads,
                webhook_menu.spammer.spam,
                [webhook],
                [message, username, tts]
            ).work()

        elif choice in ['02', '2']:
            threads = UI().ask('THREADS')
            webhook = UI().ask('WEBHOOK')

            log.log('WEBHOOK INFO FETCHER', 'Getting info abt the webhook...')

            thread(
                threads,
                webhook_menu.getinfo.getinfo,
                [webhook]
            ).work()

        elif choice in ['03', '3']:
            threads = UI().ask('THREADS')
            webhook = UI().ask('WEBHOOK')
            username = UI().ask('USERNAME')

            log.log('WEBHOOK USERNAME CHANGER', 'Changing webhooks username...')

            thread(
                threads,
                webhook_menu.change_username.change,
                [webhook]
                [username]
            ).work()

        elif choice in ['04', '4']:
            threads = UI().ask('THREADS')
            webhook = UI().ask('WEBHOOK')
            root = tk.Tk()
            root.withdraw()
            path = filedialog.askopenfilename()

            log.log('WEBHOOK AVATAR CHANGER', 'Changing webhooks avatar...')

            thread(
                threads,
                webhook_menu.change_avatar.change,
                [webhook]
                [path]
            ).work()

        elif choice == '<<':
            log.log('UI', 'Returning')

        else:
            log.log('UI', 'Invalid option')