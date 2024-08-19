from core import *
from core.plugins.client import *
from core.discordutils import *
from core.plugins.cmd import *
from core.plugins.ui import *
from core.plugins.threads import *
from core.plugins.utils import *

class bypass_menu:
    class reactor:
        def react(token: str, reaction, channelid: str, messageid: str, csess = None):
            sess, cookies, headers = client.build(token)
            if csess != None: sess = csess

            r = sess.put(
                f'https://discord.com/api/v9/channels/{channelid}/messages/{messageid}/reactions/{reaction}/%40me?location=Message&type=0',
                headers=headers,
                cookies=cookies,
            )

            log.debug(r.status_code)
            log.debug(r.text)

            try:
                resp = r.json()
            except:
                resp = r.text

            if r.status_code == 204:
                log.good('Reacted', f'{token[:30]}...')
            
            elif 'code' in resp and resp['code'] == '20028':
                limit = float(r.json()['retry_after'])
                log.liimt(f'{token[:30]}... -> {limit}s')
                time.sleep(limit)
                bypass_menu.reactor.react(token, reaction, channelid, messageid, sess)

            elif 'captcha_key' in r.text:
                log.hcap(f'{token[:30]}...')

            elif 'You need to verify' in r.text:
                log.locked(f'{token[:30]}...')

            else:
                log.fail(r.text)

        def dereact(token: str, reaction, channelid: str, messageid: str, csess = None):
            sess, cookies, headers = client.build(token)
            if csess != None: sess = csess

            r = sess.delete(
                f'https://discord.com/api/v9/channels/{channelid}/messages/{messageid}/reactions/{reaction}/0/%40me?location=Message&burst=false',
                headers=headers,
                cookies=cookies,
            )

            log.debug(r.status_code)
            log.debug(r.text)

            try:
                resp = r.json()
            except:
                resp = r.text

            if r.status_code == 204:
                log.good('Dereacted', f'{token[:30]}...')
            
            elif 'code' in resp and resp['code'] == '20028':
                limit = float(r.json()['retry_after'])
                log.liimt(f'{token[:30]}... -> {limit}s')
                time.sleep(limit)
                bypass_menu.reactor.dereact(token, reaction, channelid, messageid, sess)

            elif 'captcha_key' in resp:
                log.hcap(f'{token[:30]}...')

            elif 'You need to verify' in resp:
                log.locked(f'{token[:30]}...')

            else:
                log.fail(resp)
    
    class button_clicker:
        def click(token: str, channelid: str, messageid: str, serverid: str, customid: str, authorid: str, csess = None):
            sess, cookies, headers = client.build(token)
            if csess != None: sess = csess

            payload = {
                    'application_id': authorid,
                    'channel_id': channelid,
                    'data': {
                        'component_type': 2,
                        'custom_id': customid,
                    },
                    'guild_id': serverid,
                    'message_flags': 0,
                    'message_id': messageid,
                    'nonce': utils.getnonce(),
                    'session_id': uuid.uuid4().hex,
                    'type': 3,
                }

            r = sess.post(
                f'https://discord.com/api/v9/interactions',
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
                log.good('Clicked', f'{token[:30]}...')
            
            elif 'code' in resp and resp['code'] == '20028':
                limit = float(r.json()['retry_after'])
                log.liimt(f'{token[:30]}... -> {limit}s')
                time.sleep(limit)
                bypass_menu.button_clicker.click(token, channelid, messageid, serverid, customid, authorid, sess)

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
            'Reactor', 
            'Button clicker', 
            'Rule accepter (PAID ONLY)', 
            'Onboard bypasser (PAID ONLY)',
            'Restorecord bypasser (NO CAPTCHA ONLY!) (PAID ONLY)'
            'Choice bot menu thing (PAID ONLY)'
        ], True)
        choice = UI().ask('CHOICE')
        
        if choice in ['01', '1']:
            UI().make_menu([
                'Add reaction', 
                'Remove reaction', 
            ], False, 1)

            choice = UI().ask('CHOICE')
            threads = UI().ask('THREADS')
            messagelink = UI().ask('MESSAGE LINK')
            log.log('REACTOR', 'Getting reactions...')

            found = False
            reacts = []
            LIST = []
            tokens = Discord.get_server_acces_tokens()
            serverid, channelid, messageid = Discord.extract_messagelink(messagelink)
            messages = Discord.get_messages(channelid)
            for message in messages:
                if message['id'] == messageid:
                    found = True
                    for reaction in message['reactions']:
                        emoji_name = reaction['emoji']['name']
                        count = reaction['count']
                        reacts.append((emoji_name, count))

            if not found:
                log.log('REACTOR', 'Message not found')

            for i, (reactionname, count) in enumerate(reacts, 1):
                LIST.append(f'{reactionname} - {count}')

            UI().make_menu(LIST, False, 2)

            selected_reaction = int(UI().ask('CHOICE')) - 1
            reaction_name = reacts[selected_reaction][0]

            if choice in ['01', '1']:
                thread(
                    threads,
                    bypass_menu.reactor.react,
                    tokens,
                    [reaction_name, channelid, messageid]
                ).work()

            elif choice in ['02', '2']:
                thread(
                    threads,
                    bypass_menu.reactor.dereact,
                    tokens,
                    [reaction_name, channelid, messageid]
                ).work()
            
            else:
                log.log('UI', 'Invalid option')
    
        elif choice in ['02', '2']:
            threads = UI().ask('THREADS')
            messagelink = UI().ask('MESSAGE LINK')
            log.log('BUTTON CLICKER', 'Getting buttons...')

            found = False
            buttons = []
            LIST = []
            serverid, channelid, messageid = Discord.extract_messagelink(messagelink)
            tokens = Discord.get_server_acces_tokens(serverid)
            messages = Discord.get_messages(channelid)
            for message in messages:
                if message['id'] == messageid:
                    authorid = message['author']['id']
                    if 'components' in message:
                        for component_group in message['components']:
                            if 'components' in component_group:
                                for component in component_group['components']:
                                    if component['type'] == 2:
                                        found = True
                                        buttons.append((component['custom_id'], component['label']))

            for i, (customid, label) in enumerate(buttons, 1):
                LIST.append(f'{label} - {customid}')

            UI().make_menu(LIST, False, 2)

            selected_button = int(UI().ask('CHOICE')) - 1
            customid = buttons[selected_button][0]

            thread(
                threads,
                bypass_menu.button_clicker.click,
                tokens,
                [channelid, messageid, serverid, customid, authorid]
            ).work()

        elif choice == '<<':
            log.log('UI', 'Returning')

        else:
            log.log('UI', 'Invalid option')