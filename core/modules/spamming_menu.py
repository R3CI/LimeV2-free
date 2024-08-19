from core import *
from core.plugins.client import *
from core.discordutils import *
from core.plugins.cmd import *
from core.plugins.ui import *
from core.plugins.threads import *
from core.plugins.utils import *

class spamming_memnu:
    class channel_spammer:
        def spam(token: str, serverid: str, channelid: str, messageORGINAL: str, MASSPING: bool, RNDSTRING: bool, RNDEMOJIS: bool, MASSPING_: int, RNDSTRING_: int, RNDEMOJIS_: int, csess = None):
            sess, cookies, headers = client.build(token)
            if csess != None: sess = csess

            while True:
                message = messageORGINAL

                if RNDEMOJIS:
                    emojis = [
                        '😊', '😍', '🥳', '🤩', '😎', 
                        '👍', '👌', '👏', '🙌', '🙏', 
                        '🌟', '🔥', '✨', '🌈', '💖', 
                        '🎉', '🥂', '🍀', '🍎', '🍉', 
                        '☀️', '🌙', '🌸', '🎈', '🎨',
                        '😁', '😂', '🤣', '😅', '😆',
                        '😇', '🙂', '🙃', '😉', '😋',
                        '😌', '😍', '😘', '😗', '😙',
                        '😚', '😜', '😝', '😛', '🤑',
                        '🤗', '🤔', '🤐', '😷', '🤒',
                        '🤕', '🤑', '😲', '😳', '🥺',
                        '🤯', '😬', '😵', '😡', '😠',
                        '😤', '😢', '😭', '😨', '😩',
                        '😰', '😱', '😪', '😓', '🤤',
                        '😴', '😷', '🤒', '🤕', '🤑',
                        '🤠', '😈', '👿', '👹', '👺',
                        '🤡', '💩', '👻', '💀', '👽',
                        '👾', '🤖', '😺', '😸', '😹',
                        '😻', '😼', '😽', '🙀', '😿',
                        '😾', '👋', '🤚', '🖐', '✋',
                        '🖖', '👌', '✌', '🤞', '🤟',
                        '🤘', '🤙', '👈', '👉', '👆',
                        '🖕', '👇', '☝', '👍', '👎',
                        '✊', '👊', '🤛', '🤜', '👏',
                        '🙌', '👐', '🤲', '🤝', '🙏',
                        '✍', '💅', '🤳', '💪', '🦵',
                        '🦶', '👂', '👃', '🧠', '🦷',
                        '🦴', '👀', '👁', '👅', '👄',
                        '💋', '🩸', '👶', '👧', '🧒',
                        '👦', '👩', '🧑', '👨', '👩‍🦱',
                        '🧑‍🦱', '👨‍🦱', '👩‍🦰', '🧑‍🦰', '👨‍🦰',
                        '👱‍♀️', '👱', '👱‍♂️', '👩‍🦳', '🧑‍🦳',
                        '👨‍🦳', '👩‍🦲', '🧑‍🦲', '👨‍🦲', '🧔',
                        '👵', '🧓', '👴', '👲', '👳‍♀️',
                        '👳', '👳‍♂️', '🧕', '👮‍♀️', '👮',
                        '👮‍♂️', '👷‍♀️', '👷', '👷‍♂️', '💂‍♀️',
                        '💂', '💂‍♂️', '🕵️‍♀️', '🕵️', '🕵️‍♂️',
                        '👩‍⚕️', '🧑‍⚕️', '👨‍⚕️', '👩‍🌾', '🧑‍🌾',
                        '👨‍🌾', '👩‍🍳', '🧑‍🍳', '👨‍🍳', '👩‍🎓',
                        '🧑‍🎓', '👨‍🎓', '👩‍🎤', '🧑‍🎤', '👨‍🎤',
                        '👩‍🏫', '🧑‍🏫', '👨‍🏫', '👩‍🏭', '🧑‍🏭',
                        '👨‍🏭', '👩‍💻', '🧑‍💻', '👨‍💻', '👩‍💼',
                        '🧑‍💼', '👨‍💼', '👩‍🔧', '🧑‍🔧', '👨‍🔧',
                    ]
                    selected_emojis = random.sample(emojis, min(int(RNDEMOJIS_), len(emojis)))
                    selected_emojis = ' '.join(selected_emojis)
                    
                    message = f'{message} - {selected_emojis}'

                if RNDSTRING:
                    random_str = utils.random_string(int(RNDSTRING_))
                    message = f'{message} - {random_str}'

                payload = {
                    'content': message, 
                    'tts': True
                }

                r = sess.post(
                    f'https://discord.com/api/v9/channels/{channelid}/messages',
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
                    log.good('Sent', f'{token[:30]}...')
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
        UI().make_menu([
            'Channel spammer',
            'All channel spammer',
            'Thread spammer - TYPE 1 (Makes a threads to the channel)',
            'Thread spammer - TYPE 2 (Makes a threads to random messages from the channel)',
            'Poll spammer'
        ], True)
        choice = UI().ask('CHOICE')

        if choice in ['1', '01']:
            MASSPING_ = 0
            RNDSTRING_ = 0
            RNDEMOJIS_ = 0
            threads = UI().ask('THREADS')
            message = UI().ask('MESSAGE')
            log.log('SPAMMER', 'Skipping mass ping as it is paid only!')
            RNDSTRING = UI().ask('RANDOM STRING', True)
            RNDEMOJIS = UI().ask('RANDOM EMOJIS', True)
            if RNDSTRING:
                RNDSTRING_ = UI().ask('RANDOM STRING LENGTH')
            
            if RNDEMOJIS:
                RNDEMOJIS_ = UI().ask('RANDOM EMOJIS LENGTH')

            serverid = UI().ask('SERVER ID')
            channelid = UI().ask('CHANNEL ID')
    
            log.log('SPAMMER', 'Spamming...')
            tokens = Discord.get_server_acces_tokens(serverid)
            thread(
                threads,
                spamming_memnu.channel_spammer.spam,
                tokens,
                [serverid, channelid, message, False, RNDSTRING, RNDEMOJIS, MASSPING_, RNDSTRING_, RNDEMOJIS_]
            ).work()

        elif choice in ['3', '03']:
            threads = UI().ask('THREADS')
            name = UI().ask('NAME')
            serverid = UI().ask('SERVER ID')
            channelid = UI().ask('CHANNEL ID')

            log.log('THREAD CREATOR', 'Creating...')
            tokens = Discord.get_server_acces_tokens(serverid)
            
            thread(
                threads,
                spamming_memnu.thread_spammer_1.create,
                tokens,
                [channelid, name]
            ).work()

        elif choice in ['4', '04']:
            threads = UI().ask('THREADS')
            name = UI().ask('NAME')
            serverid = UI().ask('SERVER ID')
            channelid = UI().ask('CHANNEL ID')
            log.log('THREAD CREATOR', 'Getting messages...')
            messageids = Discord.get_messages(serverid, channelid)

            log.log('THREAD CREATOR', 'Creating...')
            tokens = Discord.get_server_acces_tokens(serverid)
            
            thread(
                threads,
                spamming_memnu.thread_spammer_2.create,
                tokens,
                [channelid, messageids, name]
            ).work()

        elif choice == '<<':
            log.log('UI', 'Returning')

        else:
            log.log('UI', 'Invalid option')