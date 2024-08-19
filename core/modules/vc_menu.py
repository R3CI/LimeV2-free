from core import *
from core.plugins.client import *
from core.discordutils import *
from core.plugins.cmd import *
from core.plugins.ui import *
from core.plugins.threads import *
from core.plugins.utils import *

class vc_menu:
    class joiner:
        def join(token: str, channelid: str, serverid: str, keep: bool = False):
            ws = websocket.WebSocket()
            ws.connect('wss://gateway.discord.gg/?v=9&encoding=json')

            r = json.loads(ws.recv())
            ws.send(json.dumps({
                'op': 2,
                'd': {
                    'token': token,
                    'properties': {
                        '$os': 'windows',
                        '$browser': 'Discord',
                        '$device': 'desktop'
                    }
                }
            }))

            ws.send(json.dumps({
                'op': 4,
                'd': {
                    'guild_id': serverid,
                    'channel_id': channelid,
                    'self_mute': False,
                    'self_deaf': False
                }
            }))

            log.good('Joined', f'{token[:30]}...')
            if keep:
                while True:
                    ws.recv()
                    time.sleep(r['d']['heartbeat_interval'] / 1000)
                    log.good('Kept alive', f'{token[:30]}... -> {r["d"]["heartbeat_interval"] / 1000}s')
                    continue

    class spamjoinleave:
        def spam(token: str, channelid: str, serverid: str):
            while True:
                ws = websocket.WebSocket()
                ws.connect('wss://gateway.discord.gg/?v=9&encoding=json')
                r = json.loads(ws.recv())
                ws.send(json.dumps({
                    'op': 2,
                    'd': {
                        'token': token,
                        'properties': {
                            '$os': 'windows',
                            '$browser': 'Discord',
                            '$device': 'desktop'
                        }
                    }
                }))

                ws.send(json.dumps({
                    'op': 4,
                    'd': {
                        'guild_id': serverid,
                        'channel_id': channelid,
                        'self_mute': False,
                        'self_deaf': False
                    }
                }))

                log.good('Joined', f'{token[:30]}... -> {channelid}')
                delay = random.randint(1, 3)
                time.sleep(delay)
                log.good('Left', f'{token[:30]}... -> {channelid} -> w/ {delay}s delay')
                continue


    def menu():
        cmd.cls()
        UI().banner()
        UI().make_menu([
            'Joiner', 
            'Spam join -> leave (Best with lots of tokens)', 
            'Soundboard spammer (PAID ONLY)'
        ], True)
        choice = UI().ask('CHOICE')
        
        if choice in ['01', '1']:
            threads = UI().ask('THREADS')
            serverid = UI().ask('SERVER ID')
            channelid = UI().ask('CHANNEL ID')
            keep = UI().ask('KEEP SOCKET ALIVE', True)
            tokens = Discord.get_server_acces_tokens(serverid)
            log.log('VC JOINER', 'Joining VC...')

            thread(
                threads,
                vc_menu.joiner.join,
                tokens,
                [channelid, serverid, keep]
            ).work()

        elif choice in ['02', '2']:
            log.log('VC SPAM JOINER', 'Wont work sometimes working on it')
            threads = UI().ask('THREADS')
            serverid = UI().ask('SERVER ID')
            channelid = UI().ask('CHANNEL ID')
            tokens = Discord.get_server_acces_tokens(serverid)
            
            log.log('VC SPAM JOINER', 'Spamming VC...')

            thread(
                threads,
                vc_menu.spamjoinleave.spam,
                tokens,
                [channelid, serverid]
            ).work()


        elif choice == '<<':
            log.log('UI', 'Returning')

        else:
            log.log('UI', 'Invalid option')