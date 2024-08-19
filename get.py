from core import *

class get:
    def cookies(headers = None, cookies = None, sess = None):
        if sess == None:
            sess = tls_client.sessions.Session(
                client_identifier='firefox_120', 
                random_tls_extension_order=True
            )

        r = sess.get(
            'https://discord.com',
            headers=headers,
            cookies=cookies
        )

        cookievals = r.cookies.get_dict()
        cookies = {
            '__dcfduid': cookievals['__dcfduid'],
            '__sdcfduid': cookievals['__sdcfduid'],
            '_cfuvid': cookievals['_cfuvid'],
            'locale': 'en-US',
            '__cfruid': cookievals['__cfruid']
        }

        return cookies

    def token_count() -> str:
        return len(open('data\\tokens.txt', 'r').read().splitlines())

    def proxy_count() -> str:
        return len(open('data\\proxies.txt', 'r').read().splitlines())

    def tokens() -> list:
        return open('data\\tokens.txt', 'r').read().splitlines()

    def proxies() -> list:
        return open('data\\proxies.txt', 'r').read().splitlines()
    
    def scraped_ids(serverid: str) -> list:
        return open(f'scrapes\\ids\\{serverid}.txt', 'r').read().splitlines()

    def scraped_usernames(serverid: str) -> list:
        return open(f'scrapes\\usernames\\{serverid}.txt', 'r').read().splitlines()