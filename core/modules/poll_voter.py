from core import *
from core.plugins.client import *
from core.discordutils import *
from core.plugins.cmd import *
from core.plugins.ui import *
from core.plugins.threads import *

class poll_voter:
    def vote(token: str, channelid: str, messageid: str, answer, csess = None):
            sess, cookies, headers = client.build(token)
            if csess != None: sess = csess

            payload = {
                'answer_ids': [
                    answer
                ]
            }

            r = sess.put(
                f'https://discord.com/api/v9/channels/{channelid}/polls/{messageid}/answers/@me',
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
                log.good('Voted', f'{token[:30]}...')
            
            elif 'code' in resp and resp['code'] == '20028':
                limit = float(r.json()['retry_after'])
                log.liimt(f'{token[:30]}... -> {limit}s')
                time.sleep(limit)
                poll_voter.vote(token, channelid, messageid, answer)

            elif 'captcha_key' in resp:
                log.hcap(f'{token[:30]}...')

            elif 'You need to verify' in resp:
                log.locked(f'{token[:30]}...')

            else:
                log.fail(resp)
        

    def menu():
        cmd.cls()
        UI().banner()
        threads = UI().ask('THREADS')
        msglink = UI().ask('MESSAGE LINK')
        answer = UI().ask('ANSWER (NUMBER)')    
        
        serverid, channelid, messageid = Discord.extract_messagelink(msglink)
        tokens = Discord.get_server_acces_tokens(serverid)

        log.log('Poll voter', f'Votin on {answer} in{serverid} with {len(tokens)} tokens...')

        thread(
            threads,
            poll_voter.vote,
            tokens,
            [channelid, messageid, answer]
        ).work()