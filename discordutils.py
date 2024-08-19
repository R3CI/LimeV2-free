from core import *
from core.plugins.log import *
from core.plugins.client import *

class Discord:
    def online(token: str):
        try:
            sess, cookies, headers = client.build(None)
            ws = websocket.WebSocket()
            ws.connect('wss://gateway.discord.gg/?v=9&encoding=json')
            payload = {
                "op": 2,
                "d": {
                    "token": token,
                    "capabilities": 8189,
                    "properties": {
                        "os": "Windows",
                        "browser": "Chrome",
                        "device": "",
                        "system_locale": "en-US",
                        "browser_user_agent": headers['User-Agent'],
                        "browser_version": "111.0.0.0",
                        "os_version": "10",
                        "referrer": "",
                        "referring_domain": "",
                        "referrer_current": "",
                        "referring_domain_current": "",
                        "release_channel": "stable",
                        "client_build_number": 199933,
                        "client_event_source": None,
                        "design_id": 0
                    },
                    "presence": {
                        "status": random.choice(["online", "idle", "dnd"]),
                    },
                    "compress": False,
                    "client_state": {
                        "guild_versions": {},
                        "highest_last_message_id": "0",
                        "read_state_version": 0,
                        "user_guild_settings_version": -1,
                        "user_settings_version": -1,
                        "private_channels_version": "0",
                        "api_code_version": 0
                    }
                }
            }
            ws.send(json.dumps(payload))
        except:
            pass

    def get_sessionid(token: str) -> str:
        # full get sess id only in paid :fire:
        return uuid.uuid4().hex
    

    def check_invite(regex: str, csess = None) -> bool:
        sess, cookies, headers = client.build(None)
        if csess != None: sess = csess

        r = sess.get(
            f'https://discord.com/api/v9/invites/{regex}?inputValue={regex}',
            headers=headers,
            cookies=cookies
        )

        log.debug(r.status_code)
        log.debug(r.text)

        if r.status_code == 200: 
            return True
        
        elif r.json()['code'] == '20028':
            limit = float(r.json()['retry_after'])
            time.sleep(limit)
            Discord.check_invite(regex, sess)

        else:
            return False

    def get_invite_channelid(regex: str, csess = None) -> bool:
        sess, cookies, headers = client.build(None)
        if csess != None: sess = csess

        r = sess.get(
            f'https://discord.com/api/v9/invites/{regex}?inputValue={regex}',
            headers=headers,
            cookies=cookies
        )

        log.debug(r.status_code)
        log.debug(r.text)

        if r.status_code == 200: 
            return r.json()['channel']['id']
        
        elif r.json()['code'] == '20028':
            limit = float(r.json()['retry_after'])
            time.sleep(limit)
            Discord.get_invite_channelid(regex, sess)

        else:
            return None
        
    def get_server_name(regex: str, csess = None) -> str:
        sess, cookies, headers = client.build(None)
        if csess != None: sess = csess

        r = sess.get(
            f'https://discord.com/api/v9/invites/{regex}?inputValue={regex}&with_counts=true&with_expiration=true',
            headers=headers,
            cookies=cookies
        )

        log.debug(r.status_code)
        log.debug(r.text)

        if r.status_code == 200: 
            return r.json()['guild']['name']
        
        elif r.json()['code'] == '20028':
            limit = float(r.json()['retry_after'])
            time.sleep(limit)
            Discord.get_server_name(regex, sess)

        else:
            return None
        
    def get_server_id(regex: str, csess = None) -> str:
        sess, cookies, headers = client.build(None)
        if csess != None: sess = csess

        r = sess.get(
            f'https://discord.com/api/v9/invites/{regex}?inputValue={regex}&with_counts=true&with_expiration=true',
            headers=headers,
            cookies=cookies
        )

        log.debug(r.status_code)
        log.debug(r.text)

        if r.status_code == 200: 
            return r.json()['guild']['id']
        else:
            return None
        
    def get_messages(channelid: str, token = None, csess = None) -> dict:
        if token == None:
            for token in get.tokens():
                sess, cookies, headers = client.build(token)
                if csess != None: sess = csess
                r = sess.get(
                    f'https://discord.com/api/v9/channels/{channelid}/messages?limit=50',
                    headers=headers,
                    cookies=cookies
                )

                log.debug(r.status_code)
                log.debug(r.text)

                if r.status_code == 200:
                    return r.json()
                
                elif r.json()['code'] == '20028':
                    limit = float(r.json()['retry_after'])
                    time.sleep(limit)
                    Discord.get_server_acces_tokens(channelid, token, sess)

                else:
                    pass
            
            return {}
        else:
            sess, cookies, headers = client.build(token)
            if csess != None: sess = csess
            r = sess.get(
                f'https://discord.com/api/v9/channels/{channelid}/messages?limit=50',
                headers=headers,
                cookies=cookies
            )

            log.debug(r.status_code)
            log.debug(r.text)

            if r.status_code == 200:
                return r.json()

            elif r.json()['code'] == '20028':
                limit = float(r.json()['retry_after'])
                time.sleep(limit)
                Discord.get_messages(channelid, token, sess)

            else:
                return {}
            
    def get_soundboard(token = None, csess = None) -> dict:
        if token == None:
            for token in get.tokens():
                sess, cookies, headers = client.build(token)
                if csess != None: sess = csess
                r = sess.get(
                    f'https://discord.com/api/v9/soundboard-default-sounds',
                    headers=headers,
                    cookies=cookies
                )

                log.debug(r.status_code)
                log.debug(r.text)

                if r.status_code == 200:
                    return r.json()
                
                elif r.json()['code'] == '20028':
                    limit = float(r.json()['retry_after'])
                    time.sleep(limit)
                    Discord.get_soundboard(token, sess)
            
            return {}
        else:
            sess, cookies, headers = client.build(token)
            if csess != None: sess = csess
            r = sess.get(
                f'https://discord.com/api/v9/soundboard-default-sounds',
                headers=headers,
                cookies=cookies
            )

            log.debug(r.status_code)
            log.debug(r.text)

            if r.status_code == 200:
                return r.json()

            elif r.json()['code'] == '20028':
                limit = float(r.json()['retry_after'])
                time.sleep(limit)
                Discord.get_soundboard(token, sess)

            else:
                return {}
            
    def get_server_acces_tokens(serverid: str, token = None, csess = None) -> list:
        acces = []

        if token == None:
            for token in get.tokens():
                sess, cookies, headers = client.build(token)
                if csess != None: sess = csess
                r = sess.get(
                    f'https://discord.com/api/v9/guilds/{serverid}',
                    headers=headers,
                    cookies=cookies
                )

                log.debug(r.status_code)
                log.debug(r.text)

                if r.status_code == 200:
                    acces.append(token)

                elif r.json()['code'] == '20028':
                    limit = float(r.json()['retry_after'])
                    time.sleep(limit)
                    Discord.get_server_acces_tokens(serverid, token, sess)

                log.debug(acces)
                return acces

        else:
            sess, cookies, headers = client.build(token)
            if csess != None: sess = csess
            r = sess.get(
                f'https://discord.com/api/v9/guilds/{serverid}',
                headers=headers,
                cookies=cookies
            )

            log.debug(r.status_code)
            log.debug(r.text)

            if r.status_code == 200:
                return [token]
            
            elif r.json()['code'] == '20028':
                limit = float(r.json()['retry_after'])
                time.sleep(limit)
                Discord.get_server_acces_tokens(serverid, token, sess)

            else:
                return []
            
    def get_servers(token: str, csess = None) -> list:    
        sess, cookies, headers = client.build(token)
        if csess != None: sess = csess
        servers = []

        r = sess.get(
            f'https://discord.com/api/v9/users/@me/guilds',
            headers=headers,
            cookies=cookies
        )

        log.debug(r.status_code)
        log.debug(r.text)

        if r.status_code == 200:
            for server in r.json():
                serverid = server['id']
                servername = server['name']
                servers.append({'id': serverid, 'name': servername})
        
        elif r.json()['code'] == '20028':
            limit = float(r.json()['retry_after'])
            time.sleep(limit)
            Discord.get_servers(token, sess)

        log.debug(servers)
        
        return servers
    
    def get_dms(token: str, csess = None) -> list:    
        sess, cookies, headers = client.build(token)
        if csess != None: sess = csess
        dms = []

        r = sess.get(
            f'https://discord.com/api/v9/users/@me/channels',
            headers=headers,
            cookies=cookies
        )

        log.debug(r.status_code)
        log.debug(r.text)

        if r.status_code == 200:
            for dm in r.json():
                dmid = dm['id']
                dms.append(dmid)
        
        elif r.json()['code'] == '20028':
            limit = float(r.json()['retry_after'])
            time.sleep(limit)
            Discord.get_dms(token, sess)     
        
        log.debug(dms)
        return dms

    def get_friend_ids(token: str, csess = None) -> list:
        sess, cookies, headers = client.build(token)
        if csess != None: sess = csess
        friends = []

        r = sess.get(
            f'https://discord.com/api/v9/users/@me/relationships',
            headers=headers,
            cookies=cookies
        )

        log.debug(r.status_code)
        log.debug(r.text)

        if r.status_code == 200:
            for id in r.json():
                friends.append(id['id'])  

        elif r.json()['code'] == '20028':
            limit = float(r.json()['retry_after'])
            time.sleep(limit)
            Discord.get_friend_ids(token, sess)

        log.debug(friends)
        return friends
    
    def open_dm(token: str, userid: str, csess = None) -> str:
        sess, cookies, headers = client.build(token)
        if csess != None: sess = csess

        payload = {
            'recipients': [userid]
        }

        r = sess.post(
            f'https://discord.com/api/v9/users/@me/channels',
            headers=headers,
            cookies=cookies,
            json=payload
        )

        log.debug(r.status_code)
        log.debug(r.text)

        if r.status_code == 200:
            r.json()['id']

        elif r.json()['code'] == '20028':
            limit = float(r.json()['retry_after'])
            time.sleep(limit)
            Discord.open_dm(token, userid, sess)

    def extract_invite(invite: str) -> str:
        match = re.search(r'(?:(?:http:\/\/|https:\/\/)?discord\.gg\/|discordapp\.com\/invite\/|discord\.com\/invite\/)?([a-zA-Z0-9-]+)', invite)
        if match: invite =  match.group(1)
        log.debug(invite)
        return invite

    def getid(token: str) -> str:
        period_pos = token.find('.')
        if period_pos != -1: cut = token[:period_pos]
        id = base64.b64decode(cut + '==').decode()
        log.debug(id)
        return id
    
    def extract_channellink(url: str) -> str:
        parts = url.split('/')
        serverid = parts[4]
        channelid = parts[5]
        return serverid, channelid
    
    def extract_messagelink(url: str) -> str:
        parts = url.split('/')
        serverid = parts[4]
        channelid = parts[5]
        messageid = parts[6]
        return serverid, channelid, messageid