from core import *
from core.plugins.client import *
from core.discordutils import *
from core.plugins.cmd import *
from core.plugins.ui import *
from core.plugins.threads import *

class server_managment:
    class joiner:
        def join(
                token: str, 
                regex: str, 
                serverid: str,
                invite_channelid: str,
                servername: str,
                getsessid: bool,
                csess = None
            ):
            sess, cookies, headers = client.build(token)
            if csess != None: sess = csess

            if getsessid:
                sessionid = Discord.get_sessionid(token)
                log.good('Got sessionid', f'{token[:30]}... -> {sessionid}')
            else:
                sessionid = uuid.uuid4().hex

            payload = {
                'session_id': sessionid,
            }

            xcontent = {
                'location': 'Join Guild',
                'location_guild_id': serverid,
                'location_channel_id': invite_channelid,
                'location_channel_type': 0
            }

            xcontent = json.dumps(xcontent)
            xcontent = xcontent.encode('utf-8')
            xcontent = base64.b64encode(xcontent).decode('utf-8')
            headers['X-Context-Properties'] = xcontent

            r = sess.post(
                f'https://discord.com/api/v9/invites/{regex}',
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
                log.good('Joined', f'{token[:30]}... -> {regex} -> {servername}')
            
            elif 'code' in resp and resp['code'] == '20028':
                limit = float(resp['retry_after'])
                log.liimt(f'{token[:30]}... -> {limit}s')
                time.sleep(limit)
                server_managment.joiner.join(token, regex, serverid, invite_channelid, servername, getsessid, sess)

            elif 'captcha_key' in resp:
                log.hcap(f'{token[:30]}...')

            elif 'You need to verify' in resp:
                log.locked(f'{token[:30]}...')

            else:
                log.fail(r.text)
    
    class leaver:
        def leave(
                token: str, 
                serverid: str,
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
                log.good('Left', f'{token[:30]}... -> {serverid}')
            
            elif 'code' in resp and resp['code'] == '20028':
                limit = float(r.json()['retry_after'])
                log.liimt(f'{token[:30]}... -> {limit}s')
                time.sleep(limit)
                server_managment.leaver.leave(token, serverid, sess)

            elif 'captcha_key' in resp:
                log.hcap(f'{token[:30]}...')

            elif 'You need to verify' in resp:
                log.locked(f'{token[:30]}...')

            else:
                log.fail(resp)

    class server_checker:
        def check(
                token: str, 
                serverid: str,
                csess = None
            ):
            sess, cookies, headers = client.build(token)
            if csess != None: sess = csess

            r = sess.get(
                f'https://discord.com/api/v9/guilds/{serverid}',
                headers=headers,
                cookies=cookies,
            )

            log.debug(r.status_code)
            log.debug(r.text)

            try:
                resp = r.json()
            except:
                resp = r.text

            if r.status_code == 200:
                log.good('Inside', f'{token[:30]}... -> {serverid}')
            
            elif 'code' in resp and resp['code'] == '20028':
                limit = float(r.json()['retry_after'])
                log.liimt(f'{token[:30]}... -> {limit}s')
                time.sleep(limit)
                server_managment.server_checker.check(token, serverid, sess)

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
            'Joiner', 
            'Leaver', 
            'Server checker', 
            'Anti ban (PAID ONLY)'
        ], True)
        choice = UI().ask('CHOICE')
        
        if choice in ['01', '1']:
            threads = UI().ask('THREADS')
            log.log('JOINER', 'Skipping silient as it is paid only')
            getsessid = UI().ask('GET REAL SESSION ID (MAY GET STUCK BUT BETTER BYPASS)', True)
            invite = UI().ask('INVITE')
            log.log('JOINER', 'Checking invite')
            while not Discord.check_invite(Discord.extract_invite(invite)):
                log.log('JOINER', 'Invalid invite')
                invite = UI().ask('INVITE')

            log.log('JOINER', 'Valid invite')
            regex = Discord.extract_invite(invite)

            log.log('JOINER', 'Getting info about server...')
            servername = Discord.get_server_name(regex)
            invite_channelid = Discord.get_invite_channelid(regex)
            serverid = Discord.get_server_id(regex)

            log.log('JOINER', 'Joining...')

            thread(
                threads,
                server_managment.joiner.join,
                get.tokens(),
                [regex, serverid, invite_channelid, servername, getsessid]
            ).work()

        elif choice in ['02', '2']:
            threads = UI().ask('THREADS')
            serverid = UI().ask('SERVER ID')

            log.log('LEAVER', 'Getting tokens that are in the server...')
            tokens = Discord.get_server_acces_tokens(serverid)
            log.log('LEAVER', f'{len(tokens)}/{get.token_count()} Inside of {serverid}')
            log.log('LEAVER', 'Leaving...')

            thread(
                threads,
                server_managment.leaver.leave,
                tokens,
                [serverid]
            ).work()

        elif choice in ['03', '3']:
            threads = UI().ask('THREADS')
            serverid = UI().ask('SERVER ID')

            log.log('SERVER CHECKER', 'Checking...')

            thread(
                threads,
                server_managment.server_checker.check,
                get.tokens(),
                [serverid]
            ).work()

            tokens = Discord.get_server_acces_tokens(serverid)
            log.log('SERVER CHECKER', f'{len(tokens)}/{get.token_count()} Inside of {serverid}')

        elif choice == '<<':
            log.log('UI', 'Returning')

        else:
            log.log('UI', 'Invalid option')