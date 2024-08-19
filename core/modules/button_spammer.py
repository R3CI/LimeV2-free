from core import *
from core.plugins.client import *
from core.discordutils import *
from core.plugins.cmd import *
from core.plugins.ui import *
from core.plugins.threads import *
from core.plugins.utils import *

class button_spammer:
    def spam(token: str, channelid: str, messageid: str, serverid: str, customid: str, authorid: str, csess = None):
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
        
        while True:
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
        messagelink = UI().ask('MESSAGE LINK')
        log.log('BUTTON SPAMMER', 'Getting buttons...')

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
                                    buttons.append((component['custom_id'], component['label']))

        for i, (customid, label) in enumerate(buttons, 1):
            LIST.append(f'{label} - {customid}')

        UI().make_menu(LIST, False, 2)

        selected_button = int(UI().ask('CHOICE')) - 1
        customid = buttons[selected_button][0]

        thread(
            threads,
            button_spammer.spam,
            tokens,
            [channelid, messageid, serverid, customid, authorid]
        ).work()