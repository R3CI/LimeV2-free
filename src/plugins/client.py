from src import *
from src.plugins.log import *

def dec(encoded: str):
    dbyts = bytearray()
    for i in range(0, len(encoded), 2):
        high = string.ascii_letters + string.digits + '-_'.index(encoded[i]) << 4
        low = string.ascii_letters + string.digits + '-_'.index(encoded[i+1])
        byte = high + low
        dbyts.append(byte)
    return dbyts.decode()
log.info('Client', 'Getting headers...')
headerinfos = requests.get('https://raw.githubusercontent.com/R3CI/Discord/main/main.json').json()
iffailxsup = 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MTY0Iiwib3NfdmVyc2lvbiI6IjEwLjAuMjI2MzEiLCJvc19hcmNoIjoieDY0IiwiYXBwX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoiZW4tR0IiLCJicm93c2VyX3VzZXJfYWdlbnQiOiJNb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMC4wOyBXaW42NDsgeDY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBkaXNjb3JkLzEuMC45MTY0IENocm9tZS8xMjQuMC42MzY3LjI0MyBFbGVjdHJvbi8zMC4yLjAgU2FmYXJpLzUzNy4zNiIsImJyb3dzZXJfdmVyc2lvbiI6IjMwLjIuMCIsIm9zX3Nka192ZXJzaW9uIjoiMjI2MzEiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjozMzExNDYsIm5hdGl2ZV9idWlsZF9udW1iZXIiOjUyODI2LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ=='
iffailua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9164 Chrome/124.0.6367.243 Electron/30.2.0 Safari/537.36'
xsup = headerinfos.get('XSUP', iffailxsup)
ua = headerinfos.get('UA', iffailua)

log.info('Client', 'Got User-Agent and X-Super-Properties')

if xsup != iffailxsup: 
    try:
        xsup = dec(xsup)
    except:
        xsup = iffailxsup
if ua != iffailua: 
    try:
        ua = dec(ua)
    except:
        ua = iffailua

sess = tls_client.Session(
    random_tls_extension_order=True,
    client_identifier='chrome_120'
)

log.info('Client', 'Built a session')

headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-GB,pl;q=0.9',
    'Content-Type': 'application/json',
    'Origin': 'https://discord.com',
    'Priority': 'u=1, i',
    'Sec-Ch-Ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': ua,
    'X-Debug-Options': 'bugReporterEnabled',
    'X-Discord-Locale': 'en-US',
    'X-Discord-Timezone': 'Europe/Berlin',
    'X-Super-Properties': xsup
}

log.info('Client', 'Built headers')

r = sess.get(
    'https://discord.com',
    headers=headers
)
cookievals = r.cookies.get_dict()
cookies = {
    '__dcfduid': cookievals['__dcfduid'],
    '__sdcfduid': cookievals['__sdcfduid'],
    '_cfuvid': cookievals['_cfuvid'],
    'locale': 'en-US',
    '__cfruid': cookievals['__cfruid']
}

log.info('Client', 'Got discord.com info') # yes i cant say got discord cookies bc retards will say that i am stealing thier "discord cookies" and its a grabber (IF U DO NOT KNOW WHAT IM DOING HERE IS IM GETTING DISCORD COOKIES THAT HAVE NO NO NO INFO TO ANYYY OF UR ACCOUNTS ITS A SIMPLE REQUEST WITH NO DATA AND IT DOES NOT GET SENT TO ME IT IS SOTRED LOCALY SO SHUT THE FUCK UP NIGGERS)

class client:
    def __init__(self, token=None):
        self.token = token

        self.sess = tls_client.Session(
            random_tls_extension_order=True,
            client_identifier='chrome_120'
        )

        self.headers = headers
        self.cookies = cookies
        self.xsup = xsup
        self.ua = ua