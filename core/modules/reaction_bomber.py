from core import *
from core.plugins.client import *
from core.discordutils import *
from core.plugins.cmd import *
from core.plugins.ui import *
from core.plugins.threads import *

class reaction_bomber:
    def add_reaction(token: str, reaction, channelid: str, messageid: str, csess = None):
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
            reaction_bomber.add_reaction(token, reaction, channelid, messageid, sess)

        elif 'captcha_key' in resp:
            log.hcap(f'{token[:30]}...')

        elif 'You need to verify' in resp:
            log.locked(f'{token[:30]}...')

        else:
            log.fail(resp)

    def carry_out(token: str, reactions: list, channelid: str, messageid: str):
        while True:
            reaction = random.choice(reactions)
            reaction_bomber.add_reaction(token, reaction, channelid, messageid)
            continue



    def menu():
        cmd.cls()
        UI().banner()
        threads = UI().ask('THREADS')
        msglink = UI().ask('MESSAGE LINK')

        tokens = Discord.get_server_acces_tokens(serverid)
        serverid, channelid, messageid = Discord.extract_messagelink(msglink)

        log.log('Reaction bomber', f'Bombing {messageid} with {len(tokens)} tokens...')

        reactions = [
            "😀", "😃", "😄", "😁", "😆", "😅", "😂", "🤣", "😊", "😇",
            "🙂", "🙃", "😉", "😌", "😍", "🥰", "😘", "😗", "😙", "😚",
            "😋", "😜", "😝", "😛", "🤑", "🤗", "🤩", "🤔", "🤨", "🧐",
            "😎", "🤓", "😏", "😒", "😞", "😔", "😟", "😕", "🙁", "☹️",
            "😣", "😖", "😫", "😩", "🥺", "😢", "😭", "😤", "😠", "😡",
            "🤬", "🤯", "😳", "🥵", "🥶", "😱", "😨", "😰", "😥", "😓",
            "🤗", "🤔", "🤭", "🤫", "🤥", "😶", "😐", "😑", "😬", "🙄",
            "😯", "😦", "😧", "😮", "😲", "😵", "😵‍💫", "🤐", "🥴", "😠",
            "😡", "🤬", "😷", "🤒", "🤕", "🤢", "🤮", "🤧", "😇", "🤠",
            "🤡", "🤥", "🤫", "🤭", "🧐", "🤓", "😈", "👿", "👹", "👺",
            "💀", "☠️", "👻", "👽", "👾", "🤖", "🎃", "😺", "😸", "😹",
            "😻", "😼", "😽", "🙀", "😿", "😾", "👋", "🤚", "🖐️", "✋",
            "🖖", "👌", "🤏", "✌️", "🤞", "🤟", "🤘", "🤙", "👈", "👉",
            "👆", "👇", "👍", "👎", "✊", "👊", "🤛", "🤜", "👏", "🙌",
            "👐", "🤲", "🙏", "🤝", "💅", "🤳", "💪", "🦾", "🦿", "🦵",
            "🦶", "👣", "👂", "🦻", "👃", "👀", "👁️", "🧠", "🦷", "🦴",
            "👅", "👄", "💋", "🩸", "💘", "💝", "💖", "💗", "💓", "💞"
        ]

        thread(
            threads,
            reaction_bomber.carry_out,
            tokens,
            [reactions, channelid, messageid]
        ).work()