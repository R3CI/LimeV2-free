from core import *
from core.plugins.client import *
from core.discordutils import *
from core.plugins.cmd import *
from core.plugins.ui import *
from core.plugins.threads import *
from core.plugins.utils import *

class spam_call:
    def call(token: str, channelid, userid: str):
        while True:
            if channelid == None:
                channelid = Discord.open_dm(token, userid)

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
                    'guild_id': None,
                    'channel_id': channelid,
                    'self_mute': False,
                    'self_deaf': False
                }
            }))

            ws.send(json.dumps({
                'op': 1,
                'd': None
            }))

            log.good('Called', f'{token[:30]}...')

            time.sleep(1.5)
            ws.send_close(1000, b'Bye') 
            ws.close()
            time.sleep(1.5)
            continue


    def menu():
        cmd.cls()
        UI().banner()
        
        threads = UI().ask('THREADS')
        userid = UI().ask('USER ID')
        #tokens = Discord.get_server_acces_tokens(userid)
        log.log('SPAM CALLER', 'Calling...')

        thread(
            threads,
            spam_call.call,
            tokens,
            [None, userid]
        ).work()
