from core import *
from core.plugins.get import *
from core.plugins.config import cfg
from core.plugins.log import *

class client:
    def __init__(self):
        self.thingthong = string.ascii_letters + string.digits + '-_'
        if cfg().customua() == '':
            self.ua = requests.get('https://raw.githubusercontent.com/R3CI/Discord/main/main.json').json()['UA']
            self.ua = self.decode(self.ua)
        else:
            self.ua = cfg().customua()
        log.log('HEADERS', 'Got user agent')

        if cfg().customxsup() == '':
            self.xsup = requests.get('https://raw.githubusercontent.com/R3CI/Discord/main/main.json').json()['XSUP']
            self.xsup = self.decode(self.xsup)
        else:
            self.xsup = cfg().customxsup()
        log.log('HEADERS', 'Got xsup props')


        self.cookies = get.cookies(self.getheadersforcookies())
        log.log('HEADERS', 'Got cookies')

    def decode(self, encoded: str):
        decoded_bytes = bytearray()
        
        for i in range(0, len(encoded), 2):
            high = self.thingthong.index(encoded[i]) << 4
            low = self.thingthong.index(encoded[i+1])
            byte = high + low
            decoded_bytes.append(byte)
        
        return decoded_bytes.decode()

    def build(self, token = None) -> tuple[tls_client.Session, dict, dict]:
        sess = tls_client.Session(
            client_identifier='chrome_120',
            random_tls_extension_order=True,
        )        

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
            'User-Agent': self.ua,
            'X-Debug-Options': 'bugReporterEnabled',
            'X-Discord-Locale': 'en-US',
            'X-Discord-Timezone': 'Europe/Berlin',
            'X-Super-Properties': self.xsup
        }

        if token != None:
            headers['Authorization'] = token

        return sess, self.cookies, headers
    
    def getheadersforcookies(self):    
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
            'User-Agent': self.ua,
            'X-Debug-Options': 'bugReporterEnabled',
            'X-Discord-Locale': 'en-US',
            'X-Discord-Timezone': 'Europe/Berlin',
            'X-Super-Properties': self.xsup
        }

        return headers

client = client()
